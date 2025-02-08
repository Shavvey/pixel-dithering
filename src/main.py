from img import Image
from pixel import Pixel
import dither.random_noise as r
from matrix import Matrix


def main():
    """Main method"""
    i = Image("images/input/example2.jpg")  # create image from file path
    r.random_noise(i).show()  # use random noise dithering method
    m = Matrix([[1, 0], [0, 1]])
    print(f"String representation of the matrix:{m.to_string()}")


if __name__ == "__main__":
    main()  # call the main method if this is the main file
