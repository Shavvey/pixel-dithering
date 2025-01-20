from img import Image


def main():
    """Main method"""
    i = Image("images/input/example2.jpg")  # create image from file path
    i.image = i.grayscale()  # make grayscale image
    i.show(None)


if __name__ == "__main__":
    main()
