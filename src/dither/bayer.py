from img import Image

type Matrix = list[list[int]]  # Nx2 matrix type

def mult_plus_sum(a: int, b: int, n: int) -> int:
    """ A recursive sum of an expression of the form a*n + b,
    where `a` is the multiplication term, and `b` is the plus term"""
    if n == 0:
       return 0
    else:
        return (a * mult_plus_sum(a, b, n - 1) + b)
    

class Bayer:
    matrix: Matrix = [[0, 0], [0, 0]]
    def __init__(self, level: int) -> None:
        """Create a Bayer matrix which an associated level"""
        self.matrix = self.make_bayer(level)

    def make_bayer(self, level: int) -> Matrix:
        """Helper function to recursivley compute the each row and column
        of the Bayer matrix, up to a certain level

        :param `level`: the associated level of the Bayer matrix"""
        a00 = mult_plus_sum(4, 0, level)
        a01 = mult_plus_sum(4, 2, level)
        a10 = mult_plus_sum(4, 3, level)
        a11 = mult_plus_sum(4, 1, level)
        return [[a00, a01],
                [a10, a11]]

def bayer(bayer: Bayer, img: Image) -> Image:
    """Dithering algorithm that uses a Bayer matrix

    param `bayer`: contructed Bayer matrix, based on different 'levels' 
    param `img`: underlying image that we will used for bayer dithering
    """
    return img
