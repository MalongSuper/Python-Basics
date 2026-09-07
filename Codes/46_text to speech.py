# Text-To-Speech
import nltk
from nltk.tokenize import word_tokenize
from underthesea import word_tokenize as vi_tokenize
from langdetect import detect
from gtts import gTTS
import librosa
import matplotlib.pyplot as plt
import numpy as np


nltk.download('punkt_tab')

text = input("Enter text: ")

lang = detect(text)
tokens = vi_tokenize(text) if lang == "vi" else word_tokenize(text)

print("Tokens:", tokens)

# Generate speech
gTTS(text=text, lang=lang).save("output.mp3")

# Load audio
y, sr = librosa.load("output.mp3", sr=None)

print(f"Sample Rate: {sr}")
print(f"Duration: {len(y)/sr:.2f} seconds")
print(f"Max Amplitude: {max(y)}")
print(f"Min Amplitude: {min(y)}")

# Waveform
plt.figure(figsize=(10,4))
librosa.display.waveshow(y, sr=sr)
plt.title("Waveform")
plt.show()

# Mel Spectrogram
mel = librosa.feature.melspectrogram(y=y, sr=sr)
mel_db = librosa.power_to_db(mel, ref=np.max)

plt.figure(figsize=(10,4))
librosa.display.specshow(mel_db, sr=sr, x_axis="time", y_axis="mel")
plt.colorbar(format="%+2.0f dB")
plt.title("Mel Spectrogram")
plt.show()

# Pitch Estimation
f0, _, _ = librosa.pyin(y, fmin=librosa.note_to_hz("C2"),
                        fmax=librosa.note_to_hz("C7"))

plt.figure(figsize=(10,4))
plt.plot(librosa.times_like(f0), f0)
plt.title("Pitch Contour")
plt.xlabel("Time (s)")
plt.ylabel("Frequency (Hz)")
plt.show()
