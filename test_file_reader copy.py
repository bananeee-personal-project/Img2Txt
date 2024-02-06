import sys
import io
import PyPDF2
from tkinter import Tk
from tkinter import Image as tkImage
import numpy as np

from PIL import Image,ImageGrab
from pytesseract import pytesseract
# sudo apt-get install python3-pil tesseract-ocr libtesseract-dev tesseract-ocr-eng tesseract-ocr-script-latn

def get_text_from_file(doc, first_page, last_page): 
    text = ""
    first_page = int(first_page)
    last_page = int(last_page)
    with open(doc, 'rb') as file:
        # Create a PDF reader object
        reader = PyPDF2.PdfReader(file)
        # Get the number of pages in the PDF file
        num_pages = len(reader.pages)
        # Loop through each page and extract the text
        if last_page != -1: 
            for i in range(first_page, last_page):
                # Get the page object
                page = reader.pages[i]
                # Extract the text from the page
                text = page.extractText()
                # Print the text
                # print(text)
        else:
            # Get the page object
            page = reader.pages[first_page]
            # Extract the text from the page
            text = page.extract_text()
            # Print the text
            print(text) 
    
    return text

def get_img_from_clipboard():
    # Create a Tk object
    # root = Tk()

    # Get the image from the clipboard
    image = ImageGrab.grabclipboard()

    # If the clipboard contains an image
    if image:

        # Check the format of the image data
        if isinstance(image, tkImage):
            # Convert the image to a PIL Image object
            pil_image = Image.open(image)
        else:
            # Convert the image to a NumPy array
            image_array = np.array(image)

            # Convert the array to a PIL Image object
            pil_image = Image.fromarray(image_array)

        # Do something with the PIL Image object
        # pil_image.show()

    # Close the Tk object
    # root.destroy()
    return pil_image

def main():
    
    
    text = ""
    doc = ""
    image = None
    first_page = 0
    last_page = -1
    mode = None

    while True:
      
        user_input = input("Enter content:")
        token = user_input.split("--")
        if len(token) == 3:
            doc, first_page, last_page = user_input
            mode = 0
        elif len(token) == 2:
            doc, first_page = user_input
            mode = 0
        else:
            print(token[0])
            # r = Tk()
            # r.withdraw()
            # r.clipboard_clear() 
            # image_clip = r.selection_get(selection="CLIPBOARD", type="image/png")
            # # image_clip = r.clipboard_get(type='image/*')
            # r.destroy()
            # cf = io.BytesIO(image_clip)
            pil_image = get_img_from_clipboard()
            # image = Image.open(input[0])
            # image= Image.open(timage_clip)
            mode = 1
            
        if mode == 0:
            text = "Context: " + get_text_from_file(doc, first_page, last_page)
        elif mode == 1:
            text = pytesseract.image_to_string(pil_image)
    
        r = Tk()
        r.withdraw()
        r.clipboard_clear() 
        r.clipboard_append(text)
        r.update() # now it stays on the clipboard after the window is closed
        r.destroy()
        print("Copy to clipboard!\n")

if __name__ == "__main__":
    try:
        main()
    except Exception as err:
        print(f"Exception {err=}, {type(err)=}")
        raise