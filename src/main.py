from img import Image
from dither.bayer import Bayer, bayer
from pixel import BLACK, WHITE


def main():
    """Main method"""
    # b: Bayer = Bayer(1)
    # print(b.matrix)
    # print(b.matrix.length())
    i = Image("images/input/example2.jpg")
    i = bayer(Bayer(1), i, [WHITE, BLACK])
    i.show()


if __name__ == "__main__":
    main()  # call the main method if this is the main file
