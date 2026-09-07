# Changing Colors
import tkinter as tk

root = tk.Tk()
root.geometry("500x300")
root.resizable(False, False)

root.configure(bg="#2C3E50")

label = tk.Label(root, text="Dark Theme", fg="white", bg="#2C3E50")
label.pack(padx=20, pady=20)

label = tk.Label(root, text="Hello Tkinter!", fg="white", bg="blue")
label.pack()

root.mainloop()
