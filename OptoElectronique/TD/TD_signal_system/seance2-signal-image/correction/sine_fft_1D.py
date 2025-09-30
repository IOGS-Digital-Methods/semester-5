#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LEnsE projects / Institut d'Optique

FFT on 1D signal / Sine

Created on 25/Sep/2024

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""

import numpy as np
from matplotlib import pyplot as plt


def sine_wave(time, f0, amplitude=1):
    """Generate a sine wave at a specific frequency."""
    return amplitude * np.sin(2*np.pi*f0*time)


## Generate sine waves
criteria = 21
nb_of_periods = 20
f1 = 200
f2 = 287
fe = criteria*np.max([f1, f2])
time = np.arange(0, nb_of_periods*criteria*1/fe, 1/fe)

sine_a = sine_wave(time, f1, 1)
sine_b = sine_wave(time, f2, 2)

plt.figure()
plt.plot(time, sine_a, label=f'Sine at {f1} Hz')
plt.plot(time, sine_b, label=f'Sine at {f2} Hz')
plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.show()

## Sum of sine waves
sine_c = sine_a + sine_b

plt.figure()
plt.plot(time, sine_c, label=f'Sum of sine waves')
plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.show()

## FFt of the sine_c
tf_sine_c = np.fft.fft(sine_c)
freq = np.fft.fftfreq(len(sine_c), 1/fe)

plt.figure()
plt.ylabel('Module (V)')
plt.plot(freq,np.abs(tf_sine_c))
plt.xlabel('Frequency (Hz)')
plt.title('Sum of sine waves')
plt.show()
