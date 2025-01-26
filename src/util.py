import os
from img import Image


def save(img: Image, path: str | None = None):
    if path == None:
        img_path = img.path
