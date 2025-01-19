from PIL import Image as pl
from dither import *


class Image:
    path: str = ""  # path to current image
    image: pl.Image  # loaded image to use dithering

    def __init__(self, path: str) -> None:
        """Creates the initial `Image` object given a relative path"""
        self.path = path
        self.image = pl.open(path)

    def w_open(self) -> pl.Image:
        """Returns a writable image, which will be used in
        the dithering algorithm"""
        return pl.open("w", self.path)

    def dither(self, type: DitherType) -> pl.Image:
        """Modify the image to produce the final dithering result"""
        i = pl.new("RGB", (200, 200), 1)
        return i

    def show(self) -> None:
        """Simple method to show resulting image"""
        self.image.show()
