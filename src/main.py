from img import Image
from dither.dither import dither
from dtype import DitherType
from dither.bayer import Bayer


def main():
    """Main method"""
    b: Bayer = Bayer(1)
    print(b.matrix)
    print(b.matrix.length())


if __name__ == "__main__":
    main()  # call the main method if this is the main file
