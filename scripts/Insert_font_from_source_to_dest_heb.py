from fontTools.ttLib import TTFont
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.ttGlyphPen import TTGlyphPen

HEBREW_START = 0x0590
HEBREW_END = 0x05FF
SCALE = 2  # Adjust this factor for desired size

font1 = TTFont(r"C:\Users\yaari\Downloads\Varela_Round\Varela_Round\font1.ttf")
font2 = TTFont(r"C:\Users\yaari\Downloads\Varela_Round\Varela_Round\font2.ttf")

cmap1 = font1.getBestCmap()
hebrew_glyphs = [(code, glyph) for code, glyph in cmap1.items() if HEBREW_START <= code <= HEBREW_END]
glyf2 = font2['glyf']
hmtx2 = font2['hmtx']
cmap2_tables = [t for t in font2['cmap'].tables if t.isUnicode()]
glyph_order2 = font2.getGlyphOrder()
glyph_set1 = font1.getGlyphSet()

for code, glyph_name in hebrew_glyphs:
    if glyph_name not in glyf2.glyphs:
        glyph = glyph_set1[glyph_name]
        pen = TTGlyphPen(font2.getGlyphSet())
        transform_pen = TransformPen(pen, (SCALE, 0, 0, SCALE, 0, 0))
        glyph.draw(transform_pen)
        glyf2.glyphs[glyph_name] = pen.glyph()
        # Scale advance width and left side bearing
        if glyph_name in font1['hmtx'].metrics:
            width, lsb = font1['hmtx'].metrics[glyph_name]
            hmtx2.metrics[glyph_name] = (int(width * SCALE), int(lsb * SCALE))
        else:
            hmtx2.metrics[glyph_name] = (500, 0)
        if glyph_name not in glyph_order2:
            glyph_order2.append(glyph_name)
    for cmap_table in cmap2_tables:
        cmap_table.cmap[code] = glyph_name

font2.setGlyphOrder(glyph_order2)
font2.save(r"C:\Users\yaari\Downloads\Varela_Round\Varela_Round\font2_with_hebrew_scaled.ttf")
print("Saved font as 'font2_with_hebrew_scaled.ttf'")
