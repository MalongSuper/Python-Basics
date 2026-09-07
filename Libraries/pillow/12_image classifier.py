# A Pretrained Image Classifier
import numpy as np
from PIL import Image
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions


model = MobileNetV2(weights='imagenet')
image_path = "cat.jpg"

img = Image.open(image_path)
img = img.resize((224, 224))

img_array = np.array(img)
img_array = np.expand_dims(img_array, axis=0)

img_array = preprocess_input(img_array)
predictions = model.predict(img_array)

decoded_predictions = decode_predictions(predictions, top=3)[0]

print(f"Predictions for {image_path}:")

for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
    print(f"{i + 1}. {label.capitalize()} ({score * 100:.2f}%)")
