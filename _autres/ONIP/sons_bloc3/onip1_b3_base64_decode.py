#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Outils Numériques / Semestre 5 / Institut d'Optique

WAV File conversion to Base64

Created on 26/oct/2023

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""

import base64
import numpy as np
from scipy.io import wavfile
from scipy.fft import fft
from matplotlib import pyplot as plt
from scipy.fft import fft, irfft, fftshift, fftfreq

samplerate_ONIP = 48000

#%% Decoding file
with open('B3_data_02.txt', 'rb') as file_to_decode:
    binary_file_data = file_to_decode.read()
    data = np.frombuffer(base64.b64decode(binary_file_data), np.int16)

print(f'Data Type = {type(data[0])}')
print(f'Data Shape = {data.shape}')

#%% FFT
tf_data = fft(data)
tf_freq = fftfreq(len(data), d=1/samplerate_ONIP)
plt.figure()
plt.title('Read WAV FFT')
plt.plot(tf_freq, np.abs(tf_data))
plt.show()


#%% Carrier freq
freq_c = float(input('Value of the carrier frequency ?'))
print(type(freq_c))

time = np.linspace(0, len(data)*1/samplerate_ONIP, len(data))
sig_port = np.sin(2*np.pi*freq_c*time)


#%% Decoding
sig_dec = data * sig_port
sig_dec = sig_dec.astype(np.int16)
plt.figure()
plt.title('Carrier')
plt.plot(time, sig_port)
plt.show()

# Need low-pass filter !!

#%% FFT
tf_data = fft(sig_dec)
tf_freq = fftfreq(len(sig_dec), d=1/samplerate_ONIP)
plt.figure()
plt.title('Read WAV FFT')
plt.plot(tf_freq, np.abs(tf_data))
plt.show()


#%% TF inverse
sig_dec_fin = np.fft.irfft(tf_data).astype(np.int16)
#%% Plotting decoded data
plt.figure()
plt.title('Decoded B64 Data')
plt.plot(sig_dec_fin)
plt.show()

print(type(sig_dec_fin[0]))


wavfile.write('test_en.wav', samplerate_ONIP, sig_dec_fin)