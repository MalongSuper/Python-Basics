# PhotoImage
import tkinter as tk

root = tk.Tk()

image = tk.PhotoImage(file="python_logo.png")
label = tk.Label(root, image=image)
label.pack()

root.mainloop()
