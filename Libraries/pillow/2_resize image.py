# Resizing Images
from PIL import Image

img = Image.open("cat.jpg")

new_img = img.resize((300, 200))
new_img.show()
