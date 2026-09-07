# Treeview widget allows data to be
# displayed in a table format.
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Sample Table")

# Create the Treeview widget
table = ttk.Treeview(root)
table["columns"] = ("Name", "Age")

# Format the columns
table.column("#0", width=0, stretch=tk.NO)  # Hide the default first phantom column
table.column("Name", width=150)
table.column("Age", width=100)

# Create headings
table.heading("Name", text="Name")
table.heading("Age", text="Age")

# Add sample data (5 entries)
samples = [("Alice Smith", 28),
           ("Bob Jones", 34),
           ("Charlie Brown", 22),
           ("Diana Prince", 29),
           ("Evan Wright", 41)]

for name, age in samples:
    table.insert("", tk.END, values=(name, age))

# Pack the widget and run the application
table.pack(padx=10, pady=10)

root.mainloop()
