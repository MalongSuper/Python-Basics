# Canvas
import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()
canvas.create_rectangle(50, 50, 150, 100)

root.mainloop()
