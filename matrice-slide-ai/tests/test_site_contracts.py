from __future__ import annotations

import html
import json
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

        primary = ROOT / "assets/downloads" / f"{ROOT.name}-slides.zip"
        if not primary.is_file():
            self.skipTest("ZIP non généré.")
        metadata_path = ROOT / "variant.json"
        metadata = json.loads(metadata_path.read_text()) if metadata_path.is_file() else {}
        parts = metadata.get("download_parts") or [{"filename": primary.name, "first": 1, "last": len(self.slides)}]
        seen = []
        for part in parts:
            path = ROOT / "assets/downloads" / part["filename"]
            self.assertTrue(path.is_file(), path)
            self.assertLess(path.stat().st_size, 100 * 1024 * 1024)
            expected = {Path(slide["image"]).name: ROOT / slide["image"] for slide in self.slides
                        if part["first"] <= slide["numero"] <= part["last"]}
            with zipfile.ZipFile(path) as archive:
                names = [name for name in archive.namelist() if name != "alternatives.md"]
                self.assertEqual(sorted(names), sorted(expected))
                seen.extend(names)
                self.assertEqual(archive.read("alternatives.md"), (ROOT / "alternatives.md").read_bytes())
                for name, source in expected.items():
                    with self.subTest(slide=name):
                        self.assertEqual(archive.read(name), source.read_bytes())
            for page in (self.index_html, self.alternatives_html, (ROOT / "accessibilite.html").read_text()):
                self.assertIn(f'assets/downloads/{part["filename"]}', page)
        self.assertEqual(sorted(seen), sorted(Path(slide["image"]).name for slide in self.slides))
        self.assertEqual(len(seen), len(set(seen)))

    def test_alternative_pages_keep_transcriptions(self):
        self.assertIn("Alternatives textuelles", self.index_html)
        self.assertIn("Alternatives textuelles", self.alternatives_html)
        self.assertIn("Message à retenir", self.alternatives_html)
        self.assertIn("# Alternatives textuelles", self.alternatives_md)
        self.assertIn("### Transcription", self.alternatives_md)
        self.assertIn("### Description détaillée du visuel", self.alternatives_md)
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
                path = ROOT / "source" / source_name
                self.assertTrue(path.is_dir() if source_name.endswith("/") else path.is_file())

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

    def test_each_slide_has_an_accessible_local_accordion_command(self):
        command_pattern = re.compile(
            r"<button(?P<attributes>[^>]*) data-slide-accordions-toggle(?P<suffix>[^>]*)>"
            r"(?P<label>.*?)</button>\s*"
            r'<div class="fr-accordions-group" data-fr-group="false">',
            re.DOTALL,
        )
        commands = list(command_pattern.finditer(self.index_html))

        self.assertEqual(len(self.slides), len(commands))
        rendered_ids = re.findall(r'\bid="([^"]+)"', self.index_html)
        document_ids = set(rendered_ids)
        self.assertEqual(len(rendered_ids), len(document_ids))
        for slide, command in zip(self.slides, commands, strict=True):
            attributes = command.group("attributes") + command.group("suffix")
            sid = self.build.slide_id(slide)
            controls = re.search(r'aria-controls="([^"]+)"', attributes)

            with self.subTest(slide=slide["numero"]):
                self.assertIn('type="button"', attributes)
                self.assertIn(
                    'class="fr-btn fr-btn--secondary fr-mb-2w"',
                    attributes,
                )
                self.assertIn(f'data-slide-number="{slide["numero"]}"', attributes)
                self.assertNotIn("fr-accordion__btn", attributes)
                self.assertIn('aria-expanded="false"', attributes)
                self.assertIsNotNone(controls)
                self.assertEqual(
                    [f"description-{sid}", f"discours-{sid}"],
                    controls.group(1).split(),
                )
                self.assertTrue(set(controls.group(1).split()) <= document_ids)
                self.assertIn(">Ouvrir les accordéons<", command.group("label"))
                self.assertIn(
                    "data-slide-accordions-context",
                    command.group("label"),
                )
                self.assertIn(
                    f", description et discours oral de la slide {slide['numero']}",
                    command.group("label"),
                )

    def test_accordion_commands_follow_the_slideshow_and_dsfr_lifecycle(self):
        script = self.build.MAIN_JS

        self.assertIn(
            'open ? "Fermer les accordéons" : "Ouvrir les accordéons"',
            script,
        )
        self.assertIn(
            'allMode ? ", description et discours oral de toutes les slides"',
            script,
        )
        self.assertIn(
            ': `, description et discours oral de la slide ${slideNumber}`',
            script,
        )
        self.assertIn("let persistentAccordionsOpen = false;", script)
        self.assertIn("let accordionInitializationReady = false;", script)
        self.assertNotIn("pendingAccordionStates", script)
        self.assertNotRegex(script, r"localStorage|sessionStorage|document\.cookie")
        self.assertIn(
            "const proxy = window.dsfr && window.dsfr(panel);",
            script,
        )
        self.assertIn("const collapse = proxy && proxy.collapse;", script)
        self.assertIn('panel.addEventListener("dsfr.disclose"', script)
        self.assertIn('panel.addEventListener("dsfr.conceal"', script)
        self.assertIn("requestAnimationFrame", script)
        self.assertNotIn(".click()", script)

        group_command = re.search(
            r"function setAccordionCommandOpen\(command, open\) \{(?P<body>.*?)\n  \}",
            script,
            re.DOTALL,
        )
        self.assertIsNotNone(group_command)
        self.assertNotIn(
            "renderAccordionCommandState",
            group_command.group("body"),
        )

        show_slide = re.search(
            r"function showSlide\(index, options = \{\}\) \{(?P<body>.*?)\n  \}",
            script,
            re.DOTALL,
        )
        show_all = re.search(
            r"function showAllSlides\(\) \{(?P<body>.*?)\n  \}",
            script,
            re.DOTALL,
        )
        self.assertIsNotNone(show_slide)
        self.assertIsNotNone(show_all)
        self.assertLess(
            show_slide.group("body").index("applyVisibility();"),
            show_slide.group("body").index("applyPersistentAccordionState"),
        )
        self.assertIn(
            'renderAccordionCommandContext(slides[currentIndex].querySelector("[data-slide-accordions-toggle]"));',
            show_slide.group("body"),
        )
        self.assertNotIn("persistentAccordionsOpen = false;", show_all.group("body"))
        self.assertIn(
            "accordionCommands.forEach(renderAccordionCommandContext);",
            show_all.group("body"),
        )
        self.assertIn(
            "setAllAccordionCommandsOpen(persistentAccordionsOpen);",
            show_all.group("body"),
        )

        global_command = re.search(
            r"function setAllAccordionCommandsOpen\(open\) \{(?P<body>.*?)\n  \}",
            script,
            re.DOTALL,
        )
        self.assertIsNotNone(global_command)
        self.assertIn(
            "accordionCommands.forEach((command) => setAccordionCommandOpen(command, open));",
            global_command.group("body"),
        )

        command_click = re.search(
            r"accordionCommands\.forEach\(\(command\) => \{(?P<body>.*?)\n  \}\);",
            script,
            re.DOTALL,
        )
        self.assertIsNotNone(command_click)
        self.assertIn("persistentAccordionsOpen = open;", command_click.group("body"))
        self.assertIn(
            "if (allMode) setAllAccordionCommandsOpen(open);",
            command_click.group("body"),
        )

    def test_each_slide_has_description_and_oral_accordions(self):
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
            f"Lire la description détaillée de la slide {slide['numero']} - {slide['titre']}"
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
            description_match = re.search(
                rf'<div id="description-{sid}" class="fr-collapse">(.*?)</div>',
                rendered_slide,
                re.DOTALL,
            )
            oral_match = re.search(
                rf'<div id="discours-{sid}" class="fr-collapse">(.*?)</div>',
                rendered_slide,
                re.DOTALL,
            )
            self.assertIsNotNone(description_match, sid)
            self.assertIsNotNone(oral_match, sid)
            self.assertNotIn(f'id="alternative-{sid}"', rendered_slide)
            self.assertNotRegex(slide["notes_orateur"], r"(?m)^---\s*$")
            self.assertIn(
                f"<p>{html.escape(slide['description'], quote=True)}</p>",
                description_match.group(1),
                sid,
            )
            for text in slide["textes_visibles"]:
                self.assertIn(html.escape(text, quote=True), description_match.group(1), sid)
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
        for slide in self.slides:
            rendu = (
                f"<p>{html.escape(slide['description'], quote=True)}</p>"
                + self.build.render_discours(slide)
            )
            sous_titres = len(re.findall(r"(?m)^###\s+", slide["notes_orateur"]))
            self.assertEqual(sous_titres, rendu.count("<h5>"), slide["numero"])

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

    def slide_with_rules(self, regles, sources):
        return dict(self.slides[0], regles=regles, sources=sources)

    def test_opquast_sources_are_published_in_every_export(self):
        url = "https://checklists.opquast.com/fr/qualite-numerique/69"
        slide = self.slide_with_rules([69], [url])
        index = self.build.render_v1_index([slide])
        alternatives = self.build.render_alternatives([slide])
        markdown = self.build.render_markdown([slide])
        for output in (index, alternatives):
            self.assertIn(f'<a href="{url}">Règle Opquast 69</a>', output)
        self.assertIn(f"[Règle Opquast 69]({url})", markdown)
        sans_regle = self.build.render_slide(self.slide_with_rules([], []), 1)
        self.assertNotIn("Règles Opquast de la slide", sans_regle)

    def test_rules_and_sources_must_match(self):
        valide = self.slide_with_rules(
            [69, 70],
            [
                "https://checklists.opquast.com/fr/qualite-numerique/69",
                "https://checklists.opquast.com/fr/qualite-numerique/70",
            ],
        )
        self.build.validate_slide_contract(valide, valide["numero"])
        invalides = [
            ([69, 70], ["https://checklists.opquast.com/fr/qualite-numerique/69"]),
            ([69], ["https://checklists.opquast.com/fr/qualite-numerique/70"]),
            ([69], ["https://exemple.org/69"]),
            (["69"], ["https://checklists.opquast.com/fr/qualite-numerique/69"]),
            ("69", []),
            (
                [69, 69],
                [
                    "https://checklists.opquast.com/fr/qualite-numerique/69",
                    "https://checklists.opquast.com/fr/qualite-numerique/69",
                ],
            ),
        ]
        for regles, sources in invalides:
            with self.subTest(regles=regles, sources=sources), self.assertRaises(ValueError):
                self.build.validate_slide_contract(
                    self.slide_with_rules(regles, sources), self.slides[0]["numero"]
                )

    def test_bare_url_does_not_swallow_closing_parenthesis(self):
        rendered = self.build.render_markdown_content("Voir (https://exemple.org/69).")
        self.assertIn(
            '<a href="https://exemple.org/69">https://exemple.org/69</a>).', rendered
        )
        wiki = self.build.render_markdown_content("Voir https://exemple.org/a_(b) ici.")
        self.assertIn('<a href="https://exemple.org/a_(b)">', wiki)

    def test_download_links_state_format_and_size(self):
        label = self.build.download_label(
            {"filename": "absent.zip", "label": "Télécharger les slides"}, ROOT
        )
        self.assertEqual("Télécharger les slides (ZIP)", label)
        import tempfile

        with tempfile.TemporaryDirectory() as temporary:
            downloads = Path(temporary) / "assets" / "downloads"
            downloads.mkdir(parents=True)
            (downloads / "jeu.zip").write_bytes(b"0" * (3 * 1024 * 1024))
            sized = self.build.download_label(
                {"filename": "jeu.zip", "label": "Télécharger les slides"},
                Path(temporary),
            )
            self.assertEqual("Télécharger les slides (ZIP, 3 Mo)", sized)
            explicit = self.build.download_label(
                {"filename": "jeu.zip", "label": "Slides 1 à 66 (ZIP)"}, Path(temporary)
            )
            self.assertEqual("Slides 1 à 66 (ZIP, 3 Mo)", explicit)
        self.assertNotIn(">Télécharger les slides</a>", self.index_html)

    def test_two_slides_cannot_share_one_image(self):
        import tempfile
        from unittest import mock

        slides = json.loads(json.dumps(self.slides[:2]))
        slides[1]["image"] = slides[0]["image"]
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "slides.json"
            path.write_text(json.dumps(slides, ensure_ascii=False), encoding="utf-8")
            with mock.patch.object(self.build, "SLIDES_PATH", Path(temporary) / "absent.json"), \
                    mock.patch.object(self.build, "SLIDES_EXAMPLE_PATH", path):
                with self.assertRaisesRegex(ValueError, "déjà utilisée"):
                    self.build.load_slides()

    def test_two_slides_cannot_share_one_archive_name(self):
        import tempfile
        from unittest import mock

        slides = json.loads(json.dumps(self.slides[:2]))
        first = slides[0]["image"]
        folder, name = first.rsplit("/", 1)
        slides[1]["image"] = f"{folder}/./{name}"
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "slides.json"
            path.write_text(json.dumps(slides, ensure_ascii=False), encoding="utf-8")
            with mock.patch.object(self.build, "SLIDES_PATH", Path(temporary) / "absent.json"), \
                    mock.patch.object(self.build, "SLIDES_EXAMPLE_PATH", path):
                with self.assertRaisesRegex(ValueError, "déjà utilisée"):
                    self.build.load_slides()

    def test_failed_atomic_write_leaves_no_temporary_file(self):
        import tempfile
        from unittest import mock

        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "page.html"
            with mock.patch.object(self.build.os, "replace", side_effect=OSError("disque plein")):
                with self.assertRaises(OSError):
                    self.build.write_text_atomic(target, "contenu")
            self.assertEqual([], [p.name for p in Path(temporary).iterdir()])

    def test_stale_archives_are_removed(self):
        import tempfile

        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary)
            for name in ("jeu-slides.zip", "jeu-slides-partie-2.zip", "autre.zip"):
                (directory / name).write_bytes(b"x")
            removed = self.build.remove_stale_archives(
                directory, "jeu", {"jeu-slides.zip"}
            )
            self.assertEqual(["jeu-slides-partie-2.zip"], removed)
            self.assertEqual(
                ["autre.zip", "jeu-slides.zip"],
                sorted(p.name for p in directory.iterdir()),
            )

    def test_variant_metadata_values_must_be_non_empty_strings(self):
        import tempfile

        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "variant.json"
            for value in (None, 3, "  "):
                with self.subTest(value=value):
                    path.write_text(json.dumps({"site_title": value}), encoding="utf-8")
                    with self.assertRaises(ValueError):
                        self.build.load_version_info(path)
            path.write_text(json.dumps({"site_title": "Titre"}), encoding="utf-8")
            self.assertEqual("Titre", self.build.load_version_info(path)["site_title"])

    def test_cli_reports_malformed_data_without_traceback(self):
        original = self.build.main
        try:
            for error in (TypeError("slide non objet"), KeyError("download_parts")):
                with self.subTest(error=type(error).__name__):

                    def failing(error=error):
                        raise error

                    self.build.main = failing
                    with self.assertRaises(SystemExit) as raised:
                        self.build.cli()
                    self.assertTrue(str(raised.exception.code).startswith("Erreur : "))
        finally:
            self.build.main = original

    def test_readme_cites_every_source_file(self):
        source_dir = ROOT / "source"
        if not source_dir.is_dir():
            self.skipTest("Aucun dossier source.")
        cited = re.findall(r"`source/([^`]+)`", self.readme)
        for path in sorted(p for p in source_dir.rglob("*") if p.is_file()):
            relative = path.relative_to(source_dir).as_posix()
            with self.subTest(source=relative):
                self.assertTrue(
                    any(
                        relative == ref or relative.startswith(ref)
                        for ref in cited
                        if ref
                    ),
                    relative,
                )

    def test_visible_texts_are_kept_in_the_transcription(self):
        for slide in self.slides:
            transcription = re.sub(r"\s+", " ", slide["transcription"])
            for text in slide["textes_visibles"]:
                with self.subTest(slide=slide["numero"], text=text):
                    self.assertIn(re.sub(r"\s+", " ", text).strip(), transcription)

    def test_committed_pages_match_the_generator(self):
        if not (ROOT / "slides.json").is_file():
            self.skipTest("Gabarit sans jeu publié.")
        rendered = {
            "index.html": self.index_html,
            "alternatives.html": self.alternatives_html,
            "accessibilite.html": self.accessibilite_html,
            "alternatives.md": self.alternatives_md,
            "README.md": self.readme,
        }
        for name, content in rendered.items():
            with self.subTest(page=name):
                self.assertEqual(
                    content,
                    (ROOT / name).read_text(encoding="utf-8"),
                    f"{name} n’est pas à jour : relancer python3 build.py.",
                )


if __name__ == "__main__":
    unittest.main()
