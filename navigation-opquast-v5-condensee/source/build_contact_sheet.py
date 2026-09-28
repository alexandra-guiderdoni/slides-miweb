#!/usr/bin/env python3
"""Construit une planche de contrôle 4 x 4 à partir des PNG finaux."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[1]
SLIDES = ROOT / "assets" / "slides"
OUTPUT = ROOT / "source" / "contact-sheet.png"
FONT = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

columns = 4
rows = 4
cell_width = 400
cell_height = 255
margin = 18
label_height = 28

sheet = Image.new(
    "RGB",
    (
        margin + columns * (cell_width + margin),
        margin + rows * (cell_height + label_height + margin),
    ),
    "#F5F5F5",
)
draw = ImageDraw.Draw(sheet)
label_font = ImageFont.truetype(FONT, 18)

for index in range(16):
    numero = index + 1
    row = index // columns
    column = index % columns
    x = margin + column * (cell_width + margin)
    y = margin + row * (cell_height + label_height + margin)
    slide = Image.open(SLIDES / f"slide-{numero:02d}.png").convert("RGB")
    thumb = ImageOps.contain(slide, (cell_width, cell_height), Image.Resampling.LANCZOS)
    sheet.paste(thumb, (x, y))
    draw.text((x, y + cell_height + 4), f"SLIDE {numero:02d}", font=label_font, fill="#161B4B")

sheet.save(OUTPUT, optimize=True)
print(OUTPUT)
