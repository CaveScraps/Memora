from abc import ABC, abstractmethod
from PIL import Image

class IImageProvider(ABC):

    #This is separate as the image provider may want to set a tinned image while they do some setup before providing images
    @abstractmethod
    def get_first_image(self) -> Image:
        pass

    @abstractmethod
    def get_next_image(self) -> Image:
        pass
