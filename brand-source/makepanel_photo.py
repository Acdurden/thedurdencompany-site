"""Build panel-white.jpg from a WHITE-BACKGROUND rectangular photo instead of the
transparent cutout. Same solver, same clearances, same output geometry.

The source's background must be pure white or it will print as a visible block against
the card's true white. linkedin-headshot-white.jpg measures 255/255/255 on every edge.

Run:  python3 makepanel_photo.py [head_width_in]
"""
import sys, json
import numpy as np
from PIL import Image

PAGE_W, PAGE_H = 3.75, 2.25
BLEED = 0.125
PANEL_W = 1.32
PANEL_X0 = PAGE_W - PANEL_W          # 2.43
DPI = 600

EAR_INSIDE_TRIM = 0.145
TOP_INSIDE_TRIM = 0.145

SRC = "linkedin-headshot-white.jpg"
HEAD_W_IN = float(sys.argv[1]) if len(sys.argv) > 1 else 1.030


def head_landmarks(path):
    a = np.array(Image.open(path).convert("RGB")).astype(int)
    subj = a.min(axis=2) < 244                      # background is pure white
    rows = np.where(subj.any(axis=1))[0]
    top = int(rows[0])
    # walk down; the chin is the narrowest row before the shoulders flare out
    widths = []
    for y in range(top, min(top + 800, a.shape[0])):
        xs = np.where(subj[y])[0]
        widths.append((y, int(xs[0]), int(xs[-1])) if len(xs) else (y, 0, 0))
    lo = top + int(0.55 * (len(widths)))
    hi = top + int(0.80 * (len(widths)))
    chin = min(((r - l), y) for y, l, r in widths if lo <= y <= hi)[1]
    band = [(y, l, r) for y, l, r in widths if y <= chin]
    return {"HEAD_TOP": top, "NECK": int(chin),
            "HEAD_L": min(l for _, l, _ in band),
            "EAR_R": max(r for _, _, r in band)}


def build(head_w_in, out="panel-white.jpg"):
    G = head_landmarks(SRC)
    HEAD_TOP, HEAD_L, EAR_R = G["HEAD_TOP"], G["HEAD_L"], G["EAR_R"]
    im = Image.open(SRC).convert("RGB")
    W, H = im.size

    s = head_w_in / (EAR_R - HEAD_L)
    ear_page_x = (PAGE_W - BLEED) - EAR_INSIDE_TRIM
    top_page_y = BLEED + TOP_INSIDE_TRIM

    def page_x(x): return ear_page_x + (x - EAR_R) * s
    def page_y(y): return top_page_y + (y - HEAD_TOP) * s

    out_w, out_h = int(round(PANEL_W * DPI)), int(round(PAGE_H * DPI))
    canvas = Image.new("RGB", (out_w, out_h), (255, 255, 255))
    fig = im.resize((max(1, round(W * s * DPI)), max(1, round(H * s * DPI))), Image.LANCZOS)
    canvas.paste(fig, (round((page_x(0) - PANEL_X0) * DPI), round(page_y(0) * DPI)))
    canvas.save(out, quality=96, subsampling=0)

    rep = {
        "source": SRC, **G, "head_w_in": round(head_w_in, 4),
        "head_left_in": round(page_x(HEAD_L), 4),
        "ear_right_in": round(page_x(EAR_R), 4),
        "head_top_in": round(page_y(HEAD_TOP), 4),
        "chin_in": round(page_y(G["NECK"]), 4),
        "ear_clearance_inside_trim_in": round((PAGE_W - BLEED) - page_x(EAR_R), 4),
        "top_clearance_inside_trim_in": round(page_y(HEAD_TOP) - BLEED, 4),
        "gap_head_to_panel_edge_in": round(page_x(HEAD_L) - PANEL_X0, 4),
        "photo_covers_panel": {
            "left_edge_in": round(page_x(0), 4), "right_edge_in": round(page_x(W), 4),
            "top_edge_in": round(page_y(0), 4), "bottom_edge_in": round(page_y(H), 4),
        },
    }
    print(json.dumps(rep, indent=2))
    return rep


if __name__ == "__main__":
    build(HEAD_W_IN)
