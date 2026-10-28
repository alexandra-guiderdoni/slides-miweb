"""Cas négatifs du découpage ZIP et de la publication."""
import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]


def load(path):
    spec = importlib.util.spec_from_file_location("tested_build", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class DownloadContractTest(unittest.TestCase):
    def test_invalid_partitions_and_filenames_are_rejected(self):
        valid = [{"filename": "part-1.zip", "label": "Partie", "first": 1, "last": 1},
                 {"filename": "part-2.zip", "label": "Partie", "first": 2, "last": 2}]
        for slug in ("ecommerce-opquast-v5", "matrice-slide-ai"):
            build = load(ROOT / slug / "build.py")
            valid[0]["filename"] = f"{slug}-slides.zip"
            with self.subTest(slug=slug):
                self.assertEqual(2, len(build.download_parts({"download_parts": valid}, total=2)))
                for raw in ({}, "parts", [None], [valid[0]], [valid[1]],
                            [valid[0], dict(valid[1], first=1)],
                            [valid[0], dict(valid[1], filename=valid[0]["filename"])],
                            [valid[0], dict(valid[1], last=3)]):
                    with self.subTest(raw=raw), self.assertRaises(ValueError):
                        build.download_parts({"download_parts": raw}, total=2)
                for filename in ("../escape.zip", "a\\b.zip", "a?x.zip", "a#x.zip", ".zip", "/tmp/a.zip"):
                    with self.subTest(filename=filename), self.assertRaises(ValueError):
                        build.download_parts({"download_parts": [dict(valid[0], filename=filename, last=2)]}, total=2)
                for value in (False, "1", 0):
                    with self.subTest(first=value), self.assertRaises(ValueError):
                        build.download_parts({"download_parts": [dict(valid[0], first=value, last=2)]}, total=2)

    def test_failed_archive_preparation_preserves_existing_outputs(self):
        for slug in ("ecommerce-opquast-v5", "matrice-slide-ai"):
            build = load(ROOT / slug / "build.py")
            with tempfile.TemporaryDirectory() as directory, self.subTest(slug=slug):
                target = Path(directory)
                image = target / "slide.png"
                image.write_bytes(b"image")
                downloads = target / "assets" / "downloads"
                downloads.mkdir(parents=True)
                old_zip = downloads / build.ZIP_NAME
                old_zip.write_bytes(b"archive precedente")
                old_index = target / "index.html"
                old_index.write_text("page precedente")
                with patch.object(build, "ROOT", target), patch.object(build, "DOWNLOADS_DIR", downloads), \
                     patch.object(build, "VERSION_INFO", {}), patch.object(build, "ZIP_MAX_BYTES", 1), \
                     patch.object(build, "resolve_slide_image_path", return_value=image):
                    with self.assertRaises(ValueError):
                        build.write_zip([{"numero": 1, "image": "slide.png"}], "alternatives")
                self.assertEqual(old_zip.read_bytes(), b"archive precedente")
                self.assertEqual(old_index.read_text(), "page precedente")

    def test_markdown_bare_urls_preserve_query_parameters(self):
        for slug in ("matrice-slide-ai", "ecommerce-opquast-v5"):
            build = load(ROOT / slug / "build.py")
            with self.subTest(slug=slug):
                rendered = build.render_markdown_content("https://example.org/?a=1&b=2")
                self.assertIn('href="https://example.org/?a=1&amp;b=2"', rendered)
                self.assertNotIn("amp;amp", rendered)

    def test_identical_editorial_fields_are_rejected(self):
        for slug in ("matrice-slide-ai", "ecommerce-opquast-v5"):
            build = load(ROOT / slug / "build.py")
            slide = dict(build.load_slides()[0])
            slide["description"] = slide["transcription"]
            with self.subTest(slug=slug), self.assertRaisesRegex(ValueError, "distincts"):
                build.validate_slide_contract(slide, 1)

    def test_impossible_calendar_dates_are_rejected(self):
        publisher = load(ROOT / "matrice-slide-ai" / "publish_variant.py")
        for value in ("2026-02-29", "2026-04-31", "2026-13-01"):
            with self.subTest(value=value), self.assertRaises(ValueError):
                publisher.validate_catalog_date({"date_publication": value}, "date_publication")
        self.assertEqual("2024-02-29", publisher.validate_catalog_date({"date_publication": "2024-02-29"}, "date_publication"))
