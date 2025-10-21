#!./venv/bin/python3

from guizero import App, Text

def exit_fullscreen_message():
    app.info("Fullscreen", "Press 'q' to exit full screen.")

app = App(title="Fullscreen App", layout="auto")
message = Text(app, text="This app is now in full screen!")

# Set the app to full screen, using 'q' to exit
app.set_full_screen("q") 

# Display a message about how to exit full screen
exit_fullscreen_message()

app.display()
