from img import Image

type Matrix = list[list[int]]  # Nx2 matrix type

def mult_plus_sum(a: int, b: int, n: int) -> int:
    """ A recursive sum of an expression of the form a*n + b,
    where a is the multiplication term, and b is the plus term"""
    if n == 0:
       return 0
    else:
        return (a * mult_plus_sum(a, b, n - 1) + b)
    

class Bayer:
    matrix: Matrix = [[0, 0], [0, 0]]
    def __init__(self, level: int) -> None:
        self.matrix = self.make_bayer(level)

    def make_bayer(self, level: int) -> Matrix:
        a00 = mult_plus_sum(4, 0, level)
        a01 = mult_plus_sum(4, 2, level)
        a10 = mult_plus_sum(4, 3, level)
        a11 = mult_plus_sum(4, 1, level)
        return [[a00, a01],
                [a10, a11]]
