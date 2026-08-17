"""Build panel-white.jpg by placing the head at an explicitly solved position.

Page is the 3.75 x 2.25in BLEED sheet. Trim is 0.125in in from every edge,
so the trim box is x 0.125..3.625, y 0.125..2.125.
The photo panel is flush right: x 2.43..3.75.

Measured in the source cutout (durden-cutout-transparent-1200.webp, 1200x2117):
  head top  y = 14
  chin/neck y = 464
  head left x = 434
  ear right x = 801   <- the pixel that was getting cut

We solve for a scale and offset so that:
  ear right  lands at page x = 3.625 - EAR_INSIDE_TRIM
  head top   lands at page y = 0.125 + TOP_INSIDE_TRIM
  head width equals HEAD_W_IN
"""
import sys, json
from PIL import Image

PAGE_W, PAGE_H = 3.75, 2.25
BLEED = 0.125
PANEL_W = 1.32
PANEL_X0 = PAGE_W - PANEL_W          # 2.43
DPI = 600

EAR_INSIDE_TRIM = 0.145
TOP_INSIDE_TRIM = 0.145

G = json.load(open("headgeom.json"))
HEAD_TOP, HEAD_L, EAR_R = G["HEAD_TOP"], G["HEAD_L"], G["EAR_R"]

SRC = "durden-cutout-transparent-1200.webp"


def build(head_w_in, out):
    im = Image.open(SRC).convert("RGBA")
    s = head_w_in / (EAR_R - HEAD_L)          # inches per source pixel

    ear_page_x = (PAGE_W - BLEED) - EAR_INSIDE_TRIM
    top_page_y = BLEED + TOP_INSIDE_TRIM

    def page_x(x): return ear_page_x + (x - EAR_R) * s
    def page_y(y): return top_page_y + (y - HEAD_TOP) * s

    out_w = int(round(PANEL_W * DPI))
    out_h = int(round(PAGE_H * DPI))
    canvas = Image.new("RGB", (out_w, out_h), (255, 255, 255))

    W, H = im.size
    fig = im.resize((max(1, round(W * s * DPI)), max(1, round(H * s * DPI))), Image.LANCZOS)
    # source (0,0) in page inches:
    ox_in = page_x(0) - PANEL_X0
    oy_in = page_y(0)
    canvas.paste(fig, (round(ox_in * DPI), round(oy_in * DPI)), fig)
    canvas.save(out, quality=96, subsampling=0)

    rep = {
        "out": out, "head_w_in": round(head_w_in, 4),
        "scale_in_per_srcpx": round(s, 6),
        "head_left_in": round(page_x(HEAD_L), 4),
        "ear_right_in": round(page_x(EAR_R), 4),
        "head_top_in": round(page_y(HEAD_TOP), 4),
        "chin_in": round(page_y(G["NECK"]), 4),
        "ear_clearance_inside_trim_in": round((PAGE_W - BLEED) - page_x(EAR_R), 4),
        "top_clearance_inside_trim_in": round(page_y(HEAD_TOP) - BLEED, 4),
        "gap_head_to_panel_edge_in": round(page_x(HEAD_L) - PANEL_X0, 4),
        "gap_head_to_text_safe_in": round(page_x(HEAD_L) - (PAGE_W - 1.46), 4),
    }
    print(json.dumps(rep, indent=2))
    return rep


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "A"
    if which == "A":
        # SHIPPED. 1.030in keeps the head's left edge 0.02in inside the panel.
        # Do not raise this to 1.057: the head then clips on the panel's hard left edge.
        build(1.030, "panel-white.jpg")
    else:
        build(0.960, "panel-white.jpg")      # ~9% smaller, air on both sides, not chosen
