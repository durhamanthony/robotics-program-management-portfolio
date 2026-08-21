#!/usr/bin/env python3
"""Create high-contrast restroom sign textures for the MuJoCo model."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "simulations" / "restroom_cleaning" / "assets"
FONT_CANDIDATES = (
    Path("C:/Windows/Fonts/arialbd.ttf"),
    Path("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"),
)


def font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for candidate in FONT_CANDIDATES:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


def make_sign(filename: str, lines: tuple[str, ...], background: tuple[int, int, int]) -> None:
    width, height = 1024, 256
    image = Image.new("RGB", (width, height), background)
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((8, 8, width - 8, height - 8), radius=26, outline=(230, 240, 238), width=10)
    selected_font = font(96 if len(lines) == 1 else 76)
    spacing = 8
    boxes = [draw.textbbox((0, 0), line, font=selected_font) for line in lines]
    heights = [box[3] - box[1] for box in boxes]
    total_height = sum(heights) + spacing * (len(lines) - 1)
    y_pos = (height - total_height) / 2
    for line, box, line_height in zip(lines, boxes, heights):
        line_width = box[2] - box[0]
        draw.text(((width - line_width) / 2, y_pos - box[1]), line, font=selected_font, fill=(255, 255, 255))
        y_pos += line_height + spacing
    OUTPUT.mkdir(parents=True, exist_ok=True)
    image.save(OUTPUT / filename, optimize=True)


def main() -> None:
    make_sign("cleaning_supplies.png", ("CLEANING", "SUPPLIES"), (18, 80, 72))
    make_sign("charging_station.png", ("CHARGING", "STATION"), (0, 116, 104))
    make_sign("garbage.png", ("GARBAGE",), (28, 34, 38))
    make_sign("paper_towels.png", ("PAPER TOWEL", "DISPENSER"), (74, 84, 92))


if __name__ == "__main__":
    main()
