import numpy as np
import pygame
import time


def beep(frequency=440, duration_ms=500):
    sample_rate = 44100
    duration = duration_ms / 1000

    pygame.mixer.init(frequency=sample_rate, size=-16, channels=1)
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = (np.sin(2 * np.pi * frequency * t) * 32767).astype(np.int16)

    sound = pygame.sndarray.make_sound(wave)
    sound.play()
    time.sleep(duration)
    pygame.mixer.quit()


note_frequencies = {
    "C4": 261.63,
    "C#4": 277.18,
    "Db4": 277.18,
    "D4": 293.66,
    "D#4": 311.13,
    "Eb4": 311.13,
    "E4": 329.63,
    "F4": 349.23,
    "F#4": 369.99,
    "Gb4": 369.99,
    "G4": 392.00,
    "G#4": 415.30,
    "Ab4": 415.30,
    "A4": 440.00,
    "A#4": 466.16,
    "Bb4": 466.16,
    "B4": 493.88,
    "C5": 523.25,
}

pirates_notes = [
    "E4",
    "G4",
    "A4",
    "A4",  # "Da da da da"
    "E4",
    "G4",
    "B4",
    "B4",  # "Da da da da"
    "E4",
    "G4",
    "A4",
    "A4",  # repeat pattern
    "G4",
    "B4",
    "A4",  # descending part
    "G4",
    "E4",
    "G4",
    "A4",  # leading up again
    "B4",
    "C5",
    "D5",
    "D5",  # climax
    "E5",
    "D5",
    "C5",
    "B4",  # descending
    "A4",
    "A4",  # ending phrase
]

# Example
# beep(440, 500)

for note in pirates_notes:
    freq = note_frequencies.get(note, 440)  # default to A4 if not found
    beep(freq, 300)  # play each note for 300 ms
