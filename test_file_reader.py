import sys
import PyPDF2
from tkinter import Tk

from PIL import Image
from pytesseract import pytesseract

def main():
    test = sys.argv[1:]
    doc, pageNum = sys.argv[1:]
    text = None
    
    r = Tk()
    r.withdraw()
    r.clipboard_clear()
    
    print(test)
    with open(doc, 'rb') as file:
        # Create a PDF reader object
        reader = PyPDF2.PdfReader(file)
        # Get the number of pages in the PDF file
        num_pages = len(reader.pages)
        # Loop through each page and extract the text
        if pageNum == -1: 
            for i in range(num_pages):
                # Get the page object
                page = reader.pages[i]
                # Extract the text from the page
                text = page.extractText()
                # Print the text
                # print(text)
        else:
            # Get the page object
            page = reader.pages[int(pageNum)]
            # Extract the text from the page
            text = page.extract_text()
            # Print the text
            print(text) 
    
    r.clipboard_append(text)
    r.update() # now it stays on the clipboard after the window is closed
    r.destroy()
    print("Copy to clipboard!")

if __name__ == "__main__":
    main()
