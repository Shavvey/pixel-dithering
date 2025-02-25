from img import Image
from matrix import Matrix
from pixel import WHITE, BLACK


def mult_plus_sum(a: int, b: int, n: int) -> int:
    """A recursive sum of an expression of the form a*n + b,
    where `a` is the multiplication term, and `b` is the plus term"""
    if n == 0:
        return 0
    else:
        return a * mult_plus_sum(a, b, n - 1) + b


class Bayer:
    matrix: Matrix = Matrix([[0, 0], [0, 0]])

    def __init__(self, level: int) -> None:
        """Create a Bayer matrix which an associated level"""
        self.matrix = self.make_bayer(level)

    def make_bayer(self, level: int) -> Matrix:
        """Helper function to recursivley compute the each row and column
        of the Bayer matrix, up to a certain level

        :param `level`: the associated level of the Bayer matrix"""
        a00 = mult_plus_sum(4, 0, level) * (1 / 4**level)
        a01 = mult_plus_sum(4, 2, level) * (1 / 4**level)
        a10 = mult_plus_sum(4, 3, level) * (1 / 4**level)
        a11 = mult_plus_sum(4, 1, level) * (1 / 4**level)
        return Matrix([[a00, a01], [a10, a11]])


def bayer(bayer: Bayer, img: Image) -> Image:
    """Dithering algorithm that uses a Bayer matrix

    from Wikipedia, we would like to do somehting like this:
    c' = palette_quantize(c + r x M(x mod n, y mod n) - 1/2)
    c': new transformed color
    M: threshold map, bayer matrix in our case
    r: spread in color space (sRGB is not linear, remember?)

    param `bayer`: contructed Bayer matrix, based on different 'levels'
    param `img`: underlying image that we will used for bayer dithering
    """
    i = img
    R = 1
    LEN: int = bayer.matrix.length()  # used later
    # return the closest color, compare brightness levels
    for pixel in i:  # iter through pixel
        index = i.get_index()
        y = index[1] % LEN
        x = index[0] % LEN
        # NOTE: need to create add dunder method
        # pixel = pixel + R * bayer.matrix[x][y]
    return img
