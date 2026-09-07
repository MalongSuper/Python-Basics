# Using Tkinter File Dialog
from tkinter import filedialog
from PIL import Image

file = filedialog.askopenfilename()

if file:
    img = Image.open(file)
    img.show()
