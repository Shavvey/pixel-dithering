from PIL import Image as pl
from dtype import DitherType


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

    def dither(self, type: DitherType | None):
        """apply a dither to the image given an algorithm
        that should be specified using `DitherType`"""
        if type == None:
            # call default dither algorithm
            pass
        match type:
            case Bayer:
                pass

    def show(self, name: str | None) -> None:
        """Simple method to show resulting image,
        uses an option `name` to name the window of the image"""
        self.image.show(name)

    def grayscale(self):
        with self.w_open() as i:
            for x in range(i.width):
                for y in range(i.height):
                    pixel = i.getpixel((x, y))
                    print(pixel)
