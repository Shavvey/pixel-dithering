from img import Image
from dither.random_noise import random_noise


def main():
    """Main method"""
    i = Image("images/input/example.jpg")
    i = random_noise(i)
    i.show()


if __name__ == "__main__":
    main()  # call the main method if this is the main file
