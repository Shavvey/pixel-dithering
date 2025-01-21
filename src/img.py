from PIL import Image as pl
from dtype import DitherType
from typing import Self
import math as m


class Image:
    path: str = ""  # path to current image
    image: pl.Image  # loaded image to use dithering
    index: tuple[int, int]

    def __init__(self, path: str, image: pl.Image | None = None) -> None:
        """Creates the initial `Image` object given a relative path"""
        self.path = path
        self.index = (0, 0)  # init index to begginning of image
        if image != None:
            self.image = image
        else:
            self.image = pl.open(path)

    def __iter__(self) -> Self:
        self.index = (0, 0)  # calling next which advance the index,
        # which will point to a different pixel inside the image
        return self

    def __next__(self) -> Self:
        width = self.image.width - 1
        height = self.image.height - 1

        if self.index[0] >= width and self.index[1] >= height:
            raise StopIteration
        prev = self.index
        if self.index[0] < width:
            self.index = (prev[0] + 1, prev[1])
            return self
        else:
            self.index = (0, prev[1] + 1)
        return self

    def get_pixel(self, index: tuple[int, int] | None = None) -> tuple[int, int, int]:
        """Gets a pixel from the image,
        either uses the internal index, or custom specified index inside args"""
        if index == None:
            return self.image.getpixel(self.index)
        else:
            return self.image.getpixel(index)

    def get_brightness(self, index: tuple[int, int] | None = None) -> float:
        """Get brightness of current pixel, optionally uses a specified index"""
        if index == None:
            pixel = self.image.getpixel(self.index)
            return m.sqrt(pixel[0] ^ 2 + pixel[1] ^ 2 + pixel[3] ^ 3)
        else:
            pixel = self.image.getpixel(index)
            return m.sqrt(pixel[0] ^ 2 + pixel[1] ^ 2 + pixel[3] ^ 3)

    def put_pixel(
        self, pixel: tuple[int, int, int], index: tuple[int, int] | None = None
    ):
        """Puts a pixel into the image, either using the index tracked inside `self.index` our a
        optionally specified other index"""
        if index == None:
            self.image.putpixel(self.index, pixel)
        else:
            self.image.putpixel(index, pixel)

    def r_open(self) -> pl.Image:
        """Returns undeerlying PIL image, which will be used in
        the dithering algorithm"""
        return pl.open(self.path)

    def dither(self, type: DitherType | None):
        """apply a dither to the image given an algorithm
        that should be specified using `DitherType`"""
        if type == None:
            # call default dither algorithm (i dont have one yet!)
            pass
        match type:
            case Bayer:
                pass

    def show(self, name: str | None = None) -> None:
        """Simple method to show resulting image,
        uses an option `name` to name the window of the image"""
        self.image.show(name)

    def to_grayscale(self) -> "Image":
        """Provides a copied image that is grayscale"""
        with self.r_open() as i:
            for x in range(i.width):
                for y in range(i.height):
                    pixel = i.getpixel((x, y))
                    gray = int(
                        0.2989 * pixel[0] + 0.5870 * pixel[1] + 0.1140 * pixel[2]
                    )
                    grayscale_pixel = (gray, gray, gray)
                    i.putpixel(
                        (x, y), grayscale_pixel
                    )  # put grayscale version of pixel into image
        # return back image
        return Image(self.path, i)

    def make_grayscale(self):
        """Overwrites underlying image to grayscale"""
        for pixel in self:
            p = pixel.get_pixel()
            gray = int(0.2989 * p[0] + 0.5870 * p[1] + 0.1140 * p[2])
            pixel.put_pixel((gray, gray, gray))
