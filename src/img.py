from PIL import Image as pl
from dtype import DitherType
from typing import Self
from pixel import Pixel, distance
import math as m


class Image:
    path: str = ""  # path to current image
    image: pl.Image  # loaded image to use dithering
    index: tuple[int, int]

    def __init__(self, path: str | None, image: pl.Image | None = None) -> None:
        """Creates the initial `Image` object given a relative path

        :param `path`: path to the original image (png, jpg, whatever
        :param `image`: a PIL image, optional"""

        self.index = (0, 0)  # init index to begginning of image
        if image != None:
            self.image = image
        elif path != None:
            self.path = path
            self.image = pl.open(path)

    def __iter__(self) -> Self:
        """Used a tracked index to return pixels inside image"""
        self.index = (0, 0)  # calling next which advance the index,
        # which will point to a different pixel inside the image
        return self

    def __next__(self) -> Self:
        """Increments the tracked index, which points to a new pixel inside image,
        raises `StopIteration` if the tracked index passes final dimensions of image"""
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

    def get_pixel(self, index: tuple[int, int] | None = None) -> Pixel:
        """Gets a pixel from the image,
        either uses the internal index, or custom specified index inside args

        :param `index`: a index that specifies the pixel in a image - (0,0) corresponds to upper right,
        optional arg
        """
        if index == None:
            return self.image.getpixel(self.index)
        else:
            return self.image.getpixel(index)

    def get_brightness(self, index: tuple[int, int] | None = None) -> float:
        """Get brightness of current pixel, optionally uses a specified index

        :param `index`: a index that specifies the pixel in a image - (0,0) corresponds to upper right,
        optional arg
        """
        if index == None:
            pixel = self.image.getpixel(self.index)
            return m.sqrt(pixel[0] ^ 2 + pixel[1] ^ 2 + pixel[3] ^ 3)
        else:
            pixel = self.image.getpixel(index)
            return m.sqrt(pixel[0] ^ 2 + pixel[1] ^ 2 + pixel[3] ^ 3)

    def put_pixel(self, pixel: Pixel, index: tuple[int, int] | None = None):
        """Puts a pixel into the image, either using the index tracked inside `self.index`or a
        optionally specified other index as a parameter

        :param `index`: a index that specifies the pixel in a image - (0,0) corresponds to upper right,
        optional arg
        :param `pixel`: tuple that represents an standard rgb pixel
        """
        if index == None:
            self.image.putpixel(self.index, pixel)
        else:
            self.image.putpixel(index, pixel)

    def r_open(self) -> pl.Image:
        """Returns undeerlying PIL image, which will be used in
        the dithering algorithm"""
        return pl.open(self.path)

    def dither(self, type: DitherType = DitherType.Default):
        """apply a dither to the image given an algorithm
        that should be specified using `DitherType`

        :param `type`: a enumeration type that specifies the type
        of dithering algorithms that are available to the image"""
        match type:
            case DitherType.Default:
                pass
            case DitherType.Bayer:
                pass
            case _:  # wildcard default case
                print("[ERROR]: Couldn't parse DitherType")

    def show(self, name: str | None = None):
        """Simple method to show resulting image,
        uses an option `name` to name the window of the image

        :param `name`: the name of the image window being created, optional argument
        that is `None` by default"""
        self.image.show(name)

    def to_grayscale(self) -> "Image":
        """Provides a copy of the image to with an applied grayscale"""
        # duplicate image pixel content
        i = Image(None, self.image)
        for pixel in i:
            p = pixel.get_pixel()
            # weighted average of rgb channel content that biases green
            gray_scale = int(0.2989 * p[0] + 0.5870 * p[1] + 0.1140 * p[2])
            # replace pixel w/ new gray scale value
            pixel.put_pixel((gray_scale, gray_scale, gray_scale))
        return i  # return grayscaled image back

    def to_quantize(self, palette: list[Pixel]) -> "Image":
        """quantize the image given as set number of pixel/colors
        given by a list of pixels, `palette`

        :param `palette`: a list of colors that can represent the original pixel"""
        i = Image(None, self.image)
        for image_pixel in i:
            pixel: Pixel = (0, 0, 0)
            min: float = 1000.0  # pick a pixel such that the
            # euclidean distance between palette pixel and original pixel is minimized
            p = image_pixel.get_pixel()
            for palette_color in palette:
                d = distance(p, palette_color)
                if d < min:
                    min = d  # make distance new min
                    pixel = palette_color  # save palette color as new pixel
            # print(f"New min distance: {min}")
            image_pixel.put_pixel(pixel)
        return i
