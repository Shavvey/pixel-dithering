from img import Image


def main():
    """Main method to be run using the makefile"""
    i = Image("images/example.jpg")  # create image from file path
    i.show(None)  # show the current image


if __name__ == "__main__":
    main()
