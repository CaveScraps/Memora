#!./venv/bin/python3

from guizero import App, Picture
from PIL import Image
import tkinter as tk

from IImageProvider import IImageProvider
from FolderImageProvider import FolderImageProvider as ImageProvider

# Get the screen size using tkinter
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()

image_change_interval_ms = 10000  # Change image every 10 seconds

def main(image_provider: IImageProvider) -> None:

    app = App(title="Memora", layout="auto", bg="black")

    # Set the app to full screen, using 'q' to exit
    app.set_full_screen("q")

    with image_provider.get_first_image() as img:
        image_size = get_fullscreen_size_for_image(img, screen_width, screen_height)
        picture = Picture(app, image=img, width=image_size[0], height=image_size[1])

    app.repeat(image_change_interval_ms, ChangeImage, args=[picture, image_provider])

    app.display()


def ChangeImage(picture: Picture, image_provider: IImageProvider) -> None:
    with image_provider.get_next_image() as img:
        picture.image = img
        image_size = get_fullscreen_size_for_image(img, screen_width, screen_height)
        picture.width = image_size[0]
        picture.height = image_size[1]


def get_fullscreen_size_for_image(image: Image.Image, screen_width: int, screen_height: int) -> tuple[int, int]:

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
    image_provider = ImageProvider()
    main(image_provider)
