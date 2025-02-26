import math as m


class Pixel:
    def distance(self, other: "Pixel") -> float:
        """Calculate euclidean distance between two pixel using pythagorean theorem

        :param `other`: other pixel/endpoint to calculate distance to
        """
        return m.sqrt(
            (self.r - other.r) ** 2 + (self.g - other.g) ** 2 + (self.b - other.b) ** 2
        )

    def __init__(self, r: int, g: int, b: int) -> None:
        """Create new instance of pixel class by using rgb values

        :param `r`: red value
        :param `g`: green value
        :param `b`: blue value
        """

        self.r = r
        self.g = g
        self.b = b

    def __str__(self) -> str:
        """Create string representation of pixel 3-tuple value"""
        return f"({self.r},{self.g},{self.b})"

    def __add__(self, i: int) -> "Pixel":
        """Dudner method to quickly add values to pixels"""
        self.r += i
        self.g += i
        self.b += i
        return self

    def get_brightness(self) -> float:
        """Get brightness of an individual pixel via a simple
        euclidean distance, which will determine it's magnitude in
        color space"""

        return m.sqrt(self.r**2 + self.g**2 + self.b**2)

    @staticmethod
    def from_tuple(t: tuple[int, int, int]) -> "Pixel":
        """Create a new pixel from a 3-tuple value

        :param `t`: a 3 memeber tuple to copy the rgb values
        """
        p = Pixel(0, 0, 0)
        p.r = t[0]
        p.g = t[1]
        p.b = t[2]
        return p

    def to_tuple(self) -> tuple[int, int, int]:
        """Simple method to return original tuple value
        that the `Pixel` class is built on top of"""
        return (self.r, self.b, self.g)

    def quantize(self, palette: list["Pixel"]) -> "Pixel":
        pixel = Pixel(0, 0, 0)
        min: float = 10000.0  # find min, init from some large number
        for color in palette:
            d = self.distance(color)  # calc eulcidian distance
            if d < min:
                min = d  # find new min from eulcidian distance
                pixel = color  # save color from min
        return pixel


# CONSTANTS
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
