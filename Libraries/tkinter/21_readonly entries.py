# Read-Only Entries
import tkinter as tk

root = tk.Tk()

entry = tk.Entry(root)
entry.insert(0, "Python Programming")
entry.config(state="readonly")
entry.pack()

root.mainloop()
