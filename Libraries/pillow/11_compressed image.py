# A Simple Image Compression Program
from PIL import Image


def compress_image(input_path, output_path, target_quality=85):

    with Image.open(input_path) as img:
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        img.save(output_path,"JPEG",
                 quality=target_quality, optimize=True)


compress_image("cat.jpg", "compressed_catt.jpg", target_quality=75)
