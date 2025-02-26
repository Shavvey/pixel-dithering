from img import Image
from dither.bayer import Bayer, bayer
from palette import PASTEL, SEA_MOSS
from pixel import WHITE, BLACK


def main():
    """Main method"""
    i = Image("images/input/example2.jpg")
    qi = i.quantize_image([WHITE, BLACK])
    i = Image("images/input/example2.jpg")
    bi = bayer(Bayer(1), i, [WHITE, BLACK])
    bi.show()
    qi.show()


if __name__ == "__main__":
    main()  # call the main method if this is the main file
