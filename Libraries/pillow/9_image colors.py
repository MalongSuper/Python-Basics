# Working with Colors
from PIL import Image

img = Image.open("cat.jpg")

# Converting to Grayscale
gray = img.convert("L")
gray.show()

# Converting to HSV
hsv = img.convert("HSV")
hsv.show()

# Creating a Simple Mask
gray = img.convert("L")
mask = gray.point(lambda x: 255 if x > 120 else 0)
mask.show()

# Extracting a Specific Color Channel
r, g, b = img.split()
blank = g.point(lambda x: 0)
red_img = Image.merge("RGB", (r, blank, blank))
red_img.show()

# Green Version
green_img = Image.merge("RGB", (blank, g, blank))
green_img.show()

# Blue Version
blue_img = Image.merge("RGB", (blank, blank, b))
blue_img.show()

# Recoloring an Entire Image
r, g, b = img.split()

blue_img = Image.merge("RGB",(r.point(lambda x: x // 2),
                              g.point(lambda x: x // 2),
                              b.point(lambda x: min(x + 100, 255))))

blue_img.show()

# Changing the Color of a Specific Object
pixels = img.load()

width, height = img.size

for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]
        if r > 150 and g > 80 and b < 100:
            pixels[x, y] = (0, 0, 255)

img.show()
