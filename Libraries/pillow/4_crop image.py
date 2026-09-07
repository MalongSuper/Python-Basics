# Cropping Images
from PIL import Image

img = Image.open("cat.jpg")

cropped = img.crop((100, 50, 400, 300))
cropped.show()
