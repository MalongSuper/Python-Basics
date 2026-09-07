# Configuration
import tkinter as tk

root = tk.Tk()


def show_message():
    label = tk.Label(root, text="Hello World")
    label.config(text="Button Clicked!")
    label.pack()


button = tk.Button(root, text="Click", command=show_message)
button.pack()

root.mainloop()
