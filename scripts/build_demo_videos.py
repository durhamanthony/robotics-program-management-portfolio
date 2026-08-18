#!/usr/bin/env python3
"""Build four browser-playable workflow animations for the public portfolio."""

from __future__ import annotations

import math
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "media" / "videos"
WIDTH, HEIGHT, FPS, SECONDS = 1280, 720, 20, 12
NAVY = "#073b33"
GREEN = "#087f6b"
TEAL = "#16b8aa"
CYAN = "#66e0d2"
INK = "#082d29"
MUTED = "#57716e"
PAPER = "#f3f7f6"
WHITE = "#ffffff"
AMBER = "#e9a23b"
RED = "#c94c4c"
BLUE = "#2f79b7"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    name = "DejaVuSans-Bold.ttf" if bold else "DejaVuSans.ttf"
    return ImageFont.truetype(f"/usr/share/fonts/truetype/dejavu/{name}", size)


F12 = font(12)
F14 = font(14)
F16 = font(16)
F18 = font(18)
F18B = font(18, True)
F22B = font(22, True)
F28B = font(28, True)
F34B = font(34, True)


def label(draw: ImageDraw.ImageDraw, xy: tuple[int, int], value: str, fill=INK, f=F16, anchor=None) -> None:
    draw.text(xy, value, fill=fill, font=f, anchor=anchor)


def rounded(draw: ImageDraw.ImageDraw, box, fill, outline=None, radius=14, width=1) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def arrow(draw: ImageDraw.ImageDraw, start, end, fill=TEAL, width=5) -> None:
    draw.line((start, end), fill=fill, width=width)
    angle = math.atan2(end[1] - start[1], end[0] - start[0])
    for delta in (2.55, -2.55):
        point = (end[0] + 15 * math.cos(angle + delta), end[1] + 15 * math.sin(angle + delta))
        draw.line((end, point), fill=fill, width=width)


def humanoid(draw: ImageDraw.ImageDraw, x: float, y: float, scale=1.0, carrying=False, color=BLUE) -> None:
    x, y = int(x), int(y)
    r = int(12 * scale)
    draw.ellipse((x-r, y-68*scale-r, x+r, y-68*scale+r), fill="#f0c7a5", outline=INK, width=2)
    draw.rounded_rectangle((x-17*scale, y-55*scale, x+17*scale, y-15*scale), radius=int(6*scale), fill=color, outline=INK, width=2)
    draw.line((x-12*scale, y-16*scale, x-16*scale, y+22*scale), fill=INK, width=max(2, int(5*scale)))
    draw.line((x+12*scale, y-16*scale, x+16*scale, y+22*scale), fill=INK, width=max(2, int(5*scale)))
    arm_y = y-42*scale
    if carrying:
        draw.line((x-15*scale, arm_y, x-29*scale, y-27*scale), fill=INK, width=max(2, int(4*scale)))
        draw.line((x+15*scale, arm_y, x+29*scale, y-27*scale), fill=INK, width=max(2, int(4*scale)))
        draw.rectangle((x-28*scale, y-33*scale, x+28*scale, y-10*scale), fill="#d99243", outline=INK, width=2)
    else:
        draw.line((x-15*scale, arm_y, x-24*scale, y-15*scale), fill=INK, width=max(2, int(4*scale)))
        draw.line((x+15*scale, arm_y, x+24*scale, y-15*scale), fill=INK, width=max(2, int(4*scale)))


def quadruped(draw: ImageDraw.ImageDraw, x: float, y: float, scale=1.0, color="#d7e2e0") -> None:
    x, y = int(x), int(y)
    draw.rounded_rectangle((x-32*scale, y-34*scale, x+28*scale, y-5*scale), radius=int(8*scale), fill=color, outline=INK, width=2)
    draw.rounded_rectangle((x+25*scale, y-31*scale, x+46*scale, y-13*scale), radius=int(5*scale), fill=GREEN, outline=INK, width=2)
    for dx in (-22, -4, 12, 25):
        draw.line((x+dx*scale, y-6*scale, x+(dx-5)*scale, y+24*scale), fill=INK, width=max(2, int(5*scale)))
    draw.ellipse((x+33*scale, y-26*scale, x+38*scale, y-21*scale), fill=CYAN)


def mobile_robot(draw: ImageDraw.ImageDraw, x: float, y: float, scale=1.0, carrying=False) -> None:
    x, y = int(x), int(y)
    draw.rounded_rectangle((x-34*scale, y-40*scale, x+34*scale, y+8*scale), radius=int(9*scale), fill=BLUE, outline=INK, width=2)
    draw.ellipse((x-27*scale, y, x-8*scale, y+19*scale), fill=INK)
    draw.ellipse((x+8*scale, y, x+27*scale, y+19*scale), fill=INK)
    draw.line((x, y-40*scale, x, y-83*scale), fill=INK, width=max(2, int(7*scale)))
    draw.ellipse((x-10*scale, y-95*scale, x+10*scale, y-75*scale), fill=TEAL, outline=INK, width=2)
    if carrying:
        draw.rectangle((x-27*scale, y-70*scale, x+27*scale, y-44*scale), fill="#d99243", outline=INK, width=2)


def base_frame(title: str, stage: str, index: int, progress: float) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    image = Image.new("RGB", (WIDTH, HEIGHT), PAPER)
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, WIDTH, 88), fill=NAVY)
    label(draw, (54, 27), title, WHITE, F28B)
    rounded(draw, (1010, 24, 1226, 62), "#13594e", radius=19)
    label(draw, (1118, 43), f"STAGE {index}/6", CYAN, F14, "mm")
    draw.rectangle((0, 88, int(WIDTH * progress), 95), fill=TEAL)
    label(draw, (54, 119), stage.upper(), GREEN, F14)
    label(draw, (54, 655), "Operational workflow animation • Fictional scenario • Demonstration purposes only", MUTED, F14)
    label(draw, (1226, 655), "Anthony Durham", INK, F14, "ra")
    return image, draw


def stage_info(frame: int) -> tuple[int, float, float]:
    total = FPS * SECONDS
    progress = min(frame / (total - 1), 1)
    stage_float = progress * 6
    index = min(int(stage_float), 5)
    local = stage_float - index
    return index, min(local, 1), progress


def retail_scene(frame: int) -> Image.Image:
    stages = ["Tablet request", "Locate stock", "Traverse existing store", "Retrieve item", "Employee handoff", "Inventory confirmation"]
    idx, local, progress = stage_info(frame)
    image, draw = base_frame("Retail backroom humanoid fulfillment", stages[idx], idx + 1, progress)
    rounded(draw, (46, 160, 1234, 620), WHITE, "#cbdad7", 18, 2)

    # Backroom infrastructure remains unchanged.
    for sx in (85, 235, 385):
        draw.rectangle((sx, 218, sx+110, 528), fill="#d9e4e1", outline=INK, width=2)
        for sy in (280, 350, 420, 490):
            draw.line((sx, sy, sx+110, sy), fill="#78918d", width=3)
        for row in range(4):
            draw.rectangle((sx+12, 239+70*row, sx+52, 268+70*row), fill="#d99243", outline=INK)
            draw.rectangle((sx+59, 239+70*row, sx+98, 268+70*row), fill="#c57936", outline=INK)
    label(draw, (83, 188), "EXISTING STOCK SHELVES", MUTED, F12)
    draw.rectangle((545, 300, 615, 529), fill="#d7e2e0", outline=INK, width=2)
    draw.rectangle((568, 400, 592, 424), fill="#b8cbc7", outline=INK)
    label(draw, (545, 271), "DOOR", MUTED, F12)
    for n in range(4):
        draw.rectangle((660+n*32, 474-n*28, 710+n*32, 502-n*28), fill="#d7e2e0", outline=INK)
    label(draw, (664, 510), "SHORT STAIR", MUTED, F12)
    draw.rectangle((905, 448, 1155, 523), fill="#dce8e5", outline=INK, width=2)
    label(draw, (1030, 485), "EMPLOYEE HANDOFF", INK, F16, "mm")

    route = [(790, 525), (515, 525), (515, 448), (775, 380), (885, 432), (1025, 432)]
    for a, b in zip(route, route[1:]):
        draw.line((*a, *b), fill="#9dc8c1", width=5)

    tablet_x = 925
    if idx == 0:
        pulse = int(10 * math.sin(local * math.pi))
        rounded(draw, (930-pulse, 200-pulse, 1175+pulse, 340+pulse), NAVY, radius=18)
        label(draw, (1052, 231), "ASSOCIATE TABLET", CYAN, F14, "mm")
        label(draw, (1052, 268), "SKU 55821 • SIZE 9", WHITE, F18B, "mm")
        rounded(draw, (970, 292, 1134, 326), TEAL, radius=17)
        label(draw, (1052, 309), "SEND REQUEST", WHITE, F14, "mm")
        humanoid(draw, 790, 542)
    elif idx == 1:
        humanoid(draw, 790 - 245*local, 542)
        rounded(draw, (900, 220, 1165, 342), "#e8f5f2", GREEN, 14, 2)
        label(draw, (1032, 248), "LOCATION CONFIRMED", GREEN, F14, "mm")
        label(draw, (1032, 285), "Shelf B-14 • Bin 03", INK, F18B, "mm")
        label(draw, (1032, 318), "Inventory confidence: 99%", MUTED, F14, "mm")
    elif idx == 2:
        if local < .42:
            humanoid(draw, 545, 542 - 135*(local/.42))
        elif local < .72:
            humanoid(draw, 545 + 230*((local-.42)/.30), 407 - 28*((local-.42)/.30))
        else:
            humanoid(draw, 775 + 85*((local-.72)/.28), 379 + 48*((local-.72)/.28))
        rounded(draw, (880, 205, 1180, 336), "#fff5df", AMBER, 14, 2)
        label(draw, (1030, 235), "WHY LEGS HERE", AMBER, F14, "mm")
        label(draw, (1030, 274), "Door • stair • narrow aisle", INK, F18B, "mm")
        label(draw, (1030, 308), "No floor reconfiguration", MUTED, F14, "mm")
    elif idx == 3:
        x = 470 - 110*local
        humanoid(draw, x, 542, carrying=local > .45)
        rounded(draw, (870, 208, 1177, 350), "#e8f5f2", GREEN, 14, 2)
        label(draw, (1024, 238), "APPROVED ITEM CLASS", GREEN, F14, "mm")
        label(draw, (1024, 277), "Closed shoe box • 3.1 kg", INK, F18B, "mm")
        label(draw, (1024, 315), "Barcode verified", MUTED, F14, "mm")
    elif idx == 4:
        humanoid(draw, 785 + 220*local, 447, carrying=local < .78)
        draw.ellipse((1090, 374, 1115, 399), fill="#f0c7a5", outline=INK)
        draw.rectangle((1080, 399, 1125, 472), fill="#7457a7", outline=INK, width=2)
        label(draw, (1098, 492), "ASSOCIATE", MUTED, F12, "mm")
        if local > .78:
            draw.rectangle((1065, 413, 1118, 438), fill="#d99243", outline=INK)
    else:
        humanoid(draw, 790, 542)
        rounded(draw, (865, 204, 1185, 370), NAVY, radius=16)
        label(draw, (1025, 236), "MISSION COMPLETE", CYAN, F14, "mm")
        label(draw, (1025, 280), "SKU 55821 handed off", WHITE, F18B, "mm")
        label(draw, (1025, 318), "Inventory: 12 → 11", WHITE, F22B, "mm")
        rounded(draw, (931, 340, 1119, 360), TEAL, radius=10)
    humanoid(draw, 835, 558, scale=.82, color="#7a60b6")
    label(draw, (834, 588), "ROBOT 2 READY", MUTED, F12, "mm")
    return image


def security_scene(frame: int) -> Image.Image:
    stages = ["Dispatch routes", "Uneven terrain", "Gate anomaly", "Human verification", "Network safe state", "Low-battery dock"]
    idx, local, progress = stage_info(frame)
    image, draw = base_frame("Human-supervised quadruped night patrol", stages[idx], idx + 1, progress)
    rounded(draw, (46, 160, 890, 620), "#102b35", "#33535a", 18, 2)
    rounded(draw, (920, 160, 1234, 620), WHITE, "#cbdad7", 18, 2)
    # Site map.
    draw.line((85, 545, 850, 545), fill="#405c62", width=4)
    draw.rectangle((105, 223, 312, 360), fill="#28454b", outline="#77908f", width=2)
    draw.rectangle((560, 215, 810, 355), fill="#28454b", outline="#77908f", width=2)
    label(draw, (207, 288), "BUILDING A", "#c8d8d6", F18B, "mm")
    label(draw, (684, 282), "BUILDING B", "#c8d8d6", F18B, "mm")
    for n in range(4):
        draw.rectangle((400+n*30, 495-n*22, 448+n*30, 520-n*22), fill="#6c7d7b", outline="#a8bbb8")
    draw.line((835, 375, 835, 545), fill="#8aa09d", width=5)
    draw.line((785, 375, 785, 545), fill="#8aa09d", width=5)
    draw.line((785, 415, 835, 415), fill="#8aa09d", width=4)
    draw.line((785, 455, 835, 455), fill="#8aa09d", width=4)
    label(draw, (810, 356), "GATE", "#a9c0bd", F12, "mm")
    route_a = [(140, 505), (230, 410), (430, 430), (625, 395), (790, 500)]
    route_b = [(745, 500), (620, 455), (490, 260), (300, 405), (150, 465)]
    draw.line(route_a, fill=TEAL, width=4)
    draw.line(route_b, fill="#6a9fce", width=4)

    if idx == 0:
        quadruped(draw, 125+620*local, 530-40*math.sin(local*math.pi), .9, CYAN)
        quadruped(draw, 745-590*local, 520-40*math.sin(local*math.pi), .9, "#81b9e6")
    elif idx == 1:
        x = 350+230*local
        y = 515-90*local
        quadruped(draw, x, y, .95, CYAN)
        label(draw, (111, 186), "ROUTE TEST: STEPS + ROUGH SURFACE", CYAN, F14)
    elif idx == 2:
        quadruped(draw, 720+60*local, 512, .95, CYAN)
        radius = 18+int(20*abs(math.sin(local*4*math.pi)))
        draw.ellipse((810-radius, 440-radius, 810+radius, 440+radius), outline=RED, width=5)
        label(draw, (810, 440), "!", WHITE, F22B, "mm")
    elif idx == 3:
        quadruped(draw, 770, 512, .95, CYAN)
        draw.line((810, 440, 934, 292), fill=AMBER, width=3)
    elif idx == 4:
        quadruped(draw, 505, 470, .95, "#9bafac")
        draw.arc((444, 390, 566, 512), 200, 340, fill=RED, width=6)
        draw.line((474, 425, 537, 488), fill=RED, width=6)
    else:
        quadruped(draw, 730+75*local, 510, .95, CYAN)
        draw.rectangle((797, 492, 858, 552), fill="#1e4d46", outline=CYAN, width=3)
        label(draw, (827, 572), "DOCK", "#a9c0bd", F12, "mm")

    # Human operations panel.
    label(draw, (950, 190), "SECURITY OPERATIONS", GREEN, F14)
    status = ["2 routes active", "Terrain within envelope", "Anomaly detected", "Operator reviewing", "Robot safely stopped", "Robot charging"][idx]
    rounded(draw, (948, 220, 1206, 278), "#e8f5f2" if idx not in (2, 4) else "#fff0ea", radius=12)
    label(draw, (1077, 249), status, RED if idx in (2, 4) else GREEN, F16, "mm")
    items = [
        ("Robot A", "Route 01", "Online"),
        ("Robot B", "Route 02", "Online" if idx < 4 else "Safe stop"),
        ("Robot C", "Reserve", "Charging"),
    ]
    for n, item in enumerate(items):
        y = 305+n*72
        rounded(draw, (948, y, 1206, y+58), WHITE, "#cbdad7", 9, 1)
        label(draw, (966, y+12), item[0], INK, F14)
        label(draw, (966, y+36), item[1], MUTED, F12)
        label(draw, (1188, y+29), item[2], GREEN if "Online" in item[2] or "Charging" in item[2] else RED, F12, "rm")
    label(draw, (1077, 552), "Human decides the response", INK, F14, "mm")
    return image


def npi_scene(frame: int) -> Image.Image:
    stages = ["Receive tote", "Verify payload", "Travel route", "Place at station", "Return mission", "Controlled fault"]
    idx, local, progress = stage_info(frame)
    image, draw = base_frame("AD-01 first-customer workflow", stages[idx], idx + 1, progress)
    rounded(draw, (46, 160, 1234, 620), WHITE, "#cbdad7", 18, 2)
    draw.rectangle((92, 245, 322, 515), fill="#e6efed", outline=INK, width=2)
    draw.rectangle((958, 245, 1188, 515), fill="#e6efed", outline=INK, width=2)
    label(draw, (207, 285), "STATION A", GREEN, F18B, "mm")
    label(draw, (1073, 285), "STATION B", GREEN, F18B, "mm")
    draw.rectangle((132, 375, 282, 425), fill="#c7d8d5", outline=INK, width=2)
    draw.rectangle((998, 375, 1148, 425), fill="#c7d8d5", outline=INK, width=2)
    draw.line((322, 487, 958, 487), fill="#a9c4c0", width=8)
    for x in range(370, 950, 90):
        draw.ellipse((x, 479, x+14, 493), fill=TEAL)
    x = [358, 405, 400+500*local, 900+80*local, 900-500*local, 650][idx]
    carrying = idx in (0, 1, 2, 3)
    mobile_robot(draw, x, 490, 1.15, carrying=carrying and not (idx == 3 and local > .7))
    if idx == 0:
        arrow(draw, (240, 360), (350, 405))
    elif idx == 1:
        rounded(draw, (455, 245, 806, 355), "#e8f5f2", GREEN, 14, 2)
        label(draw, (630, 278), "PAYLOAD CHECK", GREEN, F14, "mm")
        label(draw, (630, 318), "11.8 kg • approved tote", INK, F22B, "mm")
    elif idx == 2:
        arrow(draw, (390, 548), (890, 548))
    elif idx == 3 and local > .7:
        draw.rectangle((1015, 345, 1128, 390), fill="#d99243", outline=INK, width=2)
    elif idx == 5:
        radius = 25+int(12*abs(math.sin(local*5*math.pi)))
        draw.ellipse((650-radius, 393-radius, 650+radius, 393+radius), outline=RED, width=6)
        rounded(draw, (462, 220, 838, 330), "#fff0ea", RED, 14, 2)
        label(draw, (650, 253), "CONTROLLED SAFE STATE", RED, F18B, "mm")
        label(draw, (650, 294), "Mission stopped • evidence retained", INK, F16, "mm")
    labels = ["Tote accepted", "Mass and barcode pass", "Mapped 18 m route", "Placement confirmed", "Ready for next mission", "Fault isolated; human notified"]
    rounded(draw, (396, 564, 884, 603), NAVY, radius=18)
    label(draw, (640, 584), labels[idx], WHITE, F16, "mm")
    return image


def support_scene(frame: int) -> Image.Image:
    stages = ["Fleet alert", "Customer correlation", "Severity decision", "Evidence package", "Restore or dispatch", "Customer confirmation"]
    idx, local, progress = stage_info(frame)
    image, draw = base_frame("Robotics support evidence-to-restoration workflow", stages[idx], idx + 1, progress)
    rounded(draw, (46, 160, 1234, 620), WHITE, "#cbdad7", 18, 2)
    boxes = [
        ("1", "FLEET ALERT", "Robot R-184 • motor temp", 75),
        ("2", "CUSTOMER CASE", "Site 042 • entitlement", 270),
        ("3", "TRIAGE", "Severity 2 • safe state", 465),
        ("4", "EVIDENCE", "Logs • telemetry • video", 660),
        ("5", "ACTION", "Remote restore / field", 855),
        ("6", "CLOSE", "Customer confirms service", 1050),
    ]
    for n, (num, heading, detail, x) in enumerate(boxes):
        active = n <= idx
        fill = NAVY if n == idx else ("#e8f5f2" if active else "#edf2f1")
        outline = TEAL if active else "#cbdad7"
        rounded(draw, (x, 250, x+155, 400), fill, outline, 14, 3 if active else 1)
        draw.ellipse((x+14, 264, x+46, 296), fill=TEAL if active else "#b5c6c3")
        label(draw, (x+30, 280), num, WHITE, F16, "mm")
        label(draw, (x+14, 318), heading, CYAN if n == idx else GREEN if active else MUTED, F12)
        words = detail.split(" ")
        line1 = " ".join(words[:3])
        line2 = " ".join(words[3:])
        label(draw, (x+14, 347), line1, WHITE if n == idx else INK, F12)
        if line2:
            label(draw, (x+14, 368), line2, WHITE if n == idx else INK, F12)
        if n < len(boxes)-1:
            arrow(draw, (x+158, 325), (x+190, 325), TEAL if active else "#b5c6c3", 3)

    activity = [
        ("Telemetry rule", "Threshold exceeded; duplicate alerts grouped"),
        ("Installed product", "Serial, version, site, contract, and owner matched"),
        ("Human decision", "Safety impact reviewed; Severity 2 assigned"),
        ("Diagnostic bundle", "Correlated identifier links logs, telemetry, and case"),
        ("Recovery control", "Runbook attempted; field work order available"),
        ("Formal closure", "Customer validates service; problem record updated"),
    ][idx]
    rounded(draw, (182, 448, 1098, 570), "#f6faf9", "#cbdad7", 14, 2)
    label(draw, (214, 478), activity[0].upper(), GREEN, F14)
    label(draw, (214, 519), activity[1], INK, F18B)
    bar = 120 + int(730 * local)
    rounded(draw, (214, 542, 1015, 555), "#dbe7e5", radius=7)
    rounded(draw, (214, 542, min(214+bar, 1015), 555), TEAL, radius=7)
    return image


def encode(filename: str, renderer) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    target = OUT / filename
    command = [
        "ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
        "-s", f"{WIDTH}x{HEIGHT}", "-r", str(FPS), "-i", "-", "-an", "-c:v", "libx264",
        "-preset", "medium", "-crf", "24", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(target),
    ]
    process = subprocess.Popen(command, stdin=subprocess.PIPE)
    assert process.stdin is not None
    for frame in range(FPS * SECONDS):
        process.stdin.write(renderer(frame).tobytes())
    process.stdin.close()
    if process.wait() != 0:
        raise RuntimeError(f"ffmpeg failed for {target}")
    print(f"Built {target.relative_to(ROOT)} ({target.stat().st_size:,} bytes)")


def main() -> None:
    encode("retail-humanoid-fulfillment.mp4", retail_scene)
    encode("quadruped-night-security.mp4", security_scene)
    encode("ad01-new-robot-npi.mp4", npi_scene)
    encode("robotics-support-triage.mp4", support_scene)


if __name__ == "__main__":
    main()
