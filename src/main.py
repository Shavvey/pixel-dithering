from img import Image
from pixel import *


def main():
    """Main method"""
    i = Image("images/input/example2.jpg")  # create image from file path
    i.show()
    i.to_quantize([BLACK, WHITE]).show()


if __name__ == "__main__":
    main()
