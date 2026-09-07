# Audio Filtering
from pydub import AudioSegment
from pydub.generators import Sine, Square, WhiteNoise
from pydub.playback import play
import numpy as np
from scipy.signal import butter, lfilter

# Generate signals
sine = Sine(440).to_audio_segment(duration=2000)
square = Square(330).to_audio_segment(duration=2000)
noise = WhiteNoise().to_audio_segment(duration=2000)

for name, sound in [("Sine", sine), ("Square", square), ("Noise", noise)]:
    print(name, sound.duration_seconds, "seconds")
    play(sound)

# Combine sounds
combined = sine + square + noise
combined.export("combined.wav", format="wav")

print("Playing Combined Signal...")
play(combined)

# Volume adjustments
(combined + 20).export("louder.wav", format="wav")
((sine * 2) + (square * 2) + (noise * 2)).export("looped.wav", format="wav")

# Built-in filters
low_pass = combined.low_pass_filter(1000)
high_pass = combined.high_pass_filter(1000)

play(low_pass)
play(high_pass)

low_pass.export("low_pass.wav", format="wav")
high_pass.export("high_pass.wav", format="wav")

# NumPy + SciPy filtering
samples = np.array(combined.get_array_of_samples())


def lowpass(data, cutoff, fs):
    b, a = butter(5, cutoff/(0.5*fs), btype="low")
    return lfilter(b, a, data)


filtered = lowpass(samples, 1000, combined.frame_rate)

filtered_audio = AudioSegment(filtered.astype(np.int16).tobytes(),
                              frame_rate=combined.frame_rate,
                              sample_width=2,
                              channels=1)

play(filtered_audio)
filtered_audio.export("filtered_output.wav", format="wav")
