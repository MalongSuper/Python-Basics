# Adjusting Widget Sizes
import tkinter as tk

root = tk.Tk()
root.geometry("500x300")

label = tk.Label(root, text="Enter something:")
label.pack()

entry = tk.Entry(root, width=30)
entry.pack()

button = tk.Button(root, text="Submit", width=20, height=2)
button.pack()

root.mainloop()
