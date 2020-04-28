'''
「Glory_to_Hong_Kong」

reference:
https://twitter.com/adiossakura/status/1174669019011518465?lang=gl
'''

import pyaudio
import numpy as np

RATE = 44100
BPM = 84
NOTE4 = 60 / BPM
NOTE1, NOTE2, NOTE8, NOTE16 = (NOTE4 * 4, NOTE4 * 2, NOTE4 / 2, NOTE4 / 4)
NOTE4P, NOTE8P = (NOTE4 * 1.5, NOTE8 * 1.5)

# 0
# 1  2   3   4   5   6   7
O, \
C4, D4, E4, F4, G4, A4, B4, \
C5, D5, E5, F5, G5, A5, B5, \
C6, D6, E6 = (

    0,
    261.626, 293.665, 329.628, 349.228, 391.995, 440.000, 493.883,
    523.251, 587.330, 659.255, 698.456, 783.991, 880.000, 987.767,
    1046.502, 1174.659, 1318.510,
)


def tone(freq, length):
    w = int(length * RATE)
    t = float(freq) * np.pi * 2 / RATE
    return np.sin(np.arange(w) * t)


def play_wave(music_list):
    stream = pyaudio.PyAudio().open(format=pyaudio.paFloat32,
                                    channels=1,
                                    rate=RATE,
                                    frames_per_buffer=1024,
                                    output=True)
    for i in music_list:
        stream.write(i.astype(np.float32).tostring())
    stream.close()


def music():
    array = [
        tone(O, NOTE4), tone(O, NOTE8), tone(G4, NOTE8), tone(C5, NOTE4), tone(C5, NOTE8P), tone(D5, NOTE16),
        tone(B4, NOTE4), tone(B4, NOTE8P), tone(C5, NOTE16), tone(A4, NOTE2),

        tone(O, NOTE4), tone(O, NOTE8), tone(C5, NOTE8), tone(F5, NOTE4), tone(E5, NOTE8P), tone(F5, NOTE16),
        tone(D5, NOTE4), tone(E5, NOTE8P), tone(F5, NOTE16), tone(E5, NOTE2),

        tone(O, NOTE4), tone(O, NOTE8), tone(C5, NOTE8P), tone(A5, NOTE4), tone(F5, NOTE8P), tone(E5, NOTE16),
        tone(D5, NOTE4), tone(E5, NOTE8P), tone(F5, NOTE16), tone(G5, NOTE4), tone(E5, NOTE4), tone(C5, NOTE4),
        tone(C5, NOTE8P), tone(B4, NOTE16), tone(A4, NOTE4P), tone(F5, NOTE8), tone(E5, NOTE4P), tone(D5, NOTE8),
        tone(C5, NOTE2),

        # ----------------------
        tone(O, NOTE4), tone(O, NOTE8), tone(G4, NOTE8), tone(C5, NOTE4), tone(C5, NOTE8P), tone(D5, NOTE16),
        tone(B4, NOTE4), tone(B4, NOTE8P), tone(C5, NOTE16), tone(A4, NOTE2),

        tone(O, NOTE4), tone(O, NOTE8), tone(C5, NOTE8), tone(F5, NOTE4), tone(E5, NOTE8P), tone(F5, NOTE16),
        tone(D5, NOTE8P), tone(D5, NOTE16), tone(E5, NOTE8P), tone(F5, NOTE16), tone(E5, NOTE2),

        tone(O, NOTE4), tone(O, NOTE8), tone(C5, NOTE8P), tone(A5, NOTE4), tone(F5, NOTE8P), tone(E5, NOTE16),
        tone(D5, NOTE8P), tone(D5, NOTE16), tone(E5, NOTE8P), tone(F5, NOTE16), tone(G5, NOTE8), tone(O, NOTE8),
        tone(E5, NOTE8), tone(O, NOTE8), tone(C5, NOTE4), tone(C5, NOTE8P), tone(B4, NOTE16), tone(A4, NOTE4P),
        tone(F5, NOTE8), tone(E5, NOTE4P), tone(D5, NOTE8), tone(D5, NOTE8), tone(C5, NOTE4P),

        # ----------------------
        tone(O, NOTE4), tone(B4, NOTE8P), tone(C5, NOTE16), tone(D5, NOTE4P), tone(B4, NOTE8), tone(B4, NOTE8P),
        tone(G4, NOTE16), tone(G4, NOTE8P), tone(F5, NOTE16), tone(E5, NOTE2),

        tone(O, NOTE4), tone(D5, NOTE8P), tone(E5, NOTE16), tone(F5, NOTE4P), tone(F5, NOTE8), tone(F5, NOTE8P),
        tone(F5, NOTE16), tone(G5, NOTE8P), tone(D5, NOTE16), tone(E5, NOTE8), tone(O, NOTE8), tone(G5, NOTE8),
        tone(O, NOTE8), tone(C6, NOTE4), tone(C6, NOTE8P), tone(B5, NOTE16), tone(A5, NOTE8P), tone(A5, NOTE16),
        tone(A5, NOTE8), tone(B5, NOTE8), tone(C6, NOTE8), tone(C6, NOTE8P), tone(A5, NOTE16), tone(A5, NOTE8),
        tone(B5, NOTE8), tone(C6, NOTE8), tone(C6, NOTE8P), tone(C6, NOTE16), tone(C6, NOTE8P), tone(C6, NOTE16),
        tone(C6, NOTE8P), tone(C6, NOTE16), tone(C6, NOTE8P), tone(D6, NOTE16), tone(D6, NOTE1),

        # ----------------------
        tone(O, NOTE2), tone(G4, NOTE4), tone(G4, NOTE4), tone(G4, NOTE4), tone(C5, NOTE4), tone(C5, NOTE8P),
        tone(D5, NOTE16), tone(B4, NOTE4), tone(B4, NOTE8P), tone(C5, NOTE16), tone(A4, NOTE2),

        tone(O, NOTE4), tone(C5, NOTE8), tone(C5, NOTE8), tone(C5, NOTE8), tone(F5, NOTE4), tone(E5, NOTE8P),
        tone(F5, NOTE16), tone(D5, NOTE8P), tone(D5, NOTE16), tone(E5, NOTE8P), tone(F5, NOTE16), tone(E5, NOTE2),

        tone(O, NOTE4), tone(C5, NOTE8), tone(C5, NOTE8), tone(C5, NOTE8), tone(A5, NOTE4), tone(F5, NOTE8P),
        tone(E5, NOTE16), tone(D5, NOTE4), tone(E5, NOTE8P), tone(F5, NOTE16), tone(G5, NOTE4), tone(E5, NOTE4),
        tone(C5, NOTE4), tone(C5, NOTE8P), tone(B4, NOTE16), tone(A4, NOTE4P), tone(F5, NOTE8), tone(E5, NOTE4P),
        tone(D5, NOTE8), tone(D5, NOTE8), tone(C5, NOTE4P), tone(C5, NOTE2)

    ]
    return array


if __name__ == '__main__':
    play_wave(music())
