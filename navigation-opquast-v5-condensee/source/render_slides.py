#!/usr/bin/env python3
"""Compose les slides finales à partir des illustrations ImageGen et des textes contrôlés."""

from __future__ import annotations

import json
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "source"
ILLUSTRATIONS = SOURCE / "illustrations"
LAYOUTS = SOURCE / "slide-layouts.json"
OUTPUT = ROOT / "assets" / "slides"

WIDTH = 1672
HEIGHT = 941

FONT_REGULAR = Path("/System/Library/Fonts/Supplemental/Arial.ttf")
FONT_BOLD = Path("/System/Library/Fonts/Supplemental/Arial Bold.ttf")

NAVY = "#161B4B"
TEXT = "#242424"
MUTED = "#666666"
WHITE = "#FFFFFF"
LIGHT_BORDER = "#D7D9E2"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT_BOLD if bold else FONT_REGULAR), size)


def wrap_text(draw: ImageDraw.ImageDraw, value: str, chosen_font: ImageFont.FreeTypeFont, max_width: int) -> str:
    lines: list[str] = []
    for paragraph in value.split("\n"):
        words = paragraph.split()
        if not words:
            lines.append("")
            continue
        current = words[0]
        for word in words[1:]:
            candidate = f"{current} {word}"
            if draw.textlength(candidate, font=chosen_font) <= max_width:
                current = candidate
            else:
                lines.append(current)
                current = word
        lines.append(current)
    return "\n".join(lines)


def trim_white(image: Image.Image) -> Image.Image:
    rgb = image.convert("RGB")
    background = Image.new("RGB", rgb.size, "white")
    difference = ImageChops.difference(rgb, background).convert("L")
    mask = difference.point(lambda pixel: 255 if pixel > 18 else 0)
    box = mask.getbbox()
    if not box:
        return rgb
    left, top, right, bottom = box
    padding = 28
    return rgb.crop(
        (
            max(0, left - padding),
            max(0, top - padding),
            min(rgb.width, right + padding),
            min(rgb.height, bottom + padding),
        )
    )


def paste_contained(canvas: Image.Image, image: Image.Image, box: tuple[int, int, int, int]) -> None:
    x1, y1, x2, y2 = box
    fitted = ImageOps.contain(image, (x2 - x1, y2 - y1), Image.Resampling.LANCZOS)
    x = x1 + (x2 - x1 - fitted.width) // 2
    y = y1 + (y2 - y1 - fitted.height) // 2
    canvas.paste(fitted, (x, y))


def draw_pill(draw: ImageDraw.ImageDraw, x: int, y: int, label: str, fill: str) -> int:
    chosen = font(18, True)
    width = int(draw.textlength(label, font=chosen)) + 34
    draw.rounded_rectangle((x, y, x + width, y + 34), radius=17, fill=fill)
    draw.text((x + 17, y + 7), label, font=chosen, fill=NAVY)
    return width


def draw_card(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    card: dict[str, str],
    accent: str,
    pale: str,
    compact: bool = False,
) -> None:
    x1, y1, x2, y2 = box
    draw.rounded_rectangle(box, radius=22, fill=pale, outline=LIGHT_BORDER, width=2)
    draw.rounded_rectangle((x1, y1, x1 + 9, y2), radius=5, fill=accent)
    if card.get("rule"):
        draw_pill(draw, x1 + 22, y1 + 18, card["rule"], WHITE)
        heading_y = y1 + 64
    else:
        heading_y = y1 + 22
    heading_font = font(24 if not compact else 21, True)
    body_font = font(19 if not compact else 17)
    heading = wrap_text(draw, card["heading"], heading_font, x2 - x1 - 44)
    draw.multiline_text((x1 + 22, heading_y), heading, font=heading_font, fill=NAVY, spacing=4)
    heading_box = draw.multiline_textbbox((x1 + 22, heading_y), heading, font=heading_font, spacing=4)
    body_y = heading_box[3] + 9
    if card.get("body"):
        body = wrap_text(draw, card["body"], body_font, x2 - x1 - 44)
        draw.multiline_text((x1 + 22, body_y), body, font=body_font, fill=TEXT, spacing=4)


def render_standard(layout: dict[str, object], illustration: Image.Image | None) -> Image.Image:
    canvas = Image.new("RGB", (WIDTH, HEIGHT), WHITE)
    draw = ImageDraw.Draw(canvas)
    accent = str(layout["accent"])
    pale = str(layout["pale"])

    draw.rectangle((0, 0, WIDTH, 12), fill=accent)
    draw.text((64, 31), "QUALITÉ WEB", font=font(18, True), fill=NAVY)
    right_label = "NAVIGATION · SÉRIE CONDENSÉE"
    right_width = draw.textlength(right_label, font=font(17, True))
    draw.text((WIDTH - 64 - right_width, 32), right_label, font=font(17, True), fill=MUTED)
    draw_pill(draw, 64, 70, str(layout["badge"]), pale)

    title = wrap_text(draw, str(layout["title"]), font(51, True), 1450)
    draw.multiline_text((64, 119), title, font=font(51, True), fill=NAVY, spacing=4)
    title_box = draw.multiline_textbbox((64, 119), title, font=font(51, True), spacing=4)
    body_top = max(238, title_box[3] + 28)

    left = (64, body_top, 734, 790)
    right = (780, body_top - 8, 1608, 764)
    if illustration is not None:
        paste_contained(canvas, trim_white(illustration), right)

    cards = list(layout.get("cards", []))
    card_gap = 16
    if len(cards) <= 3:
        card_height = min(150, (left[3] - left[1] - card_gap * (len(cards) - 1)) // max(1, len(cards)))
        for index, card in enumerate(cards):
            y1 = left[1] + index * (card_height + card_gap)
            draw_card(draw, (left[0], y1, left[2], y1 + card_height), card, accent, pale)
    else:
        columns = 2
        rows = (len(cards) + 1) // 2
        card_width = (left[2] - left[0] - card_gap) // 2
        card_height = (left[3] - left[1] - card_gap * (rows - 1)) // rows
        for index, card in enumerate(cards):
            column = index % columns
            row = index // columns
            x1 = left[0] + column * (card_width + card_gap)
            y1 = left[1] + row * (card_height + card_gap)
            draw_card(
                draw,
                (x1, y1, x1 + card_width, y1 + card_height),
                card,
                accent,
                pale,
                compact=True,
            )

    message_box = (64, 814, 1608, 876)
    draw.rounded_rectangle(message_box, radius=18, fill=NAVY)
    message = wrap_text(draw, str(layout["message"]), font(25, True), 1450)
    message_bbox = draw.multiline_textbbox((0, 0), message, font=font(25, True), spacing=4)
    message_y = message_box[1] + (message_box[3] - message_box[1] - (message_bbox[3] - message_bbox[1])) // 2 - 1
    draw.multiline_text((88, message_y), message, font=font(25, True), fill=WHITE, spacing=4)

    page = f"{int(layout['numero']):02d} / 16"
    page_width = draw.textlength(page, font=font(16, True))
    draw.text((WIDTH - 64 - page_width, 904), page, font=font(16, True), fill=MUTED)
    draw.text((64, 904), "RÈGLES OPQUAST · NAVIGATION", font=font(16, True), fill=MUTED)
    return canvas


def render_annex(layout: dict[str, object]) -> Image.Image:
    canvas = Image.new("RGB", (WIDTH, HEIGHT), WHITE)
    draw = ImageDraw.Draw(canvas)
    accent = str(layout["accent"])
    pale = str(layout["pale"])
    draw.rectangle((0, 0, WIDTH, 12), fill=accent)
    draw.text((64, 31), "QUALITÉ WEB", font=font(18, True), fill=NAVY)
    right_label = "NAVIGATION · SÉRIE CONDENSÉE"
    right_width = draw.textlength(right_label, font=font(17, True))
    draw.text((WIDTH - 64 - right_width, 32), right_label, font=font(17, True), fill=MUTED)
    draw_pill(draw, 64, 70, str(layout["badge"]), pale)
    draw.text((64, 119), str(layout["title"]), font=font(49, True), fill=NAVY)

    columns = list(layout["columns"])
    gap = 14
    x1 = 64
    top = 220
    total_width = 1544
    column_count = len(columns)
    column_width = (total_width - gap * (column_count - 1)) // column_count
    colors = ["#E8F1FF", "#F1ECFF", "#E3F7F1", "#FFE9E7", "#FFF0DE"]
    accents = ["#0063CB", "#6A5ACD", "#00866F", "#D65C5C", "#E87400"]
    for index, column in enumerate(columns):
        left = x1 + index * (column_width + gap)
        box = (left, top, left + column_width, 792)
        draw.rounded_rectangle(box, radius=22, fill=colors[index], outline=LIGHT_BORDER, width=2)
        draw.rounded_rectangle((left, top, left + column_width, top + 12), radius=6, fill=accents[index])
        heading = wrap_text(draw, str(column["heading"]), font(19, True), column_width - 28)
        draw.multiline_text((left + 14, top + 25), heading, font=font(19, True), fill=NAVY, spacing=3)
        heading_box = draw.multiline_textbbox((left + 14, top + 25), heading, font=font(19, True), spacing=3)
        y = heading_box[3] + 18
        for item in column["items"]:
            rule, label = item
            draw_pill(draw, left + 14, y, str(rule), WHITE)
            y += 42
            label_wrapped = wrap_text(draw, str(label), font(16, True), column_width - 28)
            draw.multiline_text((left + 14, y), label_wrapped, font=font(16, True), fill=TEXT, spacing=3)
            label_box = draw.multiline_textbbox((left + 14, y), label_wrapped, font=font(16, True), spacing=3)
            y = label_box[3] + 18

    message_box = (64, 814, 1608, 876)
    draw.rounded_rectangle(message_box, radius=18, fill=NAVY)
    draw.text((88, 832), str(layout["message"]), font=font(24, True), fill=WHITE)
    draw.text((64, 904), "RÈGLES OPQUAST · NAVIGATION", font=font(16, True), fill=MUTED)
    page = "16 / 16"
    page_width = draw.textlength(page, font=font(16, True))
    draw.text((WIDTH - 64 - page_width, 904), page, font=font(16, True), fill=MUTED)
    return canvas


def main() -> int:
    layouts = json.loads(LAYOUTS.read_text(encoding="utf-8"))
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for layout in layouts:
        numero = int(layout["numero"])
        illustration_path = ILLUSTRATIONS / f"slide-{numero:02d}.png"
        illustration = Image.open(illustration_path) if illustration_path.is_file() else None
        if layout.get("layout") == "annex":
            slide = render_annex(layout)
        else:
            slide = render_standard(layout, illustration)
        output = OUTPUT / f"slide-{numero:02d}.png"
        slide.save(output, optimize=True)
        print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
