from img import Image


def main():
    """Main method to be run using the makefile"""
    i = Image("images/example.png")  # create image from file path
    i.show()  # show the current image


if __name__ == "__main__":
    main()
