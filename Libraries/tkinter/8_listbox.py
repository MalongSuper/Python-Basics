# Listbox is used for displaying multiple selectable items.
import tkinter as tk

root = tk.Tk()

listbox = tk.Listbox(root)

listbox.insert(1, "Python")
listbox.insert(2, "Java")
listbox.insert(3, "C++")

listbox.pack()

root.mainloop()
