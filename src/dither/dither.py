from dither.random_noise import random_noise
from dtype import DitherType
from img import Image


def dither(img: Image, type: DitherType = DitherType.Default) -> Image:
    """Wrapper method that decodes `type` and applies dither method"""
    match type:
        case DitherType.Default:
            return random_noise(img)
        case _:
            print(f"[ERROR]: Could not match dither type: {type}")
            return img
