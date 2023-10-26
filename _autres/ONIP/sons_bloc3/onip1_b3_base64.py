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
import librosa
from scipy.fft import fft, ifft, fftshift, fftfreq


#%% Data
samplerate_ONIP, data_ONIP = wavfile.read('hello_english.wav')
print(samplerate_ONIP)
print(f'file Shape = {data_ONIP.shape}')
print(f'file Type = {type(data_ONIP[0])}')

#%% Plotting data
plt.figure()
plt.title('Initial WAV Data')
plt.plot(data_ONIP)
plt.show()

#%% FFT
tf_data = fft(data_ONIP)
tf_freq = fftfreq(len(data_ONIP), d=1/samplerate_ONIP)
plt.figure()
plt.title('Initial WAV FFT')
plt.plot(tf_freq, np.abs(tf_data))
plt.show()

#%% Modulation
Ttot = len(data_ONIP)/samplerate_ONIP
t_lin = np.linspace(0,Ttot,len(data_ONIP))

f_port = samplerate_ONIP / 4
sig_port = np.sin(2*np.pi*f_port*t_lin)

print(f'Type SIG {sig_port.shape} / {type(sig_port[0])}')

sig_mod = data_ONIP*sig_port
sig_mod = sig_mod.astype(np.int16)

print(f'InitData = {data_ONIP.shape}')
print(f'SigMod = {sig_mod.shape}')


#%% Plotting data
plt.figure()
plt.title('Initial WAV Data')
plt.plot(sig_mod)
plt.show()

tf_data_mod = fft(sig_mod)
plt.figure()
plt.title('Modulated Signal FFT')
plt.plot(tf_freq, np.abs(tf_data_mod))
plt.show()



#%% Encoding file
encoded = base64.b64encode(sig_mod)

print(f'encoded Length = {len(encoded)}')
print(f'encoded Type = {type(encoded[0])}')

with open('B3_data_02.txt', 'wb') as file_to_save:
    encoded_data = base64.b64encode(sig_mod)
    file_to_save.write(encoded_data)

with open('B3_data_02.txt', 'rb') as file_to_decode:
    binary_file_data = file_to_decode.read()
    data = np.frombuffer(base64.b64decode(binary_file_data), np.int16)

print(f'Data Type = {type(data[0])}')
print(f'Data Shape = {data.shape}')

wavfile.write('test_mod_en.wav', samplerate_ONIP, data)

#%% FFT
tf_data = fft(data)
tf_freq = fftfreq(len(data), d=1/samplerate_ONIP)
plt.figure()
plt.title('Read WAV FFT')
plt.plot(tf_freq, np.abs(tf_data))
plt.show()

#%% Plotting decoded data
plt.figure()
plt.title('Decoded B64 Data')
plt.plot(data)
plt.show()

#%% Decoding
sig_dec = data * sig_port
sig_dec = sig_dec.astype(np.int16)

# Need low-pass filter !!

#%% FFT
tf_data = fft(sig_dec)
tf_freq = fftfreq(len(sig_dec), d=1/samplerate_ONIP)
plt.figure()
plt.title('Read WAV FFT')
plt.plot(tf_freq, np.abs(tf_data))
plt.show()

#%% Plotting decoded data
plt.figure()
plt.title('Decoded B64 Data')
plt.plot(sig_dec)
plt.show()

wavfile.write('test_en.wav', samplerate_ONIP, sig_dec)
