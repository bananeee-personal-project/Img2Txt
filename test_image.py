import tkinter as tk
from PIL import ImageGrab, Image
import numpy as np

# Create a Tk object
root = tk.Tk()

# Get the image from the clipboard
image = ImageGrab.grabclipboard()

# If the clipboard contains an image
if image:

    # Check the format of the image data
    if isinstance(image, tk.Image):
        # Convert the image to a PIL Image object
        pil_image = Image.open(image)
    else:
        # Convert the image to a NumPy array
        image_array = np.array(image)

        # Convert the array to a PIL Image object
        pil_image = Image.fromarray(image_array)

    # Do something with the PIL Image object
    pil_image.show()

# Close the Tk object
root.destroy()