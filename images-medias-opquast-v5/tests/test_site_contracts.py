from __future__ import annotations

import html
import importlib.util
import re
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUILD_PATH = ROOT / "build.py"


class ImageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.images: list[dict[str, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag == "img":
            self.images.append({key: value or "" for key, value in attrs})


def load_build_module():
    spec = importlib.util.spec_from_file_location("miweb_build", BUILD_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Impossible de charger build.py.")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class SiteContractsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.build = load_build_module()
        cls.slides = cls.build.load_slides()
        cls.index_html = cls.build.render_v1_index(cls.slides)
        cls.alternatives_html = cls.build.render_alternatives(cls.slides)
        cls.accessibilite_html = cls.build.render_accessibility()
        cls.alternatives_md = cls.build.render_markdown(cls.slides)
        cls.readme = cls.build.render_readme()

    def test_slides_json_matches_images(self):
        slide_paths = sorted((ROOT / "assets" / "slides").glob("slide-*.png"))
        if slide_paths:
            self.assertEqual(
                len(slide_paths),
                len(self.slides),
                msg="slides.json doit contenir une entrée par image slide-*.png.",
            )
        requires_local_images = (ROOT / "slides.json").is_file()
        for slide in self.slides:
            self.assertIsInstance(slide["numero"], int)
            for field_name in (
                "titre",
                "image",
                "alt",
                "description",
                "message",
                "transcription",
                "notes_orateur",
            ):
                with self.subTest(field=field_name, slide=slide["numero"]):
                    self.assertIsInstance(slide[field_name], str)
                    self.assertTrue(slide[field_name].strip())
            self.assertIsInstance(slide["textes_visibles"], list)
            self.assertTrue(slide["textes_visibles"])
            for text in slide["textes_visibles"]:
                self.assertIsInstance(text, str)
                self.assertTrue(text.strip())
            image_path = ROOT / slide["image"]
            if requires_local_images:
                self.assertTrue(image_path.is_file(), image_path)
                self.assertGreater(image_path.stat().st_size, 1000)
            self.assertLessEqual(len(slide["alt"]), 80)
            self.assertTrue(slide["description"])
            self.assertTrue(slide["textes_visibles"])
            self.assertTrue(slide["message"])

    def test_download_zip_matches_current_slides(self):
        import zipfile

        zip_path = ROOT / "assets" / "downloads" / f"{ROOT.name}-slides.zip"
        if not zip_path.is_file():
            self.skipTest("ZIP non généré.")
        slide_paths = sorted((ROOT / "assets" / "slides").glob("slide-*.png"))
        with zipfile.ZipFile(zip_path) as archive:
            for slide_path in slide_paths:
                with self.subTest(slide=slide_path.name):
                    self.assertEqual(
                        slide_path.read_bytes(),
                        archive.read(slide_path.name),
                        msg=(
                            "Le ZIP doit être régénéré après optimisation "
                            f"ou remplacement de {slide_path.name}."
                        ),
                    )

    def test_variant_pages_expose_transcriptions(self):
        self.assertIn("Alternatives textuelles", self.index_html)
        self.assertIn("Message à retenir", self.index_html)
        self.assertIn("Alternatives textuelles", self.alternatives_html)
        self.assertIn("Message à retenir", self.alternatives_html)
        self.assertIn("# Alternatives textuelles", self.alternatives_md)
        self.assertIn("### Transcription", self.alternatives_md)
        self.assertIn("### Discours oral", self.alternatives_md)
        for slide in self.slides:
            escaped_title = html.escape(slide["titre"], quote=True)
            self.assertIn(escaped_title, self.index_html)
            self.assertIn(escaped_title, self.alternatives_html)
            self.assertTrue(slide["transcription"].strip())
            self.assertTrue(slide["notes_orateur"].strip())

    def test_readme_source_entries_match_existing_files(self):
        source_refs = re.findall(r"`source/([^`]+)`", self.readme)
        self.assertTrue(
            source_refs, "Le README doit lister les fichiers source traçables."
        )
        for source_name in source_refs:
            with self.subTest(source=source_name):
                self.assertTrue((ROOT / "source" / source_name).is_file())

    def test_slideshow_keeps_projection_and_all_slides_controls(self):
        self.assertIn(self.build.DIAPORAMA_TITLE, self.index_html)
        self.assertIn("data-slide-previous", self.index_html)
        self.assertIn("data-slide-next", self.index_html)
        self.assertIn("data-slide-fullscreen", self.index_html)
        self.assertIn("data-slide-all", self.index_html)
        self.assertIn("data-projection-controls", self.index_html)
        self.assertIn("requestFullscreen", self.index_html)
        self.assertIn("exitFullscreen", self.index_html)
        self.assertIn('addEventListener("touchstart"', self.index_html)
        self.assertIn('addEventListener("touchend"', self.index_html)
        self.assertIn("swipeMinDistance", self.index_html)
        self.assertIn("const swipeDirectionRatio = 1.4;", self.index_html)
        self.assertIn("function isInteractiveSwipeTarget(target)", self.index_html)
        self.assertIn(
            """target.closest("a, button, input, textarea, select, summary, [role='button'], .fr-accordion")""",
            self.index_html,
        )
        self.assertIn("!isInteractiveSwipeTarget(event.target)", self.index_html)
        self.assertIn("?projection=1#slide-01", self.index_html)
        self.assertIn("?slides=all#diaporama", self.index_html)
        self.assertIn("if (isAllSlidesRequested()) {", self.index_html)
        self.assertIn("showAllSlides();", self.index_html)
        self.assertIn('window.addEventListener("popstate"', self.index_html)

    def test_single_slide_url_removes_all_slides_query(self):
        self.assertIn("function slideUrl(index)", self.index_html)
        self.assertIn('params.delete("slides");', self.index_html)
        self.assertIn("const query = params.toString();", self.index_html)
        self.assertIn(
            'return `${window.location.pathname}${query ? `?${query}` : ""}${hash}`;',
            self.index_html,
        )
        self.assertIn("const url = slideUrl(index);", self.index_html)
        self.assertIn(
            "if (window.location.hash === hash && !hasSlidesQuery()) return;",
            self.index_html,
        )
        self.assertNotIn(
            "const url = `${window.location.pathname}${window.location.search}${hash}`;",
            self.index_html,
        )

    def test_images_have_alt_and_stable_dimensions(self):
        parser = ImageParser()
        parser.feed(self.index_html)
        slide_images = [
            image
            for image in parser.images
            if image.get("src", "").startswith("assets/slides/")
        ]
        self.assertEqual(len(self.slides), len(slide_images))
        self.assertEqual(
            {("1672", "941")},
            {(image.get("width"), image.get("height")) for image in slide_images},
        )
        for image in slide_images:
            self.assertTrue(image.get("alt"))
        self.assertEqual(
            ["eager"] + ["lazy"] * (len(slide_images) - 1),
            [image.get("loading") for image in slide_images],
        )
        self.assertTrue(all(image.get("decoding") == "async" for image in slide_images))

    def test_each_slide_has_transcription_and_oral_accordions(self):
        button_pattern = re.compile(
            r"<button(?P<attributes>[^>]*)>(?P<label>.*?)</button>", re.DOTALL
        )
        rendered_buttons = []
        for match in button_pattern.finditer(self.index_html):
            attributes = match.group("attributes")
            if 'class="fr-accordion__btn"' not in attributes:
                continue
            target = re.search(r'aria-controls="([^"]+)"', attributes)
            self.assertIsNotNone(target)
            label = html.unescape(re.sub(r"<[^>]+>", "", match.group("label"))).strip()
            rendered_buttons.append((label, target.group(1)))

        expected_labels = {
            f"Lire la transcription de la slide {slide['numero']} - {slide['titre']}"
            for slide in self.slides
        } | {
            f"Lire le discours oral de la slide {slide['numero']} - {slide['titre']}"
            for slide in self.slides
        }
        self.assertEqual(2 * len(self.slides), len(rendered_buttons))
        self.assertEqual(expected_labels, {label for label, _ in rendered_buttons})

        document_ids = set(re.findall(r'\bid="([^"]+)"', self.index_html))
        controlled_ids = [target for _, target in rendered_buttons]
        self.assertEqual(len(controlled_ids), len(set(controlled_ids)))
        for target in controlled_ids:
            with self.subTest(target=target):
                self.assertIn(target, document_ids)

    def test_each_accordion_contains_its_assigned_wording(self):
        for slide in self.slides:
            sid = self.build.slide_id(slide)
            rendered_slide = self.build.render_slide(slide, len(self.slides))
            transcription_match = re.search(
                rf'<div id="alternative-{sid}" class="fr-collapse">(.*?)</div>',
                rendered_slide,
                re.DOTALL,
            )
            oral_match = re.search(
                rf'<div id="discours-{sid}" class="fr-collapse">(.*?)</div>',
                rendered_slide,
                re.DOTALL,
            )
            self.assertIsNotNone(transcription_match, sid)
            self.assertIsNotNone(oral_match, sid)
            self.assertNotRegex(slide["notes_orateur"], r"(?m)^---\s*$")
            self.assertEqual(
                self.build.render_transcription(slide).strip(),
                transcription_match.group(1).strip(),
                sid,
            )
            self.assertEqual(
                self.build.render_discours(slide).strip(),
                oral_match.group(1).strip(),
                sid,
            )
            self.assertIn(
                self.build.shift_markdown_headings(slide["transcription"], 1),
                self.alternatives_md,
            )
            self.assertIn(
                self.build.shift_markdown_headings(slide["notes_orateur"], 1),
                self.alternatives_md,
            )
        self.assertIn(
            '<pre><code class="language-html">alt=&quot;&quot;</code></pre>',
            self.index_html,
        )
        self.assertIn("<h5>Impact utilisateur</h5>", self.index_html)
        self.assertIn("<h5>Mémo</h5>", self.index_html)

    def test_security_and_assets_contracts(self):
        self.assertIn('http-equiv="Content-Security-Policy"', self.index_html)
        self.assertNotIn("nonce=", self.index_html)
        self.assertIn(self.build.csp_hash(self.build.MAIN_JS), self.index_html)
        self.assertIn(self.build.csp_hash(self.build.CUSTOM_CSS), self.index_html)
        self.assertNotIn("unsafe-inline", self.index_html)
        self.assertNotIn('href="#"', self.index_html)
        self.assertNotIn('href="#"', self.alternatives_html)
        favicon_path = ROOT / "assets" / "favicons" / "favicon.ico"
        self.assertTrue(favicon_path.is_file())
        self.assertEqual(b"\x00\x00\x01\x00", favicon_path.read_bytes()[:4])

    def test_oral_discourse_and_secure_links_render_in_all_exports(self):
        slide = dict(
            self.slides[0],
            notes_orateur=(
                "Présenter l’**exigence** et consulter "
                "[la source officielle](https://example.org/source).\n\n"
                "Complément : https://example.org/guide."
            ),
        )
        index = self.build.render_v1_index([slide])
        alternatives = self.build.render_alternatives([slide])
        markdown = self.build.render_markdown([slide])

        for output in (index, alternatives):
            self.assertIn("discours oral", output.lower())
            self.assertIn("<strong>exigence</strong>", output)
            self.assertIn(
                '<a href="https://example.org/source">la source officielle</a>',
                output,
            )
            self.assertIn(
                '<a href="https://example.org/guide">https://example.org/guide</a>.',
                output,
            )
        self.assertIn("### Discours oral", markdown)
        self.assertIn("Présenter l’**exigence**", markdown)
        self.assertIn("[la source officielle](https://example.org/source)", markdown)


if __name__ == "__main__":
    unittest.main()
