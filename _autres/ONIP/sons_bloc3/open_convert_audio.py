#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Outils Numériques / Semestre 5 / Institut d'Optique

WAV file opening and converting

Created on 22/Jul/2023

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""

import numpy as np
from scipy.io import wavfile
from scipy.fft import fft
from matplotlib import pyplot as plt
import librosa

# Data
samplerate_ONIP, data_ONIP = wavfile.read('ONIP.wav')
samplerate_cest, data_cest = wavfile.read('cest.wav')
samplerate_cool, data_cool = wavfile.read('cool.wav')

print(f'Type of Data = {type(data_ONIP[1])}')

print(samplerate_ONIP)
print(f'1st = {data_ONIP.shape}')
print(f'2nd = {data_cest.shape}')
print(f'3rd = {data_cool.shape}')

# Nb data and time vector
nb_data = 320000
sampling_freq = 160000
time = np.linspace(0, nb_data/sampling_freq, nb_data)

# Carriing frequencies
car_freq_1 = 15000
car_freq_2 = 30000
car_freq_3 = 45000
# Carriing signals
sin_freq_1 = np.sin(2*np.pi*car_freq_1*time)
sin_freq_2 = np.sin(2*np.pi*car_freq_2*time)
sin_freq_3 = np.sin(2*np.pi*car_freq_3*time)

# Resampling audio
new_data_ONIP = librosa.resample(data_ONIP/65536.0, orig_sr=samplerate_ONIP, target_sr=sampling_freq)
new_data_cest = librosa.resample(data_cest/65536.0, orig_sr=samplerate_ONIP, target_sr=sampling_freq)
new_data_cool = librosa.resample(data_cool/65536.0, orig_sr=samplerate_ONIP, target_sr=sampling_freq)

# Adding blank samples
n_ONIP = len(new_data_ONIP)
n_zeros = np.zeros((nb_data - n_ONIP))
new_data_ONIP = np.concatenate([new_data_ONIP*65536, n_zeros])
new_data_ONIP = new_data_ONIP.astype(int)
n_cest = len(new_data_cest)
n_zeros = np.zeros((nb_data - n_cest))
new_data_cest = np.concatenate([new_data_cest*65536, n_zeros])
new_data_cest = new_data_cest.astype(int)
n_cool = len(new_data_cool)
n_zeros = np.zeros((nb_data - n_cool))
new_data_cool = np.concatenate([new_data_cool*65536, n_zeros])
new_data_cool = new_data_cool.astype(int)

# Carriing signals
n_sig_ONIP = new_data_ONIP*sin_freq_1
n_sig_cest = new_data_cest*sin_freq_2
n_sig_cool = new_data_cool*sin_freq_3

n_sig_AM = (n_sig_ONIP + n_sig_cest + n_sig_cool)/3.0


# FFT of audio sample
TF_sig_AM = fft(n_sig_AM)

plt.figure()
plt.plot(np.abs(TF_sig_AM))
plt.show()

## SAVING DATA INTO CSV FILE (same type as Voltcraft Oscilloscope)