# Applying Filters and Enhancements
from PIL import Image, ImageFilter
from PIL import ImageEnhance

img = Image.open("cat.jpg")

# Blurriness
blurred = img.filter(ImageFilter.BLUR)
blurred.show()

# Sharpen
sharpened = img.filter(ImageFilter.SHARPEN)
sharpened.show()

# Brightness
enhancer = ImageEnhance.Brightness(img)

bright = enhancer.enhance(1.5)
bright.show()

# Color Enhancement
enhancer = ImageEnhance.Color(img)

colorful = enhancer.enhance(2)
colorful.show()

# Contrast
enhancer = ImageEnhance.Contrast(img)

contrast = enhancer.enhance(2)
contrast.show()
