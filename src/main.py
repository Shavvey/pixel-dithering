from img import Image
import dither.bayer as b
import palette as p


def main():
    """Main method"""
    i = Image("images/input/panda.jpg")
    i = b.bayer(b.Bayer(3), i, p.RUST)
    i.show()
    i.save("images/output/panda.jpg")


if __name__ == "__main__":
    main()  # call the main method if this is the main file
