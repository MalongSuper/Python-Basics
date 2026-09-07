# Rotating Images
from PIL import Image

img = Image.open("cat.jpg")

rotated = img.rotate(90)
rotated.show()
