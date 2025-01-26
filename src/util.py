import os
from img import Image


def save(img: Image, path: str | None = None):
    if path == None:
        if img.path != None:
            img.path = img.path.replace("input", "output")
            img.image.save(img.path)
            print(f"New image saved at: {img.path}")
        else:
            print("Could not save, no path exists!")
    else:
        img.image.save(path)
        print(f"New image saved at: {path}")
