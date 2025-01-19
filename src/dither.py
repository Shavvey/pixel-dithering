from enum import Enum
from img import Image


class DitherType(Enum):
    """Responsible for providing
    the different types of diterhing algorithms
    available for use"""

    pass


def dither(img: Image):
    with img.w_open() as i:
        pass
