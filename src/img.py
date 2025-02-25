from PIL import Image as pl
from typing import Self
from pixel import Pixel
import math as m


class Image:
    path: str = ""  # path to current image
    image: pl.Image  # loaded image to use dithering
    index: tuple[int, int]

    def __init__(self, path: str | None, image: pl.Image | None = None) -> None:
        """Creates the initial `Image` object given a relative path

        :param `path`: path to the original image (png, jpg, whatever
        :param `image`: a PIL image, optional"""

        self.index = (0, 0)  # init index to beginning of image
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

    def __next__(self) -> Pixel:
        """Increments the tracked index, which points to a new pixel inside image,
        raises `StopIteration` if the tracked index passes final dimensions of image"""
        width = self.image.width - 1
        height = self.image.height - 1

        if self.index[0] >= width and self.index[1] >= height:
            raise StopIteration
        prev = self.index
        if self.index[0] < width:
            self.index = (prev[0] + 1, prev[1])
            return self.get_pixel((self.index[0], self.index[1]))
        else:
            self.index = (0, prev[1] + 1)
            return self.get_pixel((self.index[0], self.index[1]))

    def get_index(self) -> tuple[int, int]:
        return self.index

    def get_pixel(self, index: tuple[int, int] | None = None) -> Pixel:
        """Gets a pixel from the image,
        either uses the internal index, or custom specified index inside args

        :param `index`: a index that specifies the pixel in a image - (0,0) corresponds to upper right,
        optional arg
        """
        if index == None:
            return Pixel.from_tuple(self.image.getpixel(self.index))
        else:
            return Pixel.from_tuple(self.image.getpixel(index))

    def get_brightness(self, index: tuple[int, int] | None = None) -> float:
        """Get brightness of current pixel, optionally uses a specified index

        :param `index`: a index that specifies the pixel in a image - (0,0) corresponds to upper right,
        optional arg
        """
        if index == None:
            pixel = self.image.getpixel(self.index)  # get pixel using track index
            return m.sqrt(pixel[0] ^ 2 + pixel[1] ^ 2 + pixel[3] ^ 3)
        else:
            pixel = self.image.getpixel(
                index
            )  # get pixel using index specified in args
            return m.sqrt(pixel[0] ^ 2 + pixel[1] ^ 2 + pixel[3] ^ 3)

    def put_pixel(self, pixel: Pixel, index: tuple[int, int] | None = None):
        """Puts a pixel into the image, either using the index tracked inside `self.index`or a
        optionally specified other index as a parameter

        :param `index`: a index that specifies the pixel in a image - (0,0) corresponds to upper right,
        optional arg
        :param `pixel`: tuple that represents an standard rgb pixel
        """
        if index == None:
            self.image.putpixel(self.index, pixel.to_tuple())
        else:
            self.image.putpixel(index, pixel.to_tuple())

    def r_open(self) -> pl.Image:
        """Returns underlying PIL image, which will be used in
        the dithering algorithm"""
        return pl.open(self.path)

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
            # weighted average of rgb channel content that biases green values
            # source :https://en.wikipedia.org/wiki/Grayscale
            gray_scale = int(0.2989 * pixel.r + 0.5870 * pixel.g + 0.1140 * pixel.b)
            # replace pixel w/ new gray scale value
            gray = Pixel(gray_scale, gray_scale, gray_scale)
            i.put_pixel(gray)
        return i  # return grayscaled image back

    def quantize_image(self, palette: list[Pixel]) -> "Image":
        """quantize the image given as set number of pixel/colors
        given by a list of pixels, `palette`

        :param `palette`: a list of colors that can represent the original pixel"""
        i = self  # copy over image
        for pixel in i:
            np = pixel.quantize(palette)
            i.put_pixel(np)  # put pixel using tracked index
            # quantize entire image by using pixel quantization
            # method across the entire image
        return i

    def save(self, path: str | None = None):
        """Util function that will save the image back to
        the file given some path-like string `path`

        :param `img`: Image object that contains path info
        :param `path`: optional path that overides any stored path
        info inside the Image"""
        if path == None:
            if self.path != None:
                self.path = self.path.replace("input", "output")
                self.image.save(self.path)
                print(f"New image saved at: {self.path}")
            else:
                print("Could not save image, no path exists!")
        else:
            self.image.save(path)
            print(f"New image saved at: {path}")
