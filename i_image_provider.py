#pylint: disable=missing-docstring

from abc import ABC, abstractmethod
from PIL import Image

class IImageProvider(ABC):

    #We have a separate getter for the first image provider may want to
    #send a tinned image while they do some setup before providing images
    @abstractmethod
    def get_first_image(self) -> Image.Image:
        pass

    @abstractmethod
    def get_next_image(self) -> Image.Image:
        pass
