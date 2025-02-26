from dither.random_noise import random_noise
from dither.bayer import bayer, Bayer
from dtype import DitherType
from img import Image
from pixel import Pixel, BLACK, WHITE


def dither(
    img: Image,
    palette: list[Pixel] = [BLACK, WHITE],
    type: DitherType = DitherType.Default,
) -> Image:
    """Wrapper method that decodes `type` and applies dither method"""
    match type:
        case DitherType.Default:
            return random_noise(img)
        case DitherType.Bayer:
            return bayer(Bayer(1), img, palette)
        case DitherType.RandomNoise:
            return random_noise(img)
        case _:
            print(f"[ERROR]: Could not match dither type: {type}")
            return img
