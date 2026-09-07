# Practical Example: Decimal Converter
import tkinter as tk


def convert():
    value = int(decimal_entry.get())

    binary_entry.config(state="normal")
    binary_entry.delete(0, tk.END)
    binary_entry.insert(0, bin(value))
    binary_entry.config(state="readonly")


root = tk.Tk()

tk.Label(root, text="Decimal").pack()

decimal_entry = tk.Entry(root)
decimal_entry.pack()

tk.Button(root, text="Convert", command=convert).pack()

binary_entry = tk.Entry(root)
binary_entry.pack()

root.mainloop()
