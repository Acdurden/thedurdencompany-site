"""Build the Pencil. wordmark as outlined SVG + transparent PNG.

Type spec, matching the business card exactly:
  "Pencil"  Inter Tight, weight 800, letter-spacing -0.012em
  "."       same face, colored gold #C08A2D

Text is converted to OUTLINES so nothing depends on a font being installed or loaded.
"""
import pathlib
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.misc.transform import Transform
import uharfbuzz as hb

SRC_WOFF2 = "node_modules/@fontsource/inter-tight/files/inter-tight-latin-800-normal.woff2"
TTF = "inter-tight-800.ttf"

INK = "#0E1B2A"
WHITE = "#FFFFFF"
GOLD = "#C08A2D"
TRACKING_EM = -0.012          # matches the card's letter-spacing

# --- woff2 -> ttf, because HarfBuzz cannot read woff/woff2 -------------------
f = TTFont(SRC_WOFF2)
f.flavor = None
f.save(TTF)

font = TTFont(TTF)
upem = font["head"].unitsPerEm          # take from head, hb.Face.upem lies on webfonts
glyphset = font.getGlyphSet()

blob = hb.Blob.from_file_path(TTF)
face = hb.Face(blob)
hbfont = hb.Font(face)
hbfont.scale = (upem, upem)


def shape(text):
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(hbfont, buf)
    out, x = [], 0
    for info, pos in zip(buf.glyph_infos, buf.glyph_positions):
        out.append((info.codepoint, x + pos.x_offset, pos.y_offset))
        x += pos.x_advance + TRACKING_EM * upem
    return out, x


order = font.getGlyphOrder()


def glyph_path(gid, dx, dy):
    pen = SVGPathPen(glyphset)
    # flip Y: font space is y-up, SVG is y-down
    tpen = TransformPen(pen, Transform(1, 0, 0, -1, dx, -dy))
    glyphset[order[gid]].draw(tpen)
    return pen.getCommands()


from fontTools.pens.boundsPen import BoundsPen


def ink_bounds(placed):
    """Exact bounding box of the drawn outlines, in font units, y-up."""
    x0 = y0 = 1e9
    x1 = y1 = -1e9
    for gid, dx, dy in placed:
        bp = BoundsPen(glyphset)
        tp = TransformPen(bp, Transform(1, 0, 0, 1, dx, dy))
        glyphset[order[gid]].draw(tp)
        if bp.bounds is None:
            continue
        a, b, c, d = bp.bounds
        x0, y0, x1, y1 = min(x0, a), min(y0, b), max(x1, c), max(y1, d)
    return x0, y0, x1, y1


def build(word="Pencil", dot=".", fg=INK, name="pencil-wordmark"):
    gl_word, adv_word = shape(word)
    gl_dot, _ = shape(dot)
    placed_word = [(g, x, y) for g, x, y in gl_word]
    placed_dot = [(g, adv_word + x, y) for g, x, y in gl_dot]

    x0, y0, x1, y1 = ink_bounds(placed_word + placed_dot)
    vb_w, vb_h = x1 - x0, y1 - y0

    # translate so the ink's top-left sits at 0,0 in SVG space (y flipped)
    tx, ty = -x0, y1

    paths_word = [glyph_path(g, x, y) for g, x, y in placed_word]
    paths_dot = [glyph_path(g, x, y) for g, x, y in placed_dot]

    body = "\n".join(f'    <path d="{d}" fill="{fg}"/>' for d in paths_word if d) \
        + "\n" + "\n".join(f'    <path d="{d}" fill="{GOLD}"/>' for d in paths_dot if d)

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vb_w:.1f} {vb_h:.1f}" role="img" aria-label="Pencil">
  <title>Pencil</title>
  <g transform="translate({tx:.1f}, {ty:.1f})">
{body}
  </g>
</svg>
"""
    pathlib.Path(f"{name}.svg").write_text(svg)
    print(f"  {name}.svg   viewBox 0 0 {vb_w:.1f} {vb_h:.1f}   aspect {vb_w/vb_h:.4f}")
    return vb_w, vb_h


print("building wordmarks...")
w, h = build(fg=INK, name="pencil-wordmark")
build(fg=WHITE, name="pencil-wordmark-white")
print(f"  upem {upem}")
