"""Render the bleed PDF, derive the trim PDF, make outlined copies,
then verify: fonts embedded (zero Type3), QR decodes, trim-box overlay."""
import subprocess, pathlib, sys
from playwright.sync_api import sync_playwright
import pymupdf
from PIL import Image, ImageDraw
from pyzbar.pyzbar import decode as zdecode

PT = 72.0
BLEED_W, BLEED_H = 3.75 * PT, 2.25 * PT
INSET = 0.125 * PT           # 9pt


def to_pdf(html, out):
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.goto("file://" + str(pathlib.Path(html).resolve()))
        pg.wait_for_timeout(700)
        pg.pdf(path=out, width="3.75in", height="2.25in", print_background=True,
               margin={"top": "0", "right": "0", "bottom": "0", "left": "0"})
        b.close()


def trim_from_bleed(src, out):
    """Cut 0.125in off every side, producing a true 3.5 x 2.0in page."""
    s = pymupdf.open(src)
    d = pymupdf.open()
    for i in range(s.page_count):
        pg = d.new_page(width=BLEED_W - 2 * INSET, height=BLEED_H - 2 * INSET)
        pg.show_pdf_page(
            pymupdf.Rect(-INSET, -INSET, BLEED_W - INSET, BLEED_H - INSET),
            s, i)
    d.save(out, garbage=4, deflate=True)
    d.close(); s.close()


def outline(src, out):
    subprocess.run(["gs", "-o", out, "-dNoOutputFonts", "-sDEVICE=pdfwrite",
                    "-dPDFSETTINGS=/prepress",
                    "-dColorConversionStrategy=/LeaveColorUnchanged", src],
                   check=True, capture_output=True)


def check_fonts(path):
    d = pymupdf.open(path)
    rows = []
    for i in range(d.page_count):
        for f in d.get_page_fonts(i):
            rows.append((i, f[1], f[2], f[3], f[4]))  # ext, type, basefont, name
    d.close()
    return rows


def check_qr(path, dpi):
    d = pymupdf.open(path)
    hits = []
    for i in range(d.page_count):
        pm = d.load_page(i).get_pixmap(dpi=dpi)
        img = Image.frombytes("RGB", (pm.width, pm.height), pm.samples)
        for r in zdecode(img):
            hits.append((i, dpi, r.data.decode("utf-8", "replace")))
    d.close()
    return hits


def overlay(path, dpi, out_prefix):
    """Render the bleed pages and draw trim (0.125in) and safe (0.25in) boxes."""
    d = pymupdf.open(path)
    outs = []
    for i in range(d.page_count):
        pm = d.load_page(i).get_pixmap(dpi=dpi)
        img = Image.frombytes("RGB", (pm.width, pm.height), pm.samples).convert("RGB")
        dr = ImageDraw.Draw(img)
        t = 0.125 * dpi
        s = 0.25 * dpi
        w, h = img.size
        dr.rectangle([t, t, w - t - 1, h - t - 1], outline=(255, 0, 0), width=max(2, dpi // 200))
        dr.rectangle([s, s, w - s - 1, h - s - 1], outline=(0, 170, 255), width=max(1, dpi // 400))
        p = f"{out_prefix}-p{i+1}.png"
        img.save(p)
        outs.append(p)
    d.close()
    return outs


if __name__ == "__main__":
    to_pdf("card-FINAL.html", "card-bleed-3.75x2.25.pdf")
    trim_from_bleed("card-bleed-3.75x2.25.pdf", "card-trim-3.5x2.pdf")
    outline("card-bleed-3.75x2.25.pdf", "card-bleed-3.75x2.25-OUTLINED.pdf")
    outline("card-trim-3.5x2.pdf", "card-trim-3.5x2-OUTLINED.pdf")

    print("\n--- fonts in bleed PDF (must all be Type0 with an embedded ext) ---")
    for r in check_fonts("card-bleed-3.75x2.25.pdf"):
        print("  page", r[0], "ext=", r[1], "type=", r[2], "base=", r[3])
    print("\n--- fonts in trim PDF ---")
    for r in check_fonts("card-trim-3.5x2.pdf"):
        print("  page", r[0], "ext=", r[1], "type=", r[2], "base=", r[3])
    print("\n--- fonts in OUTLINED files (must be empty) ---")
    print("  bleed:", check_fonts("card-bleed-3.75x2.25-OUTLINED.pdf"))
    print("  trim :", check_fonts("card-trim-3.5x2-OUTLINED.pdf"))

    print("\n--- QR decode out of the final PDFs ---")
    for f in ["card-bleed-3.75x2.25.pdf", "card-trim-3.5x2.pdf",
              "card-trim-3.5x2-OUTLINED.pdf"]:
        for dpi in (300, 600, 1200):
            h = check_qr(f, dpi)
            print(f"  {f} @{dpi}: {'OK ' + repr(h[0][2][:44]) if h else 'FAIL'}")
            if h:
                break

    print("\n--- trim overlay at 400dpi ---")
    print(" ", overlay("card-bleed-3.75x2.25.pdf", 400, "verify-trim"))
