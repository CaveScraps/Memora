#!./venv/bin/python3
#pylint: disable=missing-docstring

import tkinter as tk
from guizero import App, Picture
from PIL import Image

from i_image_provider import IImageProvider
from folder_image_provider import FolderImageProvider as ImageProvider

# Get the screen size using tkinter
root = tk.Tk()
screen_width = root.winfo_screenwidth()

screen_height = root.winfo_screenheight()
root.destroy()

IMAGE_CHANGE_INTERVAL = 10000  # Change image every 10 seconds

def main(image_provider: IImageProvider) -> None:

    app = App(title="Memora", layout="auto", bg="black")

    # Set the app to full screen, using 'q' to exit
    app.set_full_screen("q")

    with image_provider.get_first_image() as img:
        image_size = get_scaled_image_size(img)
        picture = Picture(app, image=img, width=image_size[0], height=image_size[1])

    app.repeat(IMAGE_CHANGE_INTERVAL, change_image, args=[picture, image_provider])

    app.display()


def change_image(picture: Picture, image_provider: IImageProvider) -> None:
    with image_provider.get_next_image() as img:
        picture.image = img
        image_size = get_scaled_image_size(img,)
        picture.width = image_size[0]
        picture.height = image_size[1]


def get_scaled_image_size(image: Image.Image) -> tuple[int, int]:

    image_size = image.size

    #now we need to scale this up to fullscreen size while maintaining aspect ratio
    image_width = image_size[0]
    image_height = image_size[1]

    image_aspect = image_width / image_height
    screen_aspect = screen_width / screen_height

    if image_aspect > screen_aspect:
        scale_factor = screen_width / image_width
    else:
        scale_factor = screen_height / image_height

    new_size = (int(image_width * scale_factor), int(image_height * scale_factor))
    return new_size


if __name__ == "__main__":
    main(ImageProvider())
