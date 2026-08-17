# Pencil wordmark, handoff spec

Everything needed to put the `Pencil.` wordmark on the site. Files are attached alongside this,
and the SVG source is inlined below so it can be pasted straight into HTML.

## What it is

The word **Pencil** in **Inter Tight, weight 800**, letter-spacing **-0.012em**, followed by a
period in **gold `#C08A2D`**. The gold period is the whole point of the mark. It is the same
lockup used on the back of the business card, so the card and the site match.

## Colors

| Part | Light background | Dark background |
|---|---|---|
| "Pencil" | ink navy `#0E1B2A` | white `#FFFFFF` |
| the period | gold `#C08A2D` | gold `#C08A2D` |

The gold does NOT change between light and dark. It is the constant.

## Files

| File | Use |
|---|---|
| `pencil-wordmark.svg` | **preferred.** Navy, transparent, outlined paths, scales to any size |
| `pencil-wordmark-white.svg` | white version for dark/navy backgrounds |
| `pencil-wordmark-2400.png` | navy, transparent, 2400x625, if a raster is required |
| `pencil-wordmark-white-2400.png` | white, transparent, 2400x625 |
| `pencil-wordmark-800.png` / `-white-800.png` | smaller rasters, same aspect |

**Use the SVG on the website.** Both PNGs are there only for places that cannot take vector,
such as an email signature or a social profile. The text in the SVG is converted to outlines,
so it does not depend on Inter Tight being installed or loaded and it cannot reflow.

## Geometry

viewBox is `0 0 6182.5 1609.0`, aspect ratio **3.8425 : 1**, cropped tight to the ink with
zero padding. Set a width and let the height follow, or the reverse. Do not stretch it.

    width  = height x 3.8425
    height = width  / 3.8425

Because the box is tight to the ink, any breathing room around the mark should come from CSS
margin or padding, not from the file. A good starting point is clear space on all sides equal
to the height of the period.

## Dropping it in

Inline, which is best because the colors stay themeable and it costs no extra request:

```html
<a href="/" class="wordmark" aria-label="Pencil home">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 6182.5 1609.0" role="img" aria-label="Pencil">
    <title>Pencil</title>
    <g transform="translate(-84.0, 1587.0)">
      <path d="M84 0V-1490H698Q866 -1490 988.0 -1425.0Q1110 -1360 1176.5 -1243.5Q1243 -1127 1243 -973Q1243 -819 1175.5 -704.0Q1108 -589 983.0 -525.5Q858 -462 688 -462H308V-746H621Q702 -746 757.5 -774.5Q813 -803 841.5 -854.0Q870 -905 870 -973Q870 -1043 841.5 -1093.5Q813 -1144 757.5 -1171.5Q702 -1199 620 -1199H443V0Z" fill="#0E1B2A"/>
      <path d="M1839.424 21Q1663.424 21 1536.424 -48.5Q1409.424 -118 1341.924 -247.0Q1274.424 -376 1274.424 -555Q1274.424 -728 1342.424 -857.5Q1410.424 -987 1534.424 -1059.5Q1658.424 -1132 1826.424 -1132Q1945.424 -1132 2044.924 -1094.5Q2144.424 -1057 2216.924 -984.5Q2289.424 -912 2328.924 -806.0Q2368.424 -700 2368.424 -561V-473H1397.424V-678H2199.424L2033.424 -630Q2033.424 -707 2010.424 -761.5Q1987.424 -816 1942.424 -846.0Q1897.424 -876 1830.424 -876Q1763.424 -876 1717.424 -846.0Q1671.424 -816 1647.424 -762.5Q1623.424 -709 1623.424 -636V-489Q1623.424 -411 1650.924 -354.0Q1678.424 -297 1728.924 -266.5Q1779.424 -236 1845.424 -236Q1891.424 -236 1929.424 -249.0Q1967.424 -262 1994.424 -287.5Q2021.424 -313 2035.424 -349L2361.424 -340Q2341.424 -230 2273.424 -149.0Q2205.424 -68 2095.424 -23.5Q1985.424 21 1839.424 21Z" fill="#0E1B2A"/>
      <path d="M2821.848 -637V0H2465.848V-1118H2817.848V-912H2826.848Q2864.848 -1014 2948.348 -1073.0Q3031.848 -1132 3155.848 -1132Q3273.848 -1132 3360.848 -1079.5Q3447.848 -1027 3495.848 -932.5Q3543.848 -838 3543.848 -712V0H3187.848V-642Q3187.848 -735 3140.848 -787.5Q3093.848 -840 3008.848 -840Q2952.848 -840 2910.848 -816.0Q2868.848 -792 2845.348 -746.5Q2821.848 -701 2821.848 -637Z" fill="#0E1B2A"/>
      <path d="M4208.272 21Q4031.272 21 3905.272 -52.0Q3779.272 -125 3712.272 -254.5Q3645.272 -384 3645.272 -555Q3645.272 -727 3712.272 -856.5Q3779.272 -986 3905.772 -1059.0Q4032.272 -1132 4208.272 -1132Q4363.272 -1132 4478.272 -1075.5Q4593.272 -1019 4658.272 -917.5Q4723.272 -816 4727.272 -678H4395.272Q4388.272 -735 4364.772 -776.0Q4341.272 -817 4302.772 -839.0Q4264.272 -861 4213.272 -861Q4151.272 -861 4104.772 -826.5Q4058.272 -792 4032.772 -724.5Q4007.272 -657 4007.272 -558Q4007.272 -459 4032.772 -390.5Q4058.272 -322 4104.272 -286.0Q4150.272 -250 4213.272 -250Q4286.272 -250 4335.272 -299.5Q4384.272 -349 4395.272 -438H4727.272Q4722.272 -300 4658.272 -196.5Q4594.272 -93 4480.272 -36.0Q4366.272 21 4208.272 21Z" fill="#0E1B2A"/>
      <path d="M4825.696 0V-1118H5181.696V0ZM5002.696 -1246Q4927.696 -1246 4873.696 -1296.0Q4819.696 -1346 4819.696 -1417Q4819.696 -1488 4873.696 -1537.5Q4927.696 -1587 5002.696 -1587Q5078.696 -1587 5132.196 -1537.5Q5185.696 -1488 5185.696 -1417Q5185.696 -1346 5132.196 -1296.0Q5078.696 -1246 5002.696 -1246Z" fill="#0E1B2A"/>
      <path d="M5681.12 -1490V0H5325.12V-1490Z" fill="#0E1B2A"/>
      <path d="M6075.544 22Q5994.544 22 5939.544 -32.5Q5884.544 -87 5884.544 -167Q5884.544 -247 5939.544 -301.5Q5994.544 -356 6075.544 -356Q6156.544 -356 6211.544 -301.5Q6266.544 -247 6266.544 -167Q6266.544 -87 6211.544 -32.5Q6156.544 22 6075.544 22Z" fill="#C08A2D"/>
    </g>
  </svg>
</a>
```

```css
.wordmark svg { height: 28px; width: auto; display: block; }
```

As a file:

```html
<img src="/pencil-wordmark.svg" alt="Pencil" width="108" height="28">
```

**Deployment note if you use the file form.** In the `thedurdencompany-site` repo, copies of these
files live in `brand-source/`, but that folder is listed in `.assetsignore`, so Cloudflare Pages
does not publish anything inside it. To serve the SVG at `/pencil-wordmark.svg`, copy it to the
**repo root**. Inlining the SVG avoids this entirely and is the recommended route.

## If it has to be live text instead of the SVG

Only do this if the wordmark must be selectable. It needs the Inter Tight webfont at weight 800,
and it will shift slightly if the font fails to load.

```html
<span class="wordmark-text">Pencil<span class="dot">.</span></span>
```

```css
.wordmark-text {
  font-family: "Inter Tight", system-ui, sans-serif;
  font-weight: 800;
  letter-spacing: -0.012em;
  color: #0E1B2A;
}
.wordmark-text .dot { color: #C08A2D; }
```

Font source, the exact one used to build these files:
`npm i @fontsource/inter-tight` then `@fontsource/inter-tight/800.css`.

## White version, inline

```html
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 6182.5 1609.0" role="img" aria-label="Pencil">
  <title>Pencil</title>
  <g transform="translate(-84.0, 1587.0)">
    <path d="M84 0V-1490H698Q866 -1490 988.0 -1425.0Q1110 -1360 1176.5 -1243.5Q1243 -1127 1243 -973Q1243 -819 1175.5 -704.0Q1108 -589 983.0 -525.5Q858 -462 688 -462H308V-746H621Q702 -746 757.5 -774.5Q813 -803 841.5 -854.0Q870 -905 870 -973Q870 -1043 841.5 -1093.5Q813 -1144 757.5 -1171.5Q702 -1199 620 -1199H443V0Z" fill="#FFFFFF"/>
    <path d="M1839.424 21Q1663.424 21 1536.424 -48.5Q1409.424 -118 1341.924 -247.0Q1274.424 -376 1274.424 -555Q1274.424 -728 1342.424 -857.5Q1410.424 -987 1534.424 -1059.5Q1658.424 -1132 1826.424 -1132Q1945.424 -1132 2044.924 -1094.5Q2144.424 -1057 2216.924 -984.5Q2289.424 -912 2328.924 -806.0Q2368.424 -700 2368.424 -561V-473H1397.424V-678H2199.424L2033.424 -630Q2033.424 -707 2010.424 -761.5Q1987.424 -816 1942.424 -846.0Q1897.424 -876 1830.424 -876Q1763.424 -876 1717.424 -846.0Q1671.424 -816 1647.424 -762.5Q1623.424 -709 1623.424 -636V-489Q1623.424 -411 1650.924 -354.0Q1678.424 -297 1728.924 -266.5Q1779.424 -236 1845.424 -236Q1891.424 -236 1929.424 -249.0Q1967.424 -262 1994.424 -287.5Q2021.424 -313 2035.424 -349L2361.424 -340Q2341.424 -230 2273.424 -149.0Q2205.424 -68 2095.424 -23.5Q1985.424 21 1839.424 21Z" fill="#FFFFFF"/>
    <path d="M2821.848 -637V0H2465.848V-1118H2817.848V-912H2826.848Q2864.848 -1014 2948.348 -1073.0Q3031.848 -1132 3155.848 -1132Q3273.848 -1132 3360.848 -1079.5Q3447.848 -1027 3495.848 -932.5Q3543.848 -838 3543.848 -712V0H3187.848V-642Q3187.848 -735 3140.848 -787.5Q3093.848 -840 3008.848 -840Q2952.848 -840 2910.848 -816.0Q2868.848 -792 2845.348 -746.5Q2821.848 -701 2821.848 -637Z" fill="#FFFFFF"/>
    <path d="M4208.272 21Q4031.272 21 3905.272 -52.0Q3779.272 -125 3712.272 -254.5Q3645.272 -384 3645.272 -555Q3645.272 -727 3712.272 -856.5Q3779.272 -986 3905.772 -1059.0Q4032.272 -1132 4208.272 -1132Q4363.272 -1132 4478.272 -1075.5Q4593.272 -1019 4658.272 -917.5Q4723.272 -816 4727.272 -678H4395.272Q4388.272 -735 4364.772 -776.0Q4341.272 -817 4302.772 -839.0Q4264.272 -861 4213.272 -861Q4151.272 -861 4104.772 -826.5Q4058.272 -792 4032.772 -724.5Q4007.272 -657 4007.272 -558Q4007.272 -459 4032.772 -390.5Q4058.272 -322 4104.272 -286.0Q4150.272 -250 4213.272 -250Q4286.272 -250 4335.272 -299.5Q4384.272 -349 4395.272 -438H4727.272Q4722.272 -300 4658.272 -196.5Q4594.272 -93 4480.272 -36.0Q4366.272 21 4208.272 21Z" fill="#FFFFFF"/>
    <path d="M4825.696 0V-1118H5181.696V0ZM5002.696 -1246Q4927.696 -1246 4873.696 -1296.0Q4819.696 -1346 4819.696 -1417Q4819.696 -1488 4873.696 -1537.5Q4927.696 -1587 5002.696 -1587Q5078.696 -1587 5132.196 -1537.5Q5185.696 -1488 5185.696 -1417Q5185.696 -1346 5132.196 -1296.0Q5078.696 -1246 5002.696 -1246Z" fill="#FFFFFF"/>
    <path d="M5681.12 -1490V0H5325.12V-1490Z" fill="#FFFFFF"/>
    <path d="M6075.544 22Q5994.544 22 5939.544 -32.5Q5884.544 -87 5884.544 -167Q5884.544 -247 5939.544 -301.5Q5994.544 -356 6075.544 -356Q6156.544 -356 6211.544 -301.5Q6266.544 -247 6266.544 -167Q6266.544 -87 6211.544 -32.5Q6156.544 22 6075.544 22Z" fill="#C08A2D"/>
  </g>
</svg>
```

## Do not

- Do not recolor the period. The gold is the mark.
- Do not add a stroke, shadow, gradient or outline.
- Do not stretch. Lock the 3.8425:1 aspect.
- Do not rebuild it from a variable font. These were built from a static Inter Tight 800 and
  converted to outlines on purpose.
