from img import Image
from dither.dither import dither
from dtype import DitherType


def main():
    """Main method"""
    i = Image("images/input/example2.jpg")  # create image from file path
    dither(i, DitherType.Default).show()


if __name__ == "__main__":
    main()  # call the main method if this is the main file
