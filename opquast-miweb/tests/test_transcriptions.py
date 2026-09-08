import unittest
import zipfile
from pathlib import Path

from test_site_contracts import load_build_module


class TranscriptionsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.build = load_build_module()
        cls.slides = cls.build.load_slides()

    def test_tables_keep_labels_and_values_associated(self):
        rubriques = self.slides[5]["transcription"][0]["tableau"]
        self.assertEqual([
            ["E-Commerce", "39"], ["Formulaires", "30"], ["Sécurité", "21"],
            ["Navigation", "20"], ["Contact", "17"], ["Liens", "17"],
        ], rubriques["lignes"])
        mnemonic = self.slides[14]["transcription"][1]["tableau"]
        self.assertEqual([["V", "Va"], ["P", "Pas"], ["T", "Te"],
                          ["C", "Croire"], ["S", "Supérieur"]], mnemonic["lignes"])
        rendered = self.build.render_transcription(self.slides[14], 3)
        self.assertIn('<th scope="col">Lettre</th>', rendered)
        self.assertIn('<th scope="row">V</th><td>Va</td>', rendered)
        self.assertIn('<caption', rendered)

    def test_nested_headings_keep_ux_and_responsibilities_readable(self):
        for level in (3, 5):
            rendered = self.build.render_transcription(self.slides[16], level)
            self.assertIn(f"<h{level}>UX - Parcours</h{level}>", rendered)
            for title in ("Avant", "Pendant", "Après"):
                self.assertIn(f"<h{level + 1}>{title}</h{level + 1}>", rendered)
            self.assertNotIn("<h7>", rendered)
        responsibilities = self.slides[20]["transcription"]
        self.assertEqual(["V - Visibilité", "P - Perception", "T - Technique",
                          "C - Contenus", "S - Services"], [b["titre"] for b in responsibilities[1:]])
        self.assertEqual(["Sécurité, Hébergement, Performance, Conformité W3C."],
                         responsibilities[3]["paragraphes"])

    def test_schema_rejects_broken_tables_and_excessive_depth(self):
        examples = [
            [],
            [{"titre": "Vide"}],
            [{"titre": "Erreur", "texte": "Champ inconnu"}],
            [{"titre": "Tableau", "tableau": {"entetes": ["A", "B"], "lignes": [["A"]]}}],
            [{"titre": "Niveau 1", "sections": [{"titre": "Niveau 2", "sections": [
                {"titre": "Niveau 3", "paragraphes": ["Trop profond"]}]}]}],
        ]
        for blocks in examples:
            with self.subTest(blocks=blocks), self.assertRaises(ValueError):
                self.build.validate_transcription(blocks, 1)
        blocks = [{"titre": "<script>titre</script>", "paragraphes": ["<img src=x>"],
                   "tableau": {"entetes": ["Repère", "Valeur"], "lignes": [["A|B", "<script>x</script>"]]}}]
        self.build.validate_transcription(blocks, 1)
        rendered = self.build.render_transcription_blocks(blocks, 3)
        self.assertNotIn("<script>", rendered)
        self.assertNotIn("<img", rendered)
        self.assertIn("&lt;script&gt;", rendered)
        self.assertIn("A\\|B", "\n".join(self.build.markdown_transcription(blocks)))

    def test_download_includes_the_current_structured_transcriptions(self):
        root = Path(__file__).resolve().parents[1]
        markdown = self.build.render_markdown(self.slides)
        self.assertIn("### UX - Parcours\n\n#### Avant", markdown)
        self.assertIn("| V | Va |", markdown)
        self.assertIn("### T - Technique", markdown)
        self.assertIn("450 euros HT", markdown)
        self.assertIn("485 € HT", markdown)
        with zipfile.ZipFile(root / "assets/downloads/opquast-miweb-slides.zip") as archive:
            self.assertEqual(markdown, archive.read("alternatives.md").decode())
