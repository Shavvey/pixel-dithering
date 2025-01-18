from PIL import Image as pl


class Image:
    path: str = ""  # path to current image
    image: pl.Image  # loaded image to use dithering

    def __init__(self, path: str):
        self.path = path
        self.image = pl.open(path)

    def ropen(self):
        pl.open("r", self.path)

    def dither(self) -> pl.Image:
        i = pl.new("RGB", (200, 200), 1)
        return i
