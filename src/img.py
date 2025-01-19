from PIL import Image as pl


class Image:
    path: str = ""  # path to current image
    image: pl.Image  # loaded image to use dithering

    def __init__(self, path: str):
        """Creates the initial `Image` object given a relative path"""
        self.path = path
        self.image = pl.open(path)

    def wopen(self) -> pl.Image:
        """Returns a writable image, which will be used in
        the dithering algorithm"""
        return pl.open("w", self.path)

    def dither(self) -> pl.Image:
        """Modify the image to produce the final dithering result"""
        i = pl.new("RGB", (200, 200), 1)
        return i

    def show(self):
        """Simple method to show resulting image"""
        self.image.show()
