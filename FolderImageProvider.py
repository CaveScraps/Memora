from PIL import Image
from IImageProvider import IImageProvider

class FolderImageProvider(IImageProvider):

    def __init__(self) -> None:
        self.first_image_path = "Bird.png"
        self.next_image_path = "Also Bird.png"

    def get_first_image(self) -> str:
        return Image.open(self.first_image_path)

    def get_next_image(self) -> str:
        return Image.open(self.next_image_path)
