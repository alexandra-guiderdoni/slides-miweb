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

- **Première idée.**
- Deuxième idée.
- Troisième idée.

#### Impact du non-respect

- Conséquence concrète.

#### Ce que garantit la règle

- **Quatrième idée.**

### Objet du contrôle

- Cinquième idée.
"""

VALID_FINAL_NOTES = """### Une synthèse directe

- **Première idée.**
- Deuxième idée.
- Troisième idée.

### Limite de preuve

- Quatrième idée.
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

    def test_required_rule_guarantee_heading_is_accepted(self):
        issues = checker.validate_slides(self.valid_slides())

        self.assertFalse(
            any("Ce que garantit la règle" in message for message in self.messages(issues))
        )

    def test_missing_notes_and_required_fields_are_rejected(self):
        slides = self.valid_slides()
        del slides[0]["notes_orateur"]
        del slides[0]["description"]

        issues = checker.validate_slides(slides)
        messages = self.messages(issues, "ERREUR")

        self.assertTrue(any("champs manquants" in message for message in messages))
        self.assertTrue(any("notes_orateur" in message for message in messages))

    def test_generic_headings_are_rejected(self):
        slides = self.valid_slides()
        slides[0]["notes_orateur"] = """### Introduction

- **Une idée.**
- Une deuxième idée.
- Une troisième idée.

### Transition

- Une quatrième idée.
"""

        issues = checker.validate_slides(slides)
        messages = self.messages(issues, "ERREUR")

        self.assertEqual(1, sum("métapédagogique" in message for message in messages))

    def test_transition_is_allowed_beyond_content_headings(self):
        slides = self.valid_slides()
        slides[0]["notes_orateur"] += "\n### Transition\n\n- Le choix conduit ensuite au paiement.\n"
        slides[1]["notes_orateur"] += "\n### Conclusion\n\n- Le parcours reste vérifiable.\n"
        self.assertEqual([], checker.validate_slides(slides))

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

    def test_missing_bullets_bold_and_semantic_hierarchy_are_rejected(self):
        slides = self.valid_slides()
        slides[0]["notes_orateur"] = "### Une règle\n\nTexte sans liste."
        slides[1]["notes_orateur"] = "### Synthèse\n\nTexte sans liste."

        issues = checker.validate_slides(slides)
        messages = self.messages(issues, "ERREUR")

        self.assertEqual(2, sum("aucune liste" in message for message in messages))
        self.assertEqual(2, sum("mise en valeur en gras" in message for message in messages))
        self.assertEqual(2, sum("entre 2 et 4 titres" in message for message in messages))
        self.assertEqual(2, sum("ligne non structurée" in message for message in messages))

    def test_semantic_headings_need_no_transition_or_conclusion(self):
        slides = [
            slide(1, "Premier bloc", VALID_RULE_NOTES),
            slide(2, "Dernier bloc", VALID_FINAL_NOTES),
        ]

        self.assertEqual([], checker.validate_slides(slides))

    def test_multiple_sentences_on_one_line_are_rejected(self):
        slides = self.valid_slides()
        slides[0]["notes_orateur"] = VALID_RULE_NOTES.replace(
            "- Deuxième idée.",
            "- Deuxième idée. Une autre phrase suit.",
        )

        issues = checker.validate_slides(slides)

        self.assertTrue(
            any("plusieurs phrases" in message for message in self.messages(issues, "ERREUR"))
        )

    def test_ordered_questions_are_accepted_as_structured_list(self):
        slides = self.valid_slides()
        slides[0]["notes_orateur"] = """### Quatre diagnostics distincts

- La **performance** mobilise plusieurs ressources.

1. **Rapide** : combien de temps faut-il ?
2. **Léger** : quel volume faut-il transférer ?
3. **Affiché** : les éléments sont-ils visibles ?
4. **Utilisable** : les commandes répondent-elles ?

### Limite de lecture

- Une connexion rapide peut masquer un transfert lourd.
- Un appareil récent peut masquer des calculs longs.
- Ces diagnostics restent distincts.
"""

        issues = checker.validate_slides(slides)

        self.assertEqual([], issues)

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

- **Première idée.**
- Deuxième idée.

### Limite

- Troisième idée.
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
