# A Simple Image Background Remover with Tkinter
# Background Remover System
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
from rembg import remove  # pip install "rembg[cpu]"

selected_file = None
original_image = None


def open_image():
    global selected_file, original_image

    selected_file = filedialog.askopenfilename(filetypes=[("Images", "*.png *.jpg "
                                                                     "*.jpeg *.bmp *.webp")])

    if not selected_file:
        return

    original_image = Image.open(selected_file)
    show_preview()


def show_preview():
    preview_window = Toplevel(root)
    preview_window.title("Preview Image")

    img = original_image.copy()

    # Resize image to fit preview window
    max_width = 500
    max_height = 400

    img.thumbnail((max_width, max_height))

    photo = ImageTk.PhotoImage(img)

    image_label = Label(preview_window, image=photo)
    image_label.image = photo
    image_label.pack(padx=10, pady=10)

    Button(preview_window, text="Remove Background", font=("Arial", 12),
           command=lambda: remove_background(preview_window)).pack(pady=10)


def remove_background(window):
    global selected_file

    try:
        with open(selected_file, "rb") as input_file:
            input_data = input_file.read()

        output_data = remove(input_data)

        save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG Image", "*.png")])

        if save_path:
            with open(save_path, "wb") as output_file:
                output_file.write(output_data)

            messagebox.showinfo("Success",
                                "Background removed successfully!")

            window.destroy()

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Main Window
root = Tk()
root.title("Simple Background Remover")
root.geometry("300x150")

Button(root, text="Choose Image", width=20, height=2, command=open_image).pack(expand=True)
root.mainloop()
