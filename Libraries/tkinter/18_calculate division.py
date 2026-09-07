import tkinter as tk
from tkinter import messagebox


def calculate_division():
    # Retrieve inputs from entry boxes
    num1_str = entry_num1.get()
    num2_str = entry_num2.get()

    # Scenario 1: Check for empty input or non-numeric characters
    try:
        val1 = float(num1_str)
        val2 = float(num2_str)
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter numbers only.")
        return

    # Scenario 2: Check for division by zero
    if val2 == 0:
        messagebox.showwarning("Warning", "Cannot divide by zero!")
        return

    # Scenario 3: Successful calculation
    result = val1 / val2
    messagebox.showinfo("Information",
                        f"Calculation successful!\n\n{val1} / {val2} = {result}")


# Set up main window
root = tk.Tk()
root.title("Division Calculator")
root.geometry("300x180")

# Number 1 Input Layout
tk.Label(root, text="Enter First Number:").pack(pady=(10, 0))
entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)

# Number 2 Input Layout
tk.Label(root, text="Enter Second Number:").pack(pady=(5, 0))
entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)

# Calculate Button
btn_calculate = tk.Button(root, text="Divide", command=calculate_division)
btn_calculate.pack(pady=15)

root.mainloop()
