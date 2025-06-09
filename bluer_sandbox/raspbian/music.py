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


# Example
beep(440, 500)
