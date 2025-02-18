from img import Image
import dither.random_noise as r


def main():
    """Main method"""
    i = Image("images/input/example2.jpg")  # create image from file path
    r.random_noise(i).show()  # use random noise dithering method


if __name__ == "__main__":
    main()  # call the main method if this is the main file
