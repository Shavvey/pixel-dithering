from PIL import Image as pl
from dtype import DitherType
from typing import Self


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
        return self

    def __next__(self) -> Self:
        if (
            self.index[0] >= self.image.width - 1
            and self.index[1] >= self.image.height - 1
        ):
            raise StopIteration
        prev = self.index
        if self.index[0] < self.image.width - 1:
            self.index = (prev[0] + 1, prev[1])
            return self
        else:
            self.index = (0, prev[1] + 1)
        return self

    def get_pixel(self) -> tuple[int, int, int]:
        return self.image.getpixel(self.index)

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

    def show(self, name: str | None) -> None:
        """Simple method to show resulting image,
        uses an option `name` to name the window of the image"""
        self.image.show(name)

    def grayscale(self) -> pl.Image:
        """Provides a simple grayscale operation to a given image"""
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
        # save new image
        return i

    def test(self):
        for pixel in self:
            print(pixel.get_pixel())
