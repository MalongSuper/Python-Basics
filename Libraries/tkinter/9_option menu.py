# Option Menu is used for drop-down selections.
import tkinter as tk

root = tk.Tk()

choice = tk.StringVar(root)
choice.set("Python")

menu = tk.OptionMenu(root, choice, "Python","Java", "C++")
menu.pack()

root.mainloop()
