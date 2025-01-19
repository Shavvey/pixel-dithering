from enum import Enum


class DitherType(Enum):
    """Responsible for providing
    the different types of diterhing algorithms
    available for use
    `Bayer`: a bayer algorithm for pixel dithering, uses grayscale image
    """

    Default = 1
    Bayer = 2
