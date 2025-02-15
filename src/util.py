from img import Image


def save(img: Image, path: str | None = None):
    """Util function that will save the image back to
    the file given some path-like string `path`

    :param `img`: Image object that contains path info
    :param `path`: optional path that overides any stored path
    info inside the Image"""
    if path == None:
        if img.path != None:
            img.path = img.path.replace("input", "output")
            img.image.save(img.path)
            print(f"New image saved at: {img.path}")
        else:
            print("Could not save image, no path exists!")
    else:
        img.image.save(path)
        print(f"New image saved at: {path}")
