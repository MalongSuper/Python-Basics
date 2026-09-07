# Saving Images
from PIL import Image
img = Image.open("cat.jpg")

# Retrieving Image Information and Metadata
print(img.size)
print(img.mode)
print(img.format)

# retrieve raw pixel data.
pixels = list(img.get_flattened_data())
print(pixels[:10])

# Save as different formats
img.save("photo.jpg")
img.save("photo.png")
img.save("photo.bmp")
