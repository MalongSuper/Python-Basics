# creates a desktop window containing a text label,
# a text entry box, and an interactive click button
import tkinter as tk


def on_click():
    user_name = entry.get()
    label.config(text=f"Hello, {user_name}!")


root = tk.Tk()
root.title("Simple App")
root.geometry("300x150")

label = tk.Label(root, text="Enter your name:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

button = tk.Button(root, text="Greet Me", command=on_click, bg="lightblue")
button.pack(pady=10)

root.mainloop()
