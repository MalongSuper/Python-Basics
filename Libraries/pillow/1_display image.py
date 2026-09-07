# Displaying Images Inside Tkinter
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

img = Image.open("cat.jpg")
photo = ImageTk.PhotoImage(img)

label = Label(root, image=photo)
label.pack()

root.mainloop()
