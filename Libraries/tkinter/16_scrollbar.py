# Large tables often use a Scrollbar using tk.Scrollbar(root)
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Table with Scrollbar")

# Create a frame to hold the table and scrollbar together
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Create the Treeview widget
table = ttk.Treeview(frame)
table["columns"] = ("Name", "Age")

# Format the columns
table.column("#0", width=0, stretch=tk.NO)
table.column("Name", width=150)
table.column("Age", width=100)

# Create headings
table.heading("Name", text="Name")
table.heading("Age", text="Age")

# Create and link the scrollbar
scrollbar = tk.Scrollbar(frame, orient="vertical", command=table.yview)
table.configure(yscrollcommand=scrollbar.set)

# Pack layout inside the frame (side-by-side)
table.pack(side="left", fill="y")
scrollbar.pack(side="right", fill="y")

# Add 20 sample entries to trigger scrolling
samples = [
    ("Alice Smith", 28), ("Bob Jones", 34), ("Charlie Brown", 22),
    ("Diana Prince", 29), ("Evan Wright", 41), ("Fiona Gallagher", 26),
    ("George Clark", 53), ("Hannah Abbott", 19), ("Ian Malcolm", 45),
    ("Julia Roberts", 38), ("Kevin Bacon", 50), ("Laura Croft", 31),
    ("Michael Scott", 43), ("Nina Simone", 27), ("Oscar Martinez", 36),
    ("Pam Beesly", 30), ("Quentin Tarantino", 55), ("Rachel Green", 25),
    ("Sam Winchester", 33), ("Tina Turner", 62)
]

for name, age in samples:
    table.insert("", tk.END, values=(name, age))

root.mainloop()
