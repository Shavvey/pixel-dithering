import math as m

# alias the type pixel as just a 3-tuple of rgb values
type Pixel = tuple[int, int, int] 
def distance(a, b: "Pixel") -> float:
    # defined a euclidean distance to using pythagorean theorem
    # this is used for quantization methods (where a pixel values are collapse into a smaller set)
    return m.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)

BLACK: Pixel = (0,0,0)
WHITE: Pixel = (255,255,255)
RED: Pixel = (255,0,0)
GREEN: Pixel = (0,255,0)
BLUE: Pixel = (0,0,255)
# careful! depending on the color space used,
# the colors do not scale linearly, that is a exact
# 50,50,50 mix of rgb values is not always a perfect 
# - what would be intutively expected

#TODO: create a linear conversion to sRGB??
