#!./venv/bin/python3

from guizero import App, Picture
from PIL import Image
import tkinter as tk

def main() -> None:

    # Get the screen size using tkinter
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()

    app = App(title="Memora", layout="auto", bg="black")

    # Set the app to full screen, using 'q' to exit
    app.set_full_screen("q")

    # Add a picture that fills the screen
    with Image.open("bird.png") as img:
        image_size = get_fullscreen_size_for_image(img, screen_width, screen_height)
        picture = Picture(app, image=img, width=image_size[0], height=image_size[1])

    # After 5 seconds, change the image
    app.after(5000, ChangeImage, args={picture})

    app.display()


def ChangeImage(picture: Picture) -> None:
    with Image.open("Also Bird.png") as img:
        picture.image = img
        image_size = get_fullscreen_size_for_image(img, screen_width, screen_height)
        picture.width = image_size[0]
        picture.height = image_size[1]


def get_fullscreen_size_for_image(image: Image, screen_width: int, screen_height: int) -> tuple[int, int]:

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
    main()
