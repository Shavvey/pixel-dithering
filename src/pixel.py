import math as m


type Pixel = tuple[int, int, int] # alias the type pixel as just a 3 memeber tuple with rgb values

def distance(a, b: "Pixel") -> float:
    # defined a euclidean distance to using pythagorean theorem
    # this is used for quantization methods (where a pixel values are collapse into a smaller set)
    return m.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)

BLACK: Pixel = (0,0,0)
WHITE: Pixel = (255,255,255)
