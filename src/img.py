from PIL import Image as pl


class Image:
    path: str = ""  # path to current image
    image: pl.Image  # loaded image to use dithering
