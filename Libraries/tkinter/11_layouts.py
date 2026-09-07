# Place, Pack and Grid
# label.pack() : automatically arranges widgets
# label.grid(row=0, column=0, padx=12, pady=15): uses rows and columns.
# label.place(x=100, y=50): Place uses exact coordinates.
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Layout Managers Example")

# Using pack()
frame_pack = ttk.LabelFrame(root, text="Pack (Top-to-Bottom)")
frame_pack.pack(side="left", padx=10, pady=10, fill="both", expand=True)

ttk.Button(frame_pack, text="Button 1").pack(pady=5)
ttk.Button(frame_pack, text="Button 2").pack(pady=5)

# Using grid()
frame_grid = ttk.LabelFrame(root, text="Grid (Rows & Columns)")
frame_grid.pack(side="left", padx=10, pady=10, fill="both", expand=True)

ttk.Button(frame_grid, text="R0 C0").grid(row=0, column=0, padx=5, pady=5)
ttk.Button(frame_grid, text="R0 C1").grid(row=0, column=1, padx=5, pady=5)
ttk.Button(frame_grid, text="R1 C0").grid(row=1, column=0, padx=5, pady=5)
ttk.Button(frame_grid, text="R1 C1").grid(row=1, column=1, padx=5, pady=5)

# Using place()
frame_place = ttk.LabelFrame(root, text="Place (Exact Coordinates)")
frame_place.pack(side="left", padx=10, pady=10, fill="both", expand=True)

ttk.Button(frame_place, text="X=20, Y=20").place(x=20, y=20)
ttk.Button(frame_place, text="X=50, Y=70").place(x=50, y=70)

root.mainloop()
