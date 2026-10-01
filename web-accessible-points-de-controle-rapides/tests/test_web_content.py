from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class WebAccessibleContentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.slides = json.loads((ROOT / "slides.json").read_text(encoding="utf-8"))
        cls.index = (ROOT / "index.html").read_text(encoding="utf-8")
        cls.alternatives = (ROOT / "alternatives.html").read_text(encoding="utf-8")

    def test_thirty_slides_and_final_images_only(self) -> None:
        self.assertEqual([slide["numero"] for slide in self.slides], list(range(1, 31)))
        images = sorted((ROOT / "assets" / "slides").glob("slide-*.png"))
        self.assertEqual(len(images), 30)
        self.assertEqual(images[0].name, "slide-01.png")
        self.assertEqual(images[-1].name, "slide-30.png")

    def test_storyboard_transcriptions_and_notes_are_exact(self) -> None:
        source = (ROOT / "source" / "storyboard.md").read_text(encoding="utf-8")
        slide_headings = list(
            re.finditer(r"^## Slide (\d{2}) - (.+)$", source, re.MULTILINE)
        )
        level_two_headings = list(re.finditer(r"^## .+$", source, re.MULTILINE))
        self.assertEqual(len(slide_headings), 30)
        for slide, heading in zip(self.slides, slide_headings, strict=True):
            end = next(
                (
                    item.start()
                    for item in level_two_headings
                    if item.start() > heading.start()
                ),
                len(source),
            )
            section = source[heading.end() : end]
            _, remainder = section.split("### Transcription exacte", 1)
            transcription, notes = remainder.split("### Discours oral exact", 1)
            self.assertEqual(slide["transcription"], transcription.strip())
            self.assertEqual(slide["notes_orateur"], notes.strip())

    def test_two_accordions_per_slide(self) -> None:
        self.assertEqual(
            len(re.findall(r"<button[^>]+data-alternative-button", self.index)), 30
        )
        self.assertEqual(self.index.count("Lire le discours oral de la slide"), 30)

    def test_markdown_tables_are_semantic_html_tables(self) -> None:
        for page in (self.index, self.alternatives):
            self.assertEqual(page.count("<table>"), 7)
            self.assertEqual(page.count("<caption>"), 7)
            self.assertEqual(page.count("<thead>"), 7)
            self.assertEqual(page.count("<tbody>"), 7)
            self.assertIn('scope="col"', page)
            self.assertNotIn("| --- |", page)

    def test_subtitles_are_rendered_as_emphasis(self) -> None:
        self.assertGreaterEqual(self.index.count("<em>"), 30)
        self.assertGreaterEqual(self.alternatives.count("<em>"), 30)


if __name__ == "__main__":
    unittest.main()
