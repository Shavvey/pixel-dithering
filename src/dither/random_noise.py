from img import Image
from pixel import *
import random as r


def random_noise(img: Image, noise: int = 200) -> Image:
    """Uses black-white quantization,
    but will introduce random noise to produce a
    more smoother (and weirder) image

    :param `img`: original image to quantize w/ random noise"""
    palette: list[Pixel] = [BLACK, WHITE]
    i = img
    for image_pixel in i:
        pixel: Pixel = (0, 0, 0)
        min: float = 1000.0  # pick a pixel such that the
        # euclidean distance between palette pixel and original pixel is minimized
        p = image_pixel.get_pixel()
        for palette_color in palette:
            d = distance(p, palette_color) + r.randint(-1 * noise, noise)
            if d < min:
                min = d  # make distance new min
                pixel = palette_color  # save palette color as new pixel
        image_pixel.put_pixel(pixel)
    return i
