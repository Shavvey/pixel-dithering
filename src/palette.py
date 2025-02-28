from PIL import Image
from PIL.ImagePalette import ImagePalette
from pixel import Pixel
type Palette = list[Pixel]
# some palettes I think are interesting
SEA_MOSS: Palette = [Pixel(221, 235, 157), 
                     Pixel(160, 200, 120), 
                     Pixel(39, 102, 123), 
                     Pixel(20, 61, 96), 
                     Pixel(0,0,0)]

PASTEL: Palette = [Pixel(70, 53, 177), 
                   Pixel(183, 113, 229),
                   Pixel(174, 234, 148), 
                   Pixel(255, 251, 202), 
                   Pixel(0,0,0)]

WINTER: Palette = [Pixel(255, 242, 242), 
                   Pixel(169, 181, 223),
                   Pixel(120, 134, 199), 
                   Pixel(45, 51, 107)]

BLACK_WHITE: Palette = [Pixel(255,255,255), 
                        Pixel(0,0,0)]

RUST: Palette = [Pixel(241, 240, 233),
                 Pixel(65, 100, 74), 
                 Pixel(13, 71, 21), 
                 Pixel(233, 118, 43)]

HELLO_KITTY: Palette = [Pixel(245, 245, 245),
                        Pixel(248, 231, 246),
                        Pixel(221, 136, 207),
                        Pixel(75, 22, 76)]

def show_palette_sample(p: Palette):
    pass
    
