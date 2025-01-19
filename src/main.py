from img import Image


def main():
    """Main method"""
    i = Image("images/example.jpg")  # create image from file path
    i.grayscale()
    i.show("grayscale_example")


if __name__ == "__main__":
    main()
