#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Outils Numériques / Semestre 5 / Institut d'Optique

FFT from Numpy and frequency axis reconstruction

Created on 28/nov/2023

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""

#%%
import numpy as np
import matplotlib.pyplot as plt


def freq_reconstruct(N, Fe=1.0):
	if N%2 == 0:	# even number (pair)
		freq1 = np.linspace(0, (N-2)/(2*N), N//2) * Fe
		freq2 = np.linspace(-N/(2*N), -2/(2*N), N//2) * Fe
		freq = np.concatenate((freq2, freq1))
		print('OK')
	else:			# odd number (impair)
		freq1 = np.linspace(0, (N-1)/(2*N), N//2+1) * Fe
		freq2 = np.linspace(-(N-1)/(2*N), -2/(2*N), N//2) * Fe
		freq = np.concatenate((freq2, freq1))
	return freq

print('Nombre impair')
N1 = 11
freq11 = np.fft.fftfreq(N1)
print(freq11)
freq12 = freq_reconstruct(N1)
print(freq12)

print('Nombre pair')
N2 = 12
freq11 = np.fft.fftfreq(N2)
print(freq11)
freq12 = freq_reconstruct(N2)
print(freq12)

'''
#%% Sinewave signal
t = np.linspace(0,10,101)
sig = np.sin(2*np.pi*t)

plt.figure()
plt.plot(t, sig)
plt.show()

FFT_sig = np.fft.fft(sig)
freq = np.fft.fftfreq(len(sig), d=t[1]-t[0])
freq = np.fft.fftshift(freq)
plt.figure()
plt.plot(freq, np.fft.fftshift(np.abs(FFT_sig)))
plt.show()

#%%
import scipy
import numpy as np
import matplotlib.pyplot as plt

dt = 0.1
T1 = 2
T2 = 5
t = np.arange(0, T1*T2, dt) 
signal = np.cos(2*np.pi/T1*t) + np.sin(2*np.pi/T2*t)

plt.figure()
plt.subplot(211)
plt.plot(t,signal)

fourier = scipy.fft.fft(signal)
n = signal.size
freq = scipy.fft.fftfreq(n, d=dt)

plt.subplot(212)
plt.plot(freq, fourier.real, label="real")
plt.plot(freq, fourier.imag, label="imag")
plt.legend()

plt.show()

'''