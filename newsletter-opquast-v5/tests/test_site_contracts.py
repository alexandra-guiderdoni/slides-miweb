from __future__ import annotations

import hashlib
import html
import importlib.util
import json
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
        slide_paths = sorted((ROOT / "assets" / "slides").glob("slide-*.jpg"))
        self.assertEqual(18, len(self.slides))
        self.assertEqual(
            len(slide_paths),
            len(self.slides),
            msg="slides.json doit contenir une entrée par image slide-*.jpg.",
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
            self.assertIsInstance(slide["transcription"], list)
            self.assertTrue(slide["transcription"])
            self.assertTrue(slide["notes_orateur"].strip())
            self.assertEqual(".jpg", Path(slide["image"]).suffix)

    def test_download_zip_matches_current_slides(self):
        import zipfile

        zip_path = ROOT / "assets" / "downloads" / f"{ROOT.name}-slides.zip"
        if not zip_path.is_file():
            self.skipTest("ZIP non généré.")
        slide_paths = sorted((ROOT / "assets" / "slides").glob("slide-*.jpg"))
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
        self.assertIn("Lire la transcription de la slide", self.index_html)
        self.assertIn("Message à retenir", self.index_html)
        self.assertIn("Alternatives textuelles", self.alternatives_html)
        self.assertIn("Lecture du visuel", self.alternatives_html)
        self.assertIn("Message à retenir", self.alternatives_html)
        self.assertIn("Lire le discours oral de la slide", self.index_html)
        self.assertIn("Discours oral", self.alternatives_html)
        self.assertIn("# Alternatives textuelles", self.alternatives_md)
        for slide in self.slides:
            escaped_title = html.escape(slide["titre"], quote=True)
            escaped_description = html.escape(slide["description"], quote=True)
            self.assertIn(escaped_title, self.index_html)
            self.assertIn(escaped_title, self.alternatives_html)
            self.assertIn(escaped_description, self.alternatives_html)
            self.assertIn(slide["message"], self.alternatives_md)
            first_oral_paragraph = slide["notes_orateur"].split("\n\n", 1)[0]
            self.assertIn(
                html.escape(first_oral_paragraph, quote=True), self.index_html
            )
            self.assertIn(first_oral_paragraph, self.alternatives_html)
            self.assertIn(first_oral_paragraph, self.alternatives_md)

    def test_vptcs_oral_uses_semantic_list_and_emphasis(self):
        slide = next(slide for slide in self.slides if slide["numero"] == 14)
        oral_html = self.build.render_discours(slide)

        ordered_lists = re.findall(r"<ol>(.*?)</ol>", oral_html, re.DOTALL)
        self.assertEqual(1, len(ordered_lists))
        self.assertEqual(5, ordered_lists[0].count("<li>"))
        responsibility_lists = re.findall(r"<ul>(.*?)</ul>", oral_html, re.DOTALL)
        self.assertEqual(1, len(responsibility_lists))
        self.assertEqual(3, responsibility_lists[0].count("<li>"))
        self.assertIn("<strong>Une responsabilité distribuée</strong>", oral_html)
        for role in ("Rédaction", "Développement", "Conformité"):
            self.assertIn(f"<strong>{role}</strong>", responsibility_lists[0])
        pillars = ("Visibilité", "Perception", "Technique", "Contenus", "Services")
        for pillar in pillars:
            self.assertIn(f"<strong>{pillar}</strong>", oral_html)

    def test_jpeg_assets_match_provenance(self):
        provenance = json.loads(
            (ROOT / "source" / "provenance.json").read_text(encoding="utf-8")
        )
        self.assertEqual("JPEG", provenance["conversion"]["format"])
        self.assertEqual(len(self.slides), len(provenance["slides"]))
        for slide, record in zip(self.slides, provenance["slides"], strict=True):
            self.assertEqual(slide["image"], record["published"])
            image_path = ROOT / slide["image"]
            self.assertEqual(".jpg", image_path.suffix)
            self.assertFalse(image_path.with_suffix(".png").exists())
            self.assertTrue(image_path.read_bytes().startswith(b"\xff\xd8\xff"))
            self.assertEqual(
                hashlib.sha256(image_path.read_bytes()).hexdigest(),
                record["published_sha256"],
            )

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
        self.assertIn("?projection=1#slide-01", self.index_html)
        self.assertIn("?slides=all#diaporama", self.index_html)

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

    def test_security_and_assets_contracts(self):
        self.assertIn('http-equiv="Content-Security-Policy"', self.index_html)
        self.assertIn("nonce-miweb-static", self.index_html)
        self.assertNotIn("unsafe-inline", self.index_html)
        self.assertNotIn('href="#"', self.index_html)
        self.assertNotIn('href="#"', self.alternatives_html)
        favicon_path = ROOT / "assets" / "favicons" / "favicon.ico"
        self.assertTrue(favicon_path.is_file())
        self.assertEqual(b"\x00\x00\x01\x00", favicon_path.read_bytes()[:4])


if __name__ == "__main__":
    unittest.main()
