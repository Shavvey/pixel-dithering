from img import Image
from dither.bayer import Bayer, bayer
from palette import HELLO_KITTY, RUST, WINTER


def main():
    """Main method"""
    i = Image("images/input/IMG_8814.jpg")
    bi = bayer(Bayer(1), i, RUST)
    bi.show()


if __name__ == "__main__":
    main()  # call the main method if this is the main file
