import copy
import html
import hashlib
import json
import unittest
from pathlib import Path

from test_site_contracts import load_build_module


class DiscoursTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.build = load_build_module()
        cls.slides = cls.build.load_slides()

    def test_all_slides_expose_distinct_transcription_and_discours(self):
        index = self.build.render_v1_index(self.slides)
        alternatives = self.build.render_alternatives(self.slides)
        markdown = self.build.render_markdown(self.slides)
        self.assertEqual(44, len(self.slides))
        self.assertEqual(44, markdown.count("### Discours oral"))
        for slide in self.slides:
            sid = self.build.slide_id(slide)
            self.assertIn(f'aria-controls="discours-{sid}"', index)
            self.assertIn(f'id="alternative-{sid}"', index)
            self.assertIn(slide["notes_orateur"].strip(), markdown)
            first_line = html.escape(slide["notes_orateur"].strip().splitlines()[0], quote=True)
            if first_line.startswith("- "):
                first_line = first_line[2:]
            self.assertIn(first_line, alternatives)

    def test_price_update_keeps_visible_source_text(self):
        slide = self.slides[-1]
        self.assertIn("450", slide["textes_visibles"])
        self.assertIn("485 euros hors taxes", slide["notes_orateur"])
        self.assertNotIn("450 euros hors taxes", slide["notes_orateur"])
        for output in (self.build.render_v1_index(self.slides),
                       self.build.render_alternatives(self.slides),
                       self.build.render_markdown(self.slides)):
            self.assertIn("485 € HT", output)
            self.assertIn("https://www.opquast.com/certification/", output)

    def test_published_assets_and_notes_match_provenance(self):
        root = Path(__file__).resolve().parents[1]
        provenance = json.loads((root / "source/provenance.json").read_text())
        self.assertEqual(44, len(provenance["slides"]))
        for slide, source in zip(self.slides, provenance["slides"]):
            with self.subTest(slide=slide["numero"]):
                self.assertEqual(slide["numero"], source["slide"])
                image = (root / slide["image"]).read_bytes()
                self.assertEqual(hashlib.sha256(image).hexdigest(), source["published_sha256"])
                notes = slide["notes_orateur"]
                if slide["numero"] == 15:
                    notes, formulas = notes.split("\n\nAutres formules mnémotechniques :\n\n", 1)
                    self.assertEqual(10, len(formulas.splitlines()))
                if slide["numero"] == 44:
                    notes = notes.replace(
                        "485 euros hors taxes (tarif vérifié le 8 septembre 2026)",
                        "450 euros hors taxes",
                    )
                self.assertEqual(hashlib.sha256(notes.encode()).hexdigest(), source["original_notes_sha256"])

    def test_notes_are_required_and_escaped(self):
        slide = copy.deepcopy(self.slides[0])
        slide["notes_orateur"] = ""
        with self.assertRaises(ValueError):
            self.build.validate_slide_contract(slide, 1)
        slide["notes_orateur"] = '<script>alert("x")</script>\nDeuxième ligne\n\n- Une étape'
        rendered = self.build.render_discours(slide)
        self.assertNotIn("<script>", rendered)
        self.assertIn("&lt;script&gt;", rendered)
        self.assertIn("<br>Deuxième ligne", rendered)
        self.assertIn("<ul><li>Une étape</li></ul>", rendered)

    def test_precision_rejects_active_urls(self):
        slide = copy.deepcopy(self.slides[-1])
        slide["precision"]["url"] = "javascript:alert(1)"
        with self.assertRaises(ValueError):
            self.build.validate_slide_contract(slide, 44)
