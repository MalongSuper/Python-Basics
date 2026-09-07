# create a Decimal → Binary → Hexadecimal converter.
import tkinter as tk


def convert():
    value = int(entry.get())
    binary_label.config(text=f"Binary: {bin(value)}")
    hex_label.config(text=f"Hex: {hex(value)}")


root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Convert", command=convert)
button.pack()

binary_label = tk.Label(root, text="Binary:")
binary_label.pack()

hex_label = tk.Label(root, text="Hex:")
hex_label.pack()

root.mainloop()
