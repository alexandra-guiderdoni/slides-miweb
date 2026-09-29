import copy
import json
import subprocess
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory


REPO_ROOT = Path(__file__).resolve().parents[2]
SCRIPTS_DIR = REPO_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

import check_notes_orales_opquast as checker  # noqa: E402


def slide(numero, titre, notes, transcription="### Contenu affiché\n\nTexte distinct."):
    return {
        "numero": numero,
        "titre": titre,
        "image": f"assets/slides/slide-{numero:02d}.png",
        "alt": "Alternative courte",
        "description": "Description complète.",
        "textes_visibles": [titre],
        "message": "Message à retenir.",
        "transcription": transcription,
        "notes_orateur": notes,
    }


VALID_RULE_NOTES = """### Une règle expliquée

- Première idée.
- Deuxième idée.
- Troisième idée.
- Quatrième idée.

#### Impact du non-respect

- Préjudice concret.

#### Ce que garantit la règle

- Garantie concrète.

### Transition

Passage vers l’idée suivante.
"""

VALID_FINAL_NOTES = """### Une synthèse directe

- Première idée.
- Deuxième idée.
- Troisième idée.
- Quatrième idée.

### Conclusion

Conclusion générale.
"""


class CheckNotesOralesOpquastTest(unittest.TestCase):
    def valid_slides(self):
        first = slide(1, "Règle 999 : exemple", VALID_RULE_NOTES)
        first["textes_visibles"].append("RÈGLE 999")
        return [first, slide(2, "Synthèse", VALID_FINAL_NOTES)]

    def messages(self, issues, severity=None):
        return [
            issue.message
            for issue in issues
            if severity is None or issue.severity == severity
        ]

    def test_valid_series_passes_without_issue(self):
        self.assertEqual([], checker.validate_slides(self.valid_slides()))

    def test_missing_notes_and_required_fields_are_rejected(self):
        slides = self.valid_slides()
        del slides[0]["notes_orateur"]
        del slides[0]["description"]

        issues = checker.validate_slides(slides)
        messages = self.messages(issues, "ERREUR")

        self.assertTrue(any("champs manquants" in message for message in messages))
        self.assertTrue(any("notes_orateur" in message for message in messages))

    def test_rule_requires_impact_and_guarantee(self):
        slides = self.valid_slides()
        slides[0]["titre"] = "Règle n° 999 : exemple"
        slides[0]["notes_orateur"] = """### Une règle

- Une idée.
- Une deuxième idée.
- Une troisième idée.
- Une quatrième idée.

### Transition

Suite.
"""

        issues = checker.validate_slides(slides)
        messages = self.messages(issues, "ERREUR")

        self.assertTrue(any("Impact du non-respect" in message for message in messages))
        self.assertTrue(any("Ce que garantit la règle" in message for message in messages))

    def test_metapedagogy_and_long_dash_are_rejected(self):
        slides = self.valid_slides()
        slides[0]["notes_orateur"] = VALID_RULE_NOTES.replace(
            "### Une règle expliquée",
            "### Intention pédagogique",
        ).replace("Première idée.", "Demandez au groupe — première idée.")

        issues = checker.validate_slides(slides)
        messages = self.messages(issues, "ERREUR")

        self.assertTrue(any("métapédagogique" in message for message in messages))
        self.assertTrue(any("gestion du groupe" in message for message in messages))
        self.assertTrue(any("tiret long" in message for message in messages))

    def test_missing_bullets_transition_and_conclusion_are_rejected(self):
        slides = self.valid_slides()
        slides[0]["notes_orateur"] = "### Une règle\n\nTexte sans liste."
        slides[1]["notes_orateur"] = "### Synthèse\n\nTexte sans liste."

        issues = checker.validate_slides(slides)
        messages = self.messages(issues, "ERREUR")

        self.assertEqual(2, sum("aucune liste" in message for message in messages))
        self.assertTrue(any("Transition" in message for message in messages))
        self.assertTrue(any("conclusion" in message for message in messages))

    def test_non_final_conclusion_does_not_require_transition(self):
        slides = [
            slide(1, "Conclusion de bloc", VALID_FINAL_NOTES),
            slide(2, "Conclusion finale", VALID_FINAL_NOTES),
        ]

        self.assertEqual([], checker.validate_slides(slides))

    def test_exact_transcription_repetition_is_rejected(self):
        slides = self.valid_slides()
        notes = slides[1]["notes_orateur"]
        slides[1]["transcription"] = notes

        issues = checker.validate_slides(slides)

        self.assertTrue(
            any("répète exactement" in message for message in self.messages(issues, "ERREUR"))
        )

    def test_less_than_four_bullets_produces_warning_only(self):
        slides = self.valid_slides()
        slides[1]["notes_orateur"] = """### Synthèse

- Première idée.
- Deuxième idée.
- Troisième idée.

### Conclusion

Conclusion générale.
"""

        issues = checker.validate_slides(slides)

        self.assertFalse(self.messages(issues, "ERREUR"))
        self.assertTrue(any("3 puce" in message for message in self.messages(issues, "AVERTISSEMENT")))

    def test_cli_returns_nonzero_on_error(self):
        with TemporaryDirectory() as tmp_dir:
            target = Path(tmp_dir) / "jeu"
            target.mkdir()
            slides = self.valid_slides()
            slides[0] = copy.deepcopy(slides[0])
            slides[0]["notes_orateur"] = ""
            (target / "slides.json").write_text(
                json.dumps(slides, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )

            result = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPTS_DIR / "check_notes_orales_opquast.py"),
                    str(target),
                ],
                check=False,
                capture_output=True,
                text=True,
            )

        self.assertEqual(1, result.returncode)
        self.assertIn("ERREUR slide 1", result.stdout)


if __name__ == "__main__":
    unittest.main()
