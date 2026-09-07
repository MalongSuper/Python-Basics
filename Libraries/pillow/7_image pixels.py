# Manipulating Individual Pixels
from PIL import Image

img = Image.open("cat.jpg")

# Reading a Pixel
pixel = img.getpixel((100, 100))
print(pixel)

# Changing a Pixel
img.putpixel((100,100), (0,255,0))
img.show()

# Drawing a Red Line
for x in range(100):
    img.putpixel((x,50), (255,0,0))

img.show()

