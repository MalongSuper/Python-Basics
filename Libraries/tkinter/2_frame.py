# Label and Frame
import tkinter as tk

root = tk.Tk()

frame = tk.Frame(root, borderwidth=5, relief=tk.RAISED)
frame.pack(padx=20, pady=20)

label = tk.Label(frame, text="Inside the Frame")
label.pack()

root.mainloop()
