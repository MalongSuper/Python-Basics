# thumbnail() creates a miniature version of the image.
from PIL import Image

img = Image.open("cat.jpg")

img.thumbnail((300, 300))
img.show()
