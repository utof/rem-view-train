# Import the necessary modules
import requests
from io import BytesIO
from tkinter import *
from PIL import Image, ImageTk

# Create a Tkinter window
window = Tk()

# Function to download and store the random image


def load_random_image():
    # Use the requests module to download a random image from the internet
    response = requests.get("https://source.unsplash.com/random")
    img = Image.open(BytesIO(response.content))

    # Use the ImageTk module to convert the image to a format that Tkinter can display
    img = ImageTk.PhotoImage(img)

    # Store the image in a global variable so it can be accessed later
    global stored_image
    stored_image = img

# Function to display the stored image


def show_image():
    # Destroy any existing image labels to clear the canvas
    for widget in window.winfo_children():
        if isinstance(widget, Label) and widget.image is not None:
            widget.destroy()

    # Create an image label to display the stored image
    label = Label(image=stored_image)
    # Keep a reference to the image to prevent it from being garbage collected
    label.image = stored_image
    label.pack()


# Create buttons to trigger the functions
load_button = Button(text="Load Random Image", command=load_random_image)
load_button.pack()
show_button = Button(text="Show Image", command=show_image)
show_button.pack()

# Start the Tkinter event loop
window.mainloop()
