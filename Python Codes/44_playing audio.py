# Playing and Analyzing Audio
import os
import librosa
import matplotlib.pyplot as plt
from pydub import AudioSegment
from pydub.playback import pla

# Convert MP3 -> WAV
audio = AudioSegment.from_mp3("bird_singing.mp3")
audio.export("bird_singing.wav", format="wav")

print("Playing Audio...")
play(audio)

# Load with Librosa
y, sr = librosa.load("bird_singing.wav", sr=None)

duration = len(y) / sr
size_mb = os.path.getsize("bird_singing.wav") / (1024**2)

print(f"Sample Rate: {sr} Hz")
print(f"Samples: {len(y)}")
print(f"Bits per Sample: 16")
print(f"Duration: {duration:.2f} seconds")
print(f"File Size: {size_mb:.2f} MB")
print(f"File Size per Second: {size_mb/duration:.2f} MB/s")
print(f"Max Amplitude: {max(y)}")
print(f"Min Amplitude: {min(y)}")

plt.figure(figsize=(10,4))
librosa.display.waveshow(y, sr=sr)
plt.title("Waveform")
plt.show()
