# -*- coding: utf-8 -*-
"""
Copertina completa KDP (retro + dorso + fronte), disegnata in vettoriale.
Uso:  python3 build_cover.py        -> out/cover_vol1.pdf  (+ out/cover_vol1_preview.png se c'e' pdftoppm)

Misure (carta bianca, B/N interno, 125 pagine):
  dorso   = 125 x 0.002252"          = 0.2815"
  largh.  = 6 + dorso + 6 + 2 x 0.125 = 12.5315"
  altezza = 9 + 2 x 0.125             = 9.25"
Copertina opaca (matte): si sceglie su KDP, non nel file.
"""
import math, os, subprocess, sys
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_interior import TITLE, VOLUME, SUBTITLE, TAGLINE, AUTHOR, TOTAL_PAGES, spine_inches, find_font

PT = 72.0
BLEED = 0.125 * PT
TRIM_W, TRIM_H = 6 * PT, 9 * PT
SPINE = spine_inches(TOTAL_PAGES) * PT
W = 2 * BLEED + 2 * TRIM_W + SPINE
H = TRIM_H + 2 * BLEED
BACK_X0 = BLEED
SPINE_X0 = BLEED + TRIM_W
FRONT_X0 = SPINE_X0 + SPINE
SAFE = 0.25 * PT     # distanza minima del testo dal taglio

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
os.makedirs(OUT, exist_ok=True)
path = os.path.join(OUT, "cover_vol1.pdf")

pdfmetrics.registerFont(TTFont("SerifB", find_font(["LiberationSerif-Bold.ttf", "DejaVuSerif-Bold.ttf"])))
pdfmetrics.registerFont(TTFont("SerifI", find_font(["LiberationSerif-Italic.ttf", "DejaVuSerif.ttf"])))
pdfmetrics.registerFont(TTFont("Serif",  find_font(["LiberationSerif-Regular.ttf", "DejaVuSerif.ttf"])))
pdfmetrics.registerFont(TTFont("SansB",  find_font(["LiberationSans-Bold.ttf", "DejaVuSans-Bold.ttf"])))

CREAM = (0.96, 0.92, 0.82)
GOLD = (0.93, 0.74, 0.30)
NAVY_TOP, NAVY_BOT = (0.05, 0.08, 0.17), (0.14, 0.22, 0.36)
HOUSE = (0.04, 0.06, 0.11)
WINDOW = (0.98, 0.78, 0.35)

c = canvas.Canvas(path, pagesize=(W, H), initialFontName="Serif", initialFontSize=10)
c.setTitle("%s %s - cover" % (TITLE, VOLUME)); c.setAuthor(AUTHOR)

def fill(rgb): c.setFillColorRGB(*rgb, alpha=1)
def stroke(rgb): c.setStrokeColorRGB(*rgb)

def text(x, y, s, font, size, rgb=CREAM, align="c", spacing=0):
    c.setFont(font, size); fill(rgb)
    w = pdfmetrics.stringWidth(s, font, size) + spacing * (len(s) - 1)
    x0 = x - w / 2 if align == "c" else (x if align == "l" else x - w)
    t = c.beginText(x0, y); t.setFont(font, size); t.setCharSpace(spacing); t.textOut(s); c.drawText(t)

# ---------- sfondo: cielo notturno a fasce (tutta la copertina, bleed incluso)
N = 90
for i in range(N):
    t = i / (N - 1)
    fill(tuple(NAVY_TOP[k] + (NAVY_BOT[k] - NAVY_TOP[k]) * t for k in range(3)))
    c.rect(0, H - (i + 1) * H / N - 0.5, W, H / N + 1, stroke=0, fill=1)

# stelle (deterministiche)
import random
rng = random.Random(7)
for _ in range(170):
    x, y = rng.uniform(0, W), rng.uniform(H * 0.45, H)
    if SPINE_X0 - 2 < x < FRONT_X0 + 2:
        continue
    fill((1, 0.97, 0.85)); c.circle(x, y, rng.choice([0.5, 0.7, 1.0]), stroke=0, fill=1)

# luna sul fronte
mx, my = FRONT_X0 + TRIM_W * 0.87, 300
for r, a in ((46, 0.10), (38, 0.16), (30, 0.25)):
    c.setFillColorRGB(1, 0.95, 0.75, alpha=a); c.circle(mx, my, r, stroke=0, fill=1)
c.setFillColorRGB(1, 0.96, 0.82, alpha=1); c.circle(mx, my, 22, stroke=0, fill=1)

# ---------- colline e villaggio: continua su retro, dorso e fronte
def hill(base, amp, ph, col):
    fill(col); p = c.beginPath(); p.moveTo(0, 0); p.lineTo(0, base)
    steps = 120
    for i in range(steps + 1):
        x = W * i / steps
        p.lineTo(x, base + amp * math.sin(x / 85.0 + ph) + amp * 0.5 * math.sin(x / 33.0 + ph * 2))
    p.lineTo(W, 0); p.close(); c.drawPath(p, stroke=0, fill=1)

hill(150, 14, 0.5, (0.09, 0.15, 0.24))
hill(118, 12, 2.0, (0.06, 0.10, 0.17))

def house(x, base, w, h, roof, chimney=True):
    fill(HOUSE)
    c.rect(x, base, w, h, stroke=0, fill=1)
    p = c.beginPath(); p.moveTo(x - 4, base + h); p.lineTo(x + w / 2, base + h + roof); p.lineTo(x + w + 4, base + h); p.close()
    c.drawPath(p, stroke=0, fill=1)
    if chimney:
        c.rect(x + w * 0.68, base + h + roof * 0.35, 6, roof * 0.6, stroke=0, fill=1)
    fill(WINDOW)
    cols = max(1, int(w // 22)); rows = max(1, int(h // 30))
    for r in range(rows):
        for k in range(cols):
            if rng.random() < 0.55:
                c.rect(x + 7 + k * (w - 14) / cols + 1, base + 8 + r * 26, 7, 10, stroke=0, fill=1)

def tree(x, base, r):
    fill((0.03, 0.07, 0.09)); c.rect(x - 2, base, 4, r * 0.7, stroke=0, fill=1)
    c.circle(x, base + r * 1.1, r, stroke=0, fill=1)

# fila di casette lungo tutta la larghezza (evita il dorso)
x = 10
while x < W - 20:
    w = rng.choice([34, 40, 48, 56]); h = rng.choice([30, 38, 46]); roof = rng.choice([16, 20, 26])
    if not (SPINE_X0 - w - 4 < x < FRONT_X0 + 4):
        base = 110 + rng.choice([0, 3, 6])
        house(x, base, w, h, roof)
        if rng.random() < 0.5:
            tree(x + w + 8, base, rng.choice([9, 12, 14]))
    x += w + rng.choice([10, 16, 24])

# chiesa con campanile sul fronte
cx = FRONT_X0 + 14
fill(HOUSE)
c.rect(cx, 110, 70, 62, stroke=0, fill=1)
p = c.beginPath(); p.moveTo(cx - 5, 172); p.lineTo(cx + 35, 206); p.lineTo(cx + 75, 172); p.close(); c.drawPath(p, stroke=0, fill=1)
c.rect(cx + 70, 110, 34, 135, stroke=0, fill=1)
p = c.beginPath(); p.moveTo(cx + 66, 245); p.lineTo(cx + 87, 292); p.lineTo(cx + 108, 245); p.close(); c.drawPath(p, stroke=0, fill=1)
fill(WINDOW); c.rect(cx + 14, 128, 8, 20, stroke=0, fill=1); c.rect(cx + 44, 128, 8, 20, stroke=0, fill=1)
# orologio del campanile fermo alle 12:07
fill(CREAM); c.circle(cx + 87, 215, 11, stroke=0, fill=1)
stroke(HOUSE); c.setLineWidth(1.4)
c.line(cx + 87, 215, cx + 87, 224)            # lancetta minuti (verso le 12)
c.setLineWidth(1.0)
a = math.radians(90 - 7 * 6)
c.line(cx + 87, 215, cx + 87 + 6 * math.cos(a), 215 + 6 * math.sin(a))

# primo piano scuro
fill((0.03, 0.05, 0.09)); c.rect(0, 0, W, 98, stroke=0, fill=1)
hill(98, 5, 1.0, (0.03, 0.05, 0.09))

# ---------- orologio grande fermo alle 12:07 (centro del fronte)
ox, oy, R = FRONT_X0 + TRIM_W / 2, 336, 74
fill((0.02, 0.03, 0.06)); c.setFillColorRGB(0.02, 0.03, 0.06, alpha=0.55); c.circle(ox + 4, oy - 5, R + 12, stroke=0, fill=1)
c.setFillColorRGB(*GOLD, alpha=1); c.circle(ox, oy, R + 8, stroke=0, fill=1)
fill((0.97, 0.94, 0.86)); c.circle(ox, oy, R, stroke=0, fill=1)
stroke((0.2, 0.15, 0.1)); c.setLineWidth(1.2); c.circle(ox, oy, R - 5, stroke=1, fill=0)
for k in range(60):
    a = math.radians(90 - k * 6)
    r1 = R - 5; r2 = R - (13 if k % 5 == 0 else 9)
    c.setLineWidth(1.8 if k % 5 == 0 else 0.6)
    c.line(ox + r1 * math.cos(a), oy + r1 * math.sin(a), ox + r2 * math.cos(a), oy + r2 * math.sin(a))
numerals = ["XII", "I", "II", "III", "IIII", "V", "VI", "VII", "VIII", "IX", "X", "XI"]
for k, nmr in enumerate(numerals):
    a = math.radians(90 - k * 30)
    text(ox + (R - 27) * math.cos(a), oy + (R - 27) * math.sin(a) - 4, nmr, "SerifB", 10, (0.15, 0.1, 0.08))
# lancette: 12:07
stroke((0.1, 0.07, 0.05)); c.setLineCap(1)
a_min = math.radians(90 - 7 * 6)
a_hr = math.radians(90 - (0 + 7 / 60.0) * 30)
c.setLineWidth(3.6); c.line(ox, oy, ox + (R - 36) * math.cos(a_hr), oy + (R - 36) * math.sin(a_hr))
c.setLineWidth(2.4); c.line(ox, oy, ox + (R - 17) * math.cos(a_min), oy + (R - 17) * math.sin(a_min))
fill(GOLD); c.circle(ox, oy, 4.2, stroke=0, fill=1)
# lente d'ingrandimento sopra l'orologio
stroke(GOLD); c.setLineWidth(5)
lx, ly, lr = ox + 64, oy - 58, 25
c.setFillColorRGB(0.8, 0.9, 1.0, alpha=0.22); c.circle(lx, ly, lr, stroke=1, fill=1)
c.setLineWidth(8); c.setLineCap(1); stroke((0.30, 0.19, 0.10))
c.line(lx + lr * 0.72, ly - lr * 0.72, lx + lr * 0.72 + 30, ly - lr * 0.72 - 30)
c.setFillColorRGB(1, 1, 1, alpha=1)

# ---------- testo FRONTE
fx = FRONT_X0 + TRIM_W / 2
text(fx, H - BLEED - 52, VOLUME.upper(), "SansB", 13, GOLD, spacing=5)
c.setLineWidth(1); stroke(GOLD)
c.line(fx - 70, H - BLEED - 62, fx + 70, H - BLEED - 62)
text(fx, H - BLEED - 108, "THE MARROWBY", "SerifB", 40, CREAM, spacing=1.5)
text(fx, H - BLEED - 166, "CASES", "SerifB", 68, GOLD, spacing=4)
text(fx, H - BLEED - 202, "A Cozy Murder Mystery Word Search Book", "SerifI", 15.5, CREAM)
text(fx, H - BLEED - 222, "for Adults", "SerifI", 15.5, CREAM)
text(fx, BLEED + 62, "50 CASES  ·  800 HIDDEN WORDS  ·  ONE FINAL DEDUCTION", "SansB", 8.2, CREAM, spacing=1.2)
text(fx, BLEED + 34, AUTHOR.upper(), "SerifB", 15, GOLD, spacing=3)

# ---------- DORSO
fill((0.02, 0.04, 0.08)); c.setFillColorRGB(0.02, 0.04, 0.08, alpha=0.88)
c.rect(SPINE_X0, 0, SPINE, H, stroke=0, fill=1)
c.saveState()
c.translate(SPINE_X0 + SPINE / 2 + 4, H - BLEED - 24)
c.rotate(-90)
text(0, 0, "THE MARROWBY CASES", "SerifB", 14, GOLD, "l", spacing=1)
text(TRIM_H - 48, 0, AUTHOR.upper(), "SansB", 9, CREAM, "r", spacing=1)
c.restoreState()

# ---------- RETRO
bx = BACK_X0 + TRIM_W / 2
left, right = BACK_X0 + 34, BACK_X0 + TRIM_W - 34
fill((0.02, 0.04, 0.08)); c.setFillColorRGB(0.02, 0.04, 0.08, alpha=0.72)
c.roundRect(BACK_X0 + 22, 150, TRIM_W - 44, H - BLEED - 150 - 28, 8, stroke=0, fill=1)

def wrap(s, font, size, width):
    words, lines, cur = s.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if pdfmetrics.stringWidth(t, font, size) <= width: cur = t
        else: lines.append(cur); cur = w
    return lines + [cur]

y = H - BLEED - 60
text(bx, y, "THE CLOCKMAKER IS DEAD.", "SerifB", 20, GOLD); y -= 24
text(bx, y, "THE CLOCKS HAVE STOPPED AT 12:07.", "SerifB", 14, CREAM); y -= 34
body = ["Welcome to Marrowby, a sleepy village where the tea is strong and the gossip is stronger. Everyone has something to hide, and the constable needs a sharp mind from outside the village.",
        "Read each short case, solve the word search, and find the hidden clue word. After 50 cases, your clues spell out one name."]
for para in body:
    for ln in wrap(para, "Serif", 11.5, right - left):
        text(left, y, ln, "Serif", 11.5, CREAM, "l"); y -= 16
    y -= 8
y -= 4
for b in ["50 cozy village cases, each with 3 clues", "15x15 puzzles with a 16th hidden word", "800 words, in every direction", "Evidence Board and final deduction", "Complete solutions included"]:
    fill(GOLD); c.circle(left + 4, y + 3.5, 2.2, stroke=0, fill=1)
    text(left + 16, y, b, "Serif", 11.5, CREAM, "l"); y -= 17
# area codice a barre KDP (2" x 1.2"), in basso a destra del retro, lasciata bianca
bw, bh = 2.0 * PT, 1.2 * PT
c.setFillColorRGB(1, 1, 1, alpha=1); c.rect(BACK_X0 + TRIM_W - 0.25 * PT - bw, BLEED + 0.25 * PT, bw, bh, stroke=0, fill=1)

c.showPage(); c.save()
print("Cover: %.4f x %.4f in  (spine %.4f in) -> %s" % (W / PT, H / PT, SPINE / PT, path))
try:
    subprocess.run(["pdftoppm", "-r", "60", "-png", "-singlefile", path, os.path.join(OUT, "cover_vol1_preview")], check=True)
except Exception as e:
    print("anteprima PNG non creata:", e)
