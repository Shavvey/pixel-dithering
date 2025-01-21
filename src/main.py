from img import Image


def main():
    """Main method"""
    i = Image("images/input/example2.jpg")  # create image from file path
    i.make_grayscale()
    i.show()


if __name__ == "__main__":
    main()
