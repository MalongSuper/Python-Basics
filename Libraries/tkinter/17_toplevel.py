# Pop-Up Windows
import tkinter as tk

root = tk.Tk()
# Display something in the first window
label = tk.Label(root, text="Hello World")
label.pack()

popup = tk.Toplevel(root)
# Display something in the pop-up window
popup_label = tk.Label(popup, text="Hello World Again")
popup_label.pack()

root.mainloop()
