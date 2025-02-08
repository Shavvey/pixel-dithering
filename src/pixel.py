import math as m


class Pixel:
    def distance(self, other: "Pixel") -> float:
        return m.sqrt(
            (self.r - other.r) ** 2 + (self.g - other.g) ** 2 + (self.b - other.b) ** 2
        )

    def __init__(self, r: int, g: int, b: int) -> None:
        self.r = r
        self.g = g
        self.b = b

    def to_tuple(self) -> tuple[int, int, int]:
        return (self.r, self.b, self.g)


BLACK = Pixel(0, 0, 0)
WHITE = Pixel(255, 255, 255)
RED = Pixel(255, 0, 0)
GREEN = Pixel(0, 255, 0)
BLUE = Pixel(0, 0, 255)
# careful! depending on the color space used,
# the colors do not scale linearly, that is a exact
# 50,50,50 mix of rgb values is not always a perfect
# - what would be intutively expected

# TODO: create a linear conversion to sRGB??
