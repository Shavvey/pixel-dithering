import os
from img import Image


def save(img: Image, path: str | None = None):
    if path == None:
        if img.path != None:
            img.path = img.path.replace("input", "output")
        else:
            print("Could not save, no path exists!")
    else:
        img.image.save(path)
