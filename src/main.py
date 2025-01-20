from img import Image


def main():
    """Main method"""
    i = Image("images/example2.jpg")  # create image from file path
    i.image = i.grayscale()  # make grayscale image
    i.show("grayscale_example")


if __name__ == "__main__":
    main()
