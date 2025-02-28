from img import Image
from dither.bayer import Bayer, bayer
from palette import HELLO_KITTY, RUST


def main():
    """Main method"""
    i = Image("images/input/example2.jpg")
    bi = bayer(Bayer(1), i, HELLO_KITTY)
    bi.show()


if __name__ == "__main__":
    main()  # call the main method if this is the main file
