from typing import Generator
from PIL import Image
from IImageProvider import IImageProvider
from pathlib import Path

class FolderImageProvider(IImageProvider):

    def __init__(self) -> None:
        self.image_folder = "images/"
        self.image_paths = [x for x in Path(self.image_folder).iterdir() if x.suffix.lower() in [".jpg", ".jpeg", ".png"]]
        self.image_counter = 0

    def get_first_image(self) -> Image.Image:
        return self.get_next_image()

    def get_next_image(self) -> Image.Image:
        image = Image.open(self.image_paths[self.image_counter % len(self.image_paths)])
        self.image_counter += 1
        return image

