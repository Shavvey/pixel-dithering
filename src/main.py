from img import Image
from pixel import *
import dither.random_noise as r


def main():
    """Main method"""
    i = Image("images/input/example2.jpg")  # create image from file path
    r.random_noise(i).show()


if __name__ == "__main__":
    main()
