# A LabelFrame is a special type of Frame
# that automatically displays a title around its border.
import tkinter as tk

root = tk.Tk()

frame = tk.LabelFrame(root, text="User Information",
                      padx=10, pady=10)
frame.pack(padx=20, pady=20)

tk.Label(frame, text="Name:").pack()

root.mainloop()
