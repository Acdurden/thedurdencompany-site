BRAND SOURCE ASSETS, not part of the website
Excluded from deployment by .assetsignore, so nothing in here is published.
Kept in the repo so it survives between Claude sessions and does not need re-uploading.

SOURCE PHOTOS
  durden-cutout-transparent-1200.webp   THE IMPORTANT ONE. Background already removed.
                                        Everything on the card and About page derives from this.
  durden-headshot-4x5-800.webp          tighter head and shoulders, cream background
  durden-headshot-square-800.webp       square crop, cream background
  durden-headshot-original-1200.jpg     original LinkedIn headshot, cream background
  durden-fulllength-1920.webp           highest resolution full length, cream background

DERIVED, used by the card build
  panel-white.jpg          head and shoulders composited on WHITE, the card front photo panel.
                           REBUILT 2026-08-16 to fix the ear crop. 792x1350 at 600dpi,
                           which is exactly 1.32 x 2.25in, the panel size.
  equal-housing.png        Equal Housing house mark, drawn as vector then rasterised
  qr-vcard.png             vCard QR, segno error level M, dark #0E1B2A on white, border 2
  andrew-durden.vcf        the contact record the QR encodes
  newsreader-500-opsz21.ttf  STATIC instance of Newsreader at wght 500 / opsz 21.
                             REQUIRED. Using the variable font makes Chromium write Type 3
                             fonts into the PDF, which Vistaprint rejects as unembedded.

DELIVERED ARTWORK
  card-FRONT/BACK-bleed-3.75x2.25.pdf   outlined, no fonts
  card-FRONT/BACK-trim-3.5x2.pdf        outlined, no fonts
  EAR CROP BUG: FIXED 2026-08-16. The old files had the ear 0.0475in PAST the trim line,
  so the printer cut it off. Measured off the rendered PDF at 800dpi, the current files put
  the ear 0.1437in INSIDE the trim line and the top of the head 0.145in inside. See the
  geometry block below before touching the photo panel again.
  linkedin-headshot-white.jpg           1000x1000, true white background
  tdc-wordmark.svg / -white / -lockup   outlined wordmark, no font dependency
  tdc-wordmark.png                      600px wide, transparent, for email signatures
  andrew-durden.png                     circular headshot, 240px, for email signatures

BUILD
  makepanel.py   builds panel-white.jpg. Solves for the crop instead of guessing at
                 object-position. Run: python3 makepanel.py A
  headgeom.json  the head landmarks measured out of the cutout's alpha channel:
                 head top y=14, chin/neck y=464, head left x=434, ear right x=801.
                 These are source pixel coordinates in durden-cutout-transparent-1200.webp.
  build.py       builds card-FINAL.html from the assets above
  render.py      Chromium to PDF, derives the trim PDF from the bleed PDF by insetting the
                 page box 0.125in on all four sides, outlines both with ghostscript, then
                 verifies fonts, decodes the QR, and writes the 400dpi trim-box overlays
  cards2.py      the older exploratory build script, kept for the rejected variants
  about.html     the About page, built and NOT yet deployed

PHOTO PANEL GEOMETRY, read this before moving the photo
  The bleed page is 3.75 x 2.25in. Trim is 0.125in in from every edge, so the trim box is
  x 0.125..3.625 and y 0.125..2.125. The photo panel is flush right, x 2.43..3.75, 1.32in wide.
  Rule: the ear, which is the rightmost pixel of the head, must land at least 0.125in inside
  the trim line. makepanel.py targets 0.145in. It also holds the top of the head 0.145in
  below the top trim line, and keeps the head's left edge inside the panel so the face is
  not clipped by the panel's hard edge.
  Option A, the one shipped, uses head width 1.030in. Option B at 0.960in was built and not
  chosen. Change the number in makepanel.py, rerun, and re-verify.

  DO NOT judge the crop from the bleed render alone. That is how the bug shipped. Render at
  400dpi or better and draw the trim rectangle, or measure the rightmost non-white pixel of
  the head and subtract it from 3.625.
