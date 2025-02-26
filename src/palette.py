from pixel import Pixel
type Palette = list[Pixel]
# some palettes I think are interesting
SEA_MOSS: Palette = [Pixel(221, 235, 157), Pixel(160, 200, 120), 
                         Pixel(39, 102, 123), Pixel(20, 61, 96), Pixel(0,0,0)]
PASTEL: Palette = [Pixel(70, 53, 177), Pixel(183, 113, 229),
                   Pixel(174, 234, 148), Pixel(255, 251, 202), Pixel(0,0,0)]

WINTER: Palette = [Pixel(255, 242, 242), Pixel(169, 181, 223),
                   Pixel(120, 134, 199), Pixel(45, 51, 107)]
BLACK_WHITE: Palette = [Pixel(255,255,255), Pixel(0,0,0)]
def show_palette_sample(p: Palette):
    pass
    
