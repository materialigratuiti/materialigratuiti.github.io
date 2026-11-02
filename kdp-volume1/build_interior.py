# -*- coding: utf-8 -*-
"""
Genera l'interno del Volume 1 (KDP, 6x9 pollici, bianco e nero, 125 pagine)
e il rapporto di controllo finale.

Uso:   python3 build_interior.py
Serve: reportlab, pypdf  (pip install reportlab pypdf)
Esce:  out/interior_vol1.pdf   out/controllo_finale.md   out/grids.json
"""
import json, os, random, re, subprocess, sys
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import simpleSplit

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from story_extras import EXTRAS
from cases_data import (CASES, MESSAGE, CAST, PROLOGUE, HOWTO, FINAL_STORY,
                        DEDUCTION, VERDICT_TEXT)

# ------------------------------------------------------------------ CONFIG
TITLE     = "The Marrowby Cases"
VOLUME    = "Volume 1"
SUBTITLE  = "A Cozy Murder Mystery Word Search Book for Adults"
TAGLINE   = "50 Cases \u00b7 800 Hidden Words \u00b7 One Final Deduction"
AUTHOR    = "YOUR NAME HERE"          # <-- metti il tuo nome o pseudonimo
YEAR      = "2026"
SEED      = 20260101                  # stesso seme = stesso libro

PT = 72.0
PAGE_W, PAGE_H = 6 * PT, 9 * PT       # 432 x 648 pt
MARGIN = 0.5 * PT                     # 36 pt: interno, esterno, alto, basso
GRID_N = 15
TOTAL_PAGES = 125
FRONT, CASES_PP, FINAL, SOL, BACK = 7, 100, 2, 13, 3   # = 125
assert FRONT + CASES_PP + FINAL + SOL + BACK == TOTAL_PAGES
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")
os.makedirs(OUT, exist_ok=True)

BANNED = ["MURDLE", "CRIMESEARCH", "MURDSEARCH", "KILL GRID", "KILLGRID",
          "KILLER SEARCH", "MURDER MYSTERY MANSION", "MURDER MYSTERY PARTY"]

# ------------------------------------------------------------------ FONT
def find_font(names):
    for d in ("/usr/share/fonts/truetype/liberation", "/usr/share/fonts/truetype/dejavu",
              "/usr/share/fonts/liberation", "/usr/share/fonts/dejavu",
              "/Library/Fonts", "C:/Windows/Fonts"):
        for n in names:
            p = os.path.join(d, n)
            if os.path.exists(p):
                return p
    raise SystemExit("Font TTF non trovato: %s (servono font incorporati per KDP)" % names)

pdfmetrics.registerFont(TTFont("Serif",   find_font(["LiberationSerif-Regular.ttf", "DejaVuSerif.ttf"])))
pdfmetrics.registerFont(TTFont("SerifB",  find_font(["LiberationSerif-Bold.ttf", "DejaVuSerif-Bold.ttf"])))
pdfmetrics.registerFont(TTFont("SerifI",  find_font(["LiberationSerif-Italic.ttf", "DejaVuSerif.ttf"])))
pdfmetrics.registerFont(TTFont("Sans",    find_font(["LiberationSans-Regular.ttf", "DejaVuSans.ttf"])))
pdfmetrics.registerFont(TTFont("SansB",   find_font(["LiberationSans-Bold.ttf", "DejaVuSans-Bold.ttf"])))
pdfmetrics.registerFont(TTFont("Mono",    find_font(["LiberationMono-Bold.ttf", "DejaVuSansMono-Bold.ttf"])))

# ------------------------------------------------------------------ GRIGLIE
DIRS = [(0, 1), (1, 0), (1, 1), (-1, 1), (0, -1), (-1, 0), (-1, -1), (1, -1)]  # (riga, colonna)
DIR_NAMES = ["E", "S", "SE", "NE", "W", "N", "NW", "SW"]
ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def count_occurrences(grid, word):
    n = len(grid); c = 0
    for r in range(n):
        for col in range(n):
            for dr, dc in DIRS:
                er, ec = r + dr * (len(word) - 1), col + dc * (len(word) - 1)
                if not (0 <= er < n and 0 <= ec < n):
                    continue
                if all(grid[r + dr * i][col + dc * i] == word[i] for i in range(len(word))):
                    c += 1
    return c

def try_make_grid(words, rng):
    n = GRID_N
    order = sorted(words, key=lambda w: -len(w))
    dirs = list(range(8)) * 2
    rng.shuffle(dirs)
    grid = [[None] * n for _ in range(n)]
    placed = {}
    for w, d in zip(order, dirs):
        ok = False
        for dd in [d] + rng.sample(range(8), 8):
            dr, dc = DIRS[dd]
            for _ in range(300):
                r, c = rng.randrange(n), rng.randrange(n)
                er, ec = r + dr * (len(w) - 1), c + dc * (len(w) - 1)
                if not (0 <= er < n and 0 <= ec < n):
                    continue
                if all(grid[r + dr * i][c + dc * i] in (None, w[i]) for i in range(len(w))):
                    for i in range(len(w)):
                        grid[r + dr * i][c + dc * i] = w[i]
                    placed[w] = (r, c, dd)
                    ok = True
                    break
            if ok:
                break
        if not ok:
            return None
    if len({d for (_, _, d) in placed.values()}) < 8:
        return None
    for _ in range(40):                      # riempimento + verifica unicita'
        g = [row[:] for row in grid]
        for r in range(n):
            for c in range(n):
                if g[r][c] is None:
                    g[r][c] = rng.choice(ALPHA)
        if all(count_occurrences(g, w) == 1 for w in words):
            return g, placed
    return None

def make_grid(words, seed):
    rng = random.Random(seed)
    for _ in range(500):
        res = try_make_grid(words, rng)
        if res:
            return res
    raise RuntimeError("Griglia impossibile per %s" % words)

# ------------------------------------------------------------------ DATI
def prepare():
    cases = []
    for i, (title, place, story, clues, clue, wl) in enumerate(CASES, 1):
        words = wl.split()
        assert len(words) == 15, "Caso %d: %d parole (devono essere 15)" % (i, len(words))
        assert clue == clue.upper() and clue not in words
        story = story + " " + EXTRAS[i]
        cases.append(dict(n=i, title=title, place=place, story=story, clues=clues,
                          clue=clue, words=words))
    return cases

def validate_words(cases):
    problems = []
    seen = {}
    for c in cases:
        for w in c["words"] + [c["clue"]]:
            if not re.fullmatch(r"[A-Z]{4,12}", w):
                problems.append("Caso %d: parola non valida %r" % (c["n"], w))
            if w == w[::-1]:
                problems.append("Caso %d: palindromo %s" % (c["n"], w))
            if w in seen:
                problems.append("DOPPIA: %s (caso %d e caso %d)" % (w, seen[w], c["n"]))
            seen[w] = c["n"]
        allw = c["words"] + [c["clue"]]
        for a in allw:
            for b in allw:
                if a != b and a in b:
                    problems.append("Caso %d: %s e' contenuta in %s" % (c["n"], a, b))
    initials = "".join(c["clue"][0] for c in cases)
    target = MESSAGE.replace(" ", "")
    if initials != target:
        problems.append("Iniziali %s != messaggio %s" % (initials, target))
    return problems

# ------------------------------------------------------------------ PDF
class Pdf:
    """Canvas con controllo dei margini: ogni disegno e' registrato."""
    def __init__(self, path):
        self.c = canvas.Canvas(path, pagesize=(PAGE_W, PAGE_H), pageCompression=1, initialFontName="Serif", initialFontSize=10)
        self.c.setTitle("%s, %s" % (TITLE, VOLUME)); self.c.setAuthor(AUTHOR)
        self.c.setSubject(SUBTITLE)
        self.page = 0
        self.ext = []          # (min_x, min_y, max_x, max_y) per pagina
        self._reset()
    def _reset(self):
        self.mn = [1e9, 1e9]; self.mx = [-1e9, -1e9]
    def _t(self, x0, y0, x1, y1):
        self.mn[0] = min(self.mn[0], x0, x1); self.mn[1] = min(self.mn[1], y0, y1)
        self.mx[0] = max(self.mx[0], x0, x1); self.mx[1] = max(self.mx[1], y0, y1)
    def next(self):
        self.c.showPage(); self.ext.append((self.mn[0], self.mn[1], self.mx[0], self.mx[1])); self._reset()
    def finish(self):
        self.ext.append((self.mn[0], self.mn[1], self.mx[0], self.mx[1]))
        self.c.save()
    # primitive tracciate
    def text(self, x, y, s, font="Serif", size=11, align="l", gray=0):
        self.c.setFont(font, size); self.c.setFillGray(gray)
        w = pdfmetrics.stringWidth(s, font, size)
        x0 = x if align == "l" else (x - w / 2 if align == "c" else x - w)
        self.c.drawString(x0, y, s)
        self._t(x0, y - 0.22 * size, x0 + w, y + 0.78 * size)
    def para(self, x, y, s, font="Serif", size=11, width=360, lead=None, gray=0):
        lead = lead or size * 1.42
        for line in simpleSplit(s, font, size, width):
            self.text(x, y, line, font, size, gray=gray); y -= lead
        return y
    def rect(self, x, y, w, h, stroke=0.6, fill=None):
        c = self.c
        c.setLineWidth(stroke); c.setStrokeGray(0)
        if fill is not None:
            c.setFillGray(fill)
        c.rect(x, y, w, h, stroke=1 if stroke else 0, fill=1 if fill is not None else 0)
        self._t(x - stroke / 2, y - stroke / 2, x + w + stroke / 2, y + h + stroke / 2)
    def line(self, x0, y0, x1, y1, w=0.5, gray=0):
        self.c.setLineWidth(w); self.c.setStrokeGray(gray); self.c.line(x0, y0, x1, y1)
        self._t(x0, y0, x1, y1)

L, R, B, T = MARGIN, PAGE_W - MARGIN, MARGIN, PAGE_H - MARGIN    # 36 .. 396 / 36 .. 612
CW = R - L                                                        # 360

def folio(p, n):                       # numero di pagina dentro il margine
    p.text(PAGE_W / 2, B + 2, str(n), "Sans", 8, "c", gray=0.35)

def heading(p, s, y=T - 20, size=20):
    p.text(PAGE_W / 2, y, s, "SerifB", size, "c")
    p.line(L + 60, y - 9, R - 60, y - 9, 0.8)
    return y - 34

# ---- pagine iniziali
def pg_title(p):
    p.text(PAGE_W / 2, 470, TITLE.upper(), "SerifB", 27, "c")
    p.line(L + 40, 452, R - 40, 452, 1.2)
    p.text(PAGE_W / 2, 420, VOLUME.upper(), "SansB", 16, "c")
    y = 360
    for line in simpleSplit(SUBTITLE, "SerifI", 17, CW - 40):
        p.text(PAGE_W / 2, y, line, "SerifI", 17, "c"); y -= 24
    p.text(PAGE_W / 2, 270, TAGLINE, "Sans", 10.5, "c")
    p.line(L + 40, 240, R - 40, 240, 1.2)
    p.text(PAGE_W / 2, 90, AUTHOR, "SerifB", 14, "c")

def pg_copyright(p):
    y = 400
    for s in ["Copyright \u00a9 %s %s. All rights reserved." % (YEAR, AUTHOR),
              "No part of this book may be reproduced, stored, or transmitted in any form without written permission of the author, except for brief quotations in a review.",
              "This is a work of fiction. All names, characters, places, and events are invented. Any resemblance to real people, living or dead, or to real places or events is entirely coincidental.",
              "First edition, %s." % YEAR,
              "Independently published."]:
        y = p.para(L + 20, y, s, "Serif", 10, CW - 40, 14.5) - 8

def pg_howto(p):
    y = heading(p, "How to Play")
    for num, s in HOWTO:
        p.text(L + 4, y, num, "SerifB", 12)
        y = p.para(L + 26, y, s, "Serif", 12, CW - 30, 17) - 9

def pg_cast(p, items, title):
    y = heading(p, title)
    for name, desc in items:
        p.text(L + 4, y, name, "SerifB", 12)
        y = p.para(L + 4, y - 15, desc, "Serif", 11, CW - 8, 15) - 11

def pg_prologue(p):
    y = heading(p, "The Night the Clocks Stopped", size=18)
    for s in PROLOGUE:
        y = p.para(L + 4, y, s, "Serif", 11.5, CW - 8, 16.5) - 8

def pg_board(p):
    y = heading(p, "Evidence Board", size=18)
    p.text(PAGE_W / 2, y + 6, "Write each clue word here as you find it.", "SerifI", 10, "c")
    top = y - 14; step = 19.5
    for k in range(25):
        yy = top - k * step
        for col, n in ((0, k + 1), (1, k + 26)):
            x = L + 4 + col * 182
            p.text(x, yy, "%d." % n, "SansB", 9)
            p.line(x + 22, yy - 2, x + 160, yy - 2, 0.5, 0.3)

# ---- caso: sinistra = storia, destra = griglia
def pg_story(p, c, num):
    p.text(L + 2, T - 14, "CASE %d" % c["n"], "SansB", 11, gray=0.3)
    p.text(L + 2, T - 46, c["title"], "SerifB", 22)
    p.text(L + 2, T - 66, c["place"], "SerifI", 12, gray=0.25)
    p.line(L, T - 76, R, T - 76, 0.8)
    y = p.para(L + 2, T - 100, c["story"], "Serif", 12.5, CW - 4, 18)
    y -= 12
    h = 18 + 3 * 21 + 14
    p.rect(L + 0.5, y - h + 4, CW - 1, h, 0.9)
    p.text(L + 12, y - 12, "THREE CLUES", "SansB", 9.5)
    yy = y - 32
    for i, cl in enumerate(c["clues"], 1):
        p.text(L + 12, yy, "%d." % i, "SansB", 10.5)
        p.text(L + 28, yy, cl, "Serif", 11.5)
        yy -= 21
    p.para(L + 2, y - h - 18, "Find the 15 words in the puzzle opposite. The 16th word is hidden, and is not on the list. Use the clues to guess it.",
           "SerifI", 10.5, CW - 4, 14.5, gray=0.2)
    folio(p, num)

def draw_grid(p, grid, x, ytop, cell, font_size, marks=None):
    n = GRID_N
    for r in range(n):
        for col in range(n):
            gx, gy = x + col * cell, ytop - (r + 1) * cell
            m = marks.get((r, col)) if marks else None
            if m == "clue":
                p.rect(gx, gy, cell, cell, 0, fill=0.25)
                p.c.setFillGray(1)
            elif m == "word":
                p.rect(gx, gy, cell, cell, 0, fill=0.78)
                p.c.setFillGray(0)
            p.c.setFont("Mono", font_size)
            p.c.setFillGray(1 if m == "clue" else 0)
            ch = grid[r][col]
            w = pdfmetrics.stringWidth(ch, "Mono", font_size)
            p.c.drawString(gx + (cell - w) / 2, gy + (cell - font_size * 0.72) / 2, ch)
            p._t(gx, gy, gx + cell, gy + cell)
    p.rect(x, ytop - n * cell, n * cell, n * cell, 1.2)

def pg_puzzle(p, c, g, num):
    p.text(PAGE_W / 2, T - 12, "CASE %d \u00b7 %s" % (c["n"], c["title"].upper()), "SansB", 10.5, "c")
    cell = (CW - 1.4) / GRID_N                       # ~24 pt = 1/3 pollice
    ytop = T - 30
    draw_grid(p, g["grid"], L + 0.7, ytop, cell, 14)
    y0 = ytop - GRID_N * cell - 22
    words = sorted(c["words"])
    colw = CW / 3
    for i, w in enumerate(words):
        col, row = i // 5, i % 5
        x = L + 6 + col * colw
        yy = y0 - row * 17
        p.rect(x, yy - 1, 8, 8, 0.7)
        p.text(x + 14, yy, w, "SansB", 10.5)
    yb = y0 - 5 * 17 - 14
    p.text(L + 6, yb, "Clue word:", "SansB", 10.5)
    p.line(L + 78, yb - 2, L + 78 + 150, yb - 2, 0.7)
    folio(p, num)

# ---- finali
def pg_final_story(p, num):
    y = heading(p, "The Final Case", size=24)
    p.text(PAGE_W / 2, y + 4, "Midnight at the Clock Shop", "SerifI", 14, "c")
    y -= 24
    for s in FINAL_STORY:
        y = p.para(L + 4, y, s, "Serif", 12.5, CW - 8, 18) - 10
    folio(p, num)

def pg_deduction(p, num):
    y = heading(p, "The Deduction", size=22)
    for s in DEDUCTION:
        y = p.para(L + 4, y, s, "Serif", 12, CW - 8, 17) - 6
    y -= 8
    bw, gap = 30, 6
    per = 10
    for row in range(5):
        for k in range(per):
            n = row * per + k + 1
            x = L + (CW - (per * bw + (per - 1) * gap)) / 2 + k * (bw + gap)
            p.text(x + bw / 2, y, str(n), "Sans", 7, "c", gray=0.35)
            p.rect(x, y - bw - 4, bw, bw, 0.9)
        y -= bw + 30
    p.para(L + 4, y - 4, "The message reads:", "SansB", 10)
    for k in range(3):
        p.line(L + 4, y - 36 - k * 28, R - 4, y - 36 - k * 28, 0.6, 0.3)
    p.para(L + 4, y - 36 - 3 * 28 - 6, "Check your answer on the last page of the Solutions section.", "SerifI", 10.5, CW - 8, 14, gray=0.2)
    folio(p, num)

# ---- soluzioni: 4 per pagina
def pg_solutions(p, batch, grids, num, first, last):
    p.text(PAGE_W / 2, T - 12, "SOLUTIONS", "SansB", 12, "c")
    gw = 172.0; cell = gw / GRID_N
    xs = [L + 0.7, R - gw - 0.7]
    for idx, c in enumerate(batch):
        col, row = idx % 2, idx // 2
        x = xs[col]
        ytop = T - 40 - row * (gw + 52)
        g = grids[c["n"] - 1]
        marks = {}
        for w, (r0, c0, dd) in g["placed"].items():
            dr, dc = DIRS[dd]
            for i in range(len(w)):
                marks[(r0 + dr * i, c0 + dc * i)] = "clue" if w == c["clue"] else "word"
        p.text(x, ytop + 4, "Case %d" % c["n"], "SansB", 8.5)
        draw_grid(p, g["grid"], x, ytop - 2, cell, 7.6, marks)
        p.text(x, ytop - 2 - gw - 12, "Clue word: %s" % c["clue"], "SansB", 8.5)
    if last:                                   # mezza pagina libera: verdetto
        y = T - 40 - 1 * (gw + 52) - 10
        # solo se la seconda riga e' vuota
        y = T - 40 - (gw + 52) - 10
        p.rect(L + 0.7, y - 150, CW - 1.4, 150, 1.2)
        p.text(PAGE_W / 2, y - 20, "THE VERDICT (spoiler!)", "SansB", 11, "c")
        yy = y - 42
        yy = p.para(L + 12, yy, VERDICT_TEXT[0], "SerifB", 11.5, CW - 24, 16) - 6
        p.para(L + 12, yy, VERDICT_TEXT[1], "Serif", 10.5, CW - 24, 14.5)
    folio(p, num)

# ---- chiusura
def pg_review(p, num):
    y = heading(p, "Thank You, Detective!", size=22)
    for s in ["Thank you for solving the cases of Marrowby. I hope the village has charmed you, and that you enjoyed every clue.",
              "If you had fun, please take a moment to leave a short review on Amazon. A few honest words help other puzzle lovers find this book, and they mean the world to a small independent author.",
              "Open the camera on your phone, go to your orders, or search for the book title, then tap \u201cWrite a customer review\u201d. Thank you!"]:
        y = p.para(L + 4, y, s, "Serif", 12.5, CW - 8, 18) - 10
    folio(p, num)

def pg_preview(p, num):
    y = heading(p, "Coming Next", size=22)
    p.text(PAGE_W / 2, y + 2, "THE MARROWBY CASES \u00b7 VOLUME 2", "SansB", 12, "c")
    y -= 30
    for s in ["A new season brings a new mystery to Marrowby. The harvest festival is coming, the pumpkins are enormous, and someone has been very careless with a trophy.",
              "Fifty brand-new cases. Fifty new puzzle grids. One new final deduction.",
              "The constable is already knocking on your door."]:
        y = p.para(L + 4, y, s, "Serif", 12.5, CW - 8, 18) - 10
    folio(p, num)

def pg_notes(p, num):
    y = heading(p, "Detective Notes", size=20)
    yy = y
    while yy > B + 30:
        p.line(L + 4, yy, R - 4, yy, 0.5, 0.55); yy -= 24
    folio(p, num)

# ------------------------------------------------------------------ MAIN
def spine_inches(pages, paper="white"):
    return pages * (0.002252 if paper == "white" else 0.0025)

def build():
    cases = prepare()
    problems = validate_words(cases)
    if problems:
        print("\n".join(problems)); raise SystemExit("ERRORI NELLE PAROLE: correggi cases_data.py")
    grids = []
    for c in cases:
        g, placed = make_grid(c["words"] + [c["clue"]], SEED + c["n"])
        grids.append(dict(grid=["".join(r) for r in g], placed=placed))
    grid_list = [[list(r) for r in g["grid"]] for g in grids]
    for g, gl in zip(grids, grid_list):
        g["grid"] = gl
    with open(os.path.join(OUT, "grids.json"), "w") as f:
        json.dump([dict(case=c["n"], clue=c["clue"], words=sorted(c["words"]),
                        grid=["".join(r) for r in g["grid"]],
                        placed={w: dict(row=v[0], col=v[1], dir=DIR_NAMES[v[2]]) for w, v in g["placed"].items()})
                   for c, g in zip(cases, grids)], f, indent=1)

    pdf_path = os.path.join(OUT, "interior_vol1.pdf")
    p = Pdf(pdf_path)
    labels = []
    def page(fn, *a, label=""):
        p.page += 1; labels.append(label); fn(p, *a); p.next()
    # 1-7
    page(pg_title, label="title"); page(pg_copyright, label="copyright")
    page(pg_howto, label="howto")
    page(pg_cast, CAST[:7], "The People of Marrowby (1)", label="cast1")
    page(pg_cast, CAST[7:], "The People of Marrowby (2)", label="cast2")
    page(pg_prologue, label="prologue"); page(pg_board, label="board")
    # 8-107: storia a sinistra (pagine pari), griglia a destra (dispari)
    for c, g in zip(cases, grids):
        assert (p.page + 1) % 2 == 0
        page(pg_story, c, p.page + 1, label="story%d" % c["n"])
        page(pg_puzzle, c, g, p.page + 1, label="puzzle%d" % c["n"])
    # 108-109
    page(pg_final_story, p.page + 1, label="final"); page(pg_deduction, p.page + 1, label="deduction")
    # 110-122
    for k in range(SOL):
        batch = cases[k * 4:(k + 1) * 4]
        page(pg_solutions, batch, grids, p.page + 1, k == 0, k == SOL - 1, label="sol%d" % (k + 1))
    # 123-125
    page(pg_review, p.page + 1, label="review"); page(pg_preview, p.page + 1, label="preview")
    page(pg_notes, p.page + 1, label="notes")
    p.finish()
    return cases, grids, p, pdf_path

def report(cases, grids, p, pdf_path):
    from pypdf import PdfReader
    rd = PdfReader(pdf_path)
    n = len(rd.pages)
    sizes = {(round(float(pg.mediabox.width), 2), round(float(pg.mediabox.height), 2)) for pg in rd.pages}
    lines = []
    ok = lambda b: "OK" if b else "ERRORE"
    lines.append("# Controllo finale - %s, %s\n" % (TITLE, VOLUME))
    lines.append("## Pagine e formato")
    lines.append("- Pagine nel PDF: **%d** (previste %d) -> %s" % (n, TOTAL_PAGES, ok(n == TOTAL_PAGES)))
    lines.append("- Dimensione pagina: %s pt (6x9\" = 432x648) -> %s" % (sizes, ok(sizes == {(432.0, 648.0)})))
    lines.append("- Il numero di pagine e' DISPARI (125). Non e' un errore, ma l'ultima pagina avra' il retro bianco. **Da verificare nell'anteprima KDP.**")
    lines.append("- Storia sempre sulla pagina sinistra (pari), griglia sempre a destra (dispari): %s" % ok(True))
    # margini
    bad = []
    for i, (x0, y0, x1, y1) in enumerate(p.ext, 1):
        if x0 < L - 0.01 or y0 < B - 0.01 or x1 > R + 0.01 or y1 > T + 0.01:
            bad.append("pag %d (%.1f,%.1f)-(%.1f,%.1f)" % (i, x0, y0, x1, y1))
    lines.append("\n## Margini (minimo 0,5\" = 36 pt per lato, interno incluso; nessun bleed)")
    lines.append("- Pagine con contenuto fuori dai margini: %s -> %s" % (bad if bad else "nessuna", ok(not bad)))
    lines.append("- Margine minimo misurato (pt): sinistra %.1f, destra %.1f, basso %.1f, alto %.1f" % (
        min(e[0] for e in p.ext), PAGE_W - max(e[2] for e in p.ext),
        min(e[1] for e in p.ext), PAGE_H - max(e[3] for e in p.ext)))
    # parole
    allw = [w for c in cases for w in c["words"] + [c["clue"]]]
    dup = {w for w in allw if allw.count(w) > 1}
    lines.append("\n## Parole")
    lines.append("- Parole totali nel libro: %d, uniche: %d, ripetute: %s -> %s" % (len(allw), len(set(allw)), sorted(dup) or "nessuna", ok(not dup)))
    cnt_bad = []
    dirs_missing = []
    for c, g in zip(cases, grids):
        gr = g["grid"]
        for w in c["words"] + [c["clue"]]:
            if count_occurrences(gr, w) != 1:
                cnt_bad.append((c["n"], w))
        used = {d for (_, _, d) in g["placed"].values()}
        if len(used) < 8:
            dirs_missing.append(c["n"])
    lines.append("- Ogni parola compare esattamente 1 volta nella sua griglia (8 direzioni, anche al contrario): %s %s" % (cnt_bad or "", ok(not cnt_bad)))
    lines.append("- Griglie con tutte e 8 le direzioni usate: %d/50 -> %s" % (50 - len(dirs_missing), ok(not dirs_missing)))
    lines.append("- Parole-indizio non presenti in nessuna lista: %s" % ok(all(c["clue"] not in c["words"] for c in cases)))
    lines.append("- Iniziali delle 50 parole-indizio = \"%s\" -> %s" % ("".join(c["clue"][0] for c in cases), ok("".join(c["clue"][0] for c in cases) == MESSAGE.replace(" ", ""))))
    lens = [len(w) for w in allw]
    lines.append("- Lunghezza parole: min %d, max %d, media %.1f lettere" % (min(lens), max(lens), sum(lens) / len(lens)))
    # storie
    wc = [len((c["story"] + " " + " ".join(c["clues"])).split()) for c in cases]
    lines.append("\n## Storie (misurato: storia + 3 indizi)")
    lines.append("- Parole per caso: min %d, max %d, media %.0f (obiettivo ~120)" % (min(wc), max(wc), sum(wc) / len(wc)))
    # testo PDF: marchi
    txt = " ".join((pg.extract_text() or "") for pg in rd.pages).upper()
    hits = [b for b in BANNED if b in txt]
    lines.append("\n## Marchi vietati nel testo del PDF")
    lines.append("- Cercati: %s -> trovati: %s -> %s" % (", ".join(BANNED), hits or "nessuno", ok(not hits)))
    lines.append("- 'COZY MYSTERY' (frase esatta) nel PDF: %s" % ("PRESENTE" if "COZY MYSTERY" in txt else "assente (si usa 'Cozy Murder Mystery Word Search' solo nel sottotitolo)"))
    # font incorporati
    try:
        out = subprocess.run(["pdffonts", pdf_path], capture_output=True, text=True).stdout.strip().splitlines()[2:]
        noemb = [l for l in out if len(l.split()) >= 5 and l.split()[-5] != "yes"]
        lines.append("\n## Font")
        lines.append("- Font nel PDF: %d, non incorporati: %d -> %s" % (len(out), len(noemb), ok(not noemb)))
    except Exception:
        lines.append("\n## Font\n- non misurato (pdffonts non disponibile)")
    # copertina
    sp = spine_inches(TOTAL_PAGES)
    lines.append("\n## Copertina (formula KDP carta bianca B/N: 0,002252\" a pagina)")
    lines.append("- Dorso = %d x 0.002252 = **%.4f\"**" % (TOTAL_PAGES, sp))
    lines.append("- Larghezza totale = 2 x 6\" + dorso + 0,25\" (bleed) = **%.4f\"** (~%.2f\")" % (12 + sp + 0.25, 12 + sp + 0.25))
    lines.append("- Altezza totale = 9\" + 0,25\" = **9.25\"**")
    lines.append("- Verifica comunque con il Cover Calculator ufficiale KDP prima di impaginare la copertina.")
    lines.append("\n## Non misurato / da fare a mano")
    lines.append("- Anteprima KDP (Previewer) e avvisi di caricamento: non fatti qui.")
    lines.append("- Controllo parole offensive nelle lettere casuali delle griglie: non misurato.")
    lines.append("- Nome dell'autore nel PDF: segnaposto 'YOUR NAME HERE', da cambiare in AUTHOR.")
    with open(os.path.join(OUT, "controllo_finale.md"), "w") as f:
        f.write("\n".join(lines) + "\n")
    print("\n".join(lines))

if __name__ == "__main__":
    cases, grids, p, path = build()
    report(cases, grids, p, path)
