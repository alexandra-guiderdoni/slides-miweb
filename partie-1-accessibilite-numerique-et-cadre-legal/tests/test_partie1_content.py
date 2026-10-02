from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class Partie1ContentTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.slides = json.loads((ROOT / "slides.json").read_text(encoding="utf-8"))
        cls.index = (ROOT / "index.html").read_text(encoding="utf-8")
        cls.alternatives = (ROOT / "alternatives.html").read_text(encoding="utf-8")
        cls.storyboard = (ROOT / "source" / "storyboard.md").read_text(
            encoding="utf-8"
        )

    def test_thirty_nine_slides_and_final_images_only(self) -> None:
        self.assertEqual([slide["numero"] for slide in self.slides], list(range(1, 40)))
        images = sorted((ROOT / "assets" / "slides").glob("slide-*.png"))
        self.assertEqual(len(images), 39)
        self.assertEqual(images[0].name, "slide-01.png")
        self.assertEqual(images[-1].name, "slide-39.png")

    def test_storyboard_transcriptions_and_notes_are_exact(self) -> None:
        headings = list(
            re.finditer(
                r"^## Slide (\d{2}) - (.+?)(?: - ÉTALON)?$",
                self.storyboard,
                re.MULTILINE,
            )
        )
        all_level_two_headings = list(
            re.finditer(r"^## .+$", self.storyboard, re.MULTILINE)
        )
        self.assertEqual(len(headings), 39)
        for slide, heading in zip(self.slides, headings, strict=True):
            end = next(
                (
                    candidate.start()
                    for candidate in all_level_two_headings
                    if candidate.start() > heading.start()
                ),
                len(self.storyboard),
            )
            section = self.storyboard[heading.end() : end]
            _, remainder = section.split("### Transcription exacte", 1)
            transcription, notes = remainder.split("### Discours oral exact", 1)
            self.assertEqual(slide["transcription"], transcription.strip())
            self.assertEqual(slide["notes_orateur"], notes.strip())

    def test_two_accordions_per_slide(self) -> None:
        self.assertEqual(
            len(re.findall(r"<button[^>]+data-alternative-button", self.index)), 39
        )
        self.assertEqual(self.index.count("Lire le discours oral de la slide"), 39)

    def test_markdown_tables_are_semantic(self) -> None:
        markdown_tables = sum(
            len(
                re.findall(
                    r"^\|.+\|\n\|(?:\s*:?-{3,}:?\s*\|)+$",
                    slide["transcription"],
                    re.MULTILINE,
                )
            )
            for slide in self.slides
        )
        expected_tables = markdown_tables - 1
        self.assertGreater(expected_tables, 0)
        for page in (self.index, self.alternatives):
            self.assertEqual(page.count("<table>"), expected_tables)
            self.assertEqual(page.count("<caption>"), expected_tables)
            self.assertEqual(page.count("<thead>"), expected_tables)
            self.assertEqual(page.count("<tbody>"), expected_tables)
            self.assertIn('scope="col"', page)
            self.assertNotIn("| --- |", page)

    def test_solution_tables_have_specific_captions(self) -> None:
        captions = (
            "Aveugle et Malvoyant",
            "Sourd et Malentendant",
            "Handicap moteur et Dyslexie / troubles dys",
            "Handicap mental et TSA",
        )
        for caption in captions:
            for page in (self.index, self.alternatives):
                self.assertIn(f"<caption>{caption}</caption>", page)

    def test_rgaa_themes_are_an_ordered_list(self) -> None:
        themes = (
            "Images",
            "Cadres",
            "Couleurs",
            "Multimédia",
            "Tableaux",
            "Liens",
            "Scripts",
            "Éléments obligatoires",
            "Structuration",
            "Présentation",
            "Formulaires",
            "Navigation",
            "Consultation",
        )
        for page, heading_level in ((self.index, 6), (self.alternatives, 5)):
            self.assertIn(
                f"<h{heading_level}>Les 13 thèmes du RGAA</h{heading_level}><ol>",
                page,
            )
            positions = []
            for number, theme in enumerate(themes, start=1):
                marker = f'<li value="{number}">{theme}</li>'
                self.assertIn(marker, page)
                positions.append(page.index(marker))
            self.assertEqual(positions, sorted(positions))

    def test_source_links_are_preserved(self) -> None:
        for url in (
            "https://atalan.fr/agissons/fr/index.html",
            "https://obligations-legales-accessibilite-numerique.fr/fr/",
        ):
            self.assertIn(f'href="{url}"', self.index)
            self.assertIn(f'href="{url}"', self.alternatives)

    def test_subtitles_are_rendered_as_emphasis(self) -> None:
        self.assertGreaterEqual(self.index.count("<em>"), 30)
        self.assertGreaterEqual(self.alternatives.count("<em>"), 30)


if __name__ == "__main__":
    unittest.main()
