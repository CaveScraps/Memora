#!./venv/bin/python3

from guizero import App, Picture
from PIL import Image

# TODO: Find out the screen size dynamically
screen_width = 1920
screen_height = 1080

def main() -> None:
    app = App(title="Fullscreen App", layout="auto", bg="black")

    # Set the app to full screen, using 'q' to exit
    app.set_full_screen("q")

    # Add a picture that fills the screen
    with Image.open("bird.png") as img:
        picture = Picture(app, image=img, width=screen_width, height=screen_height)
        bird_image_size = get_fullscreen_size_for_image(img)
        picture.width = bird_image_size[0]
        picture.height = bird_image_size[1]

        app.display()


def get_fullscreen_size_for_image(image: Image) -> tuple[int, int]:

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
