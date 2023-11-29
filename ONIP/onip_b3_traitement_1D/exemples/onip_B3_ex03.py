#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Outils Numériques / Semestre 5 / Institut d'Optique

Bonnes pratiques - Exemple 3 - Array and functions

Created on 29/Nov/2023

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""

import time
import numpy as np
import matplotlib.pyplot as plt

def sinus(t, A, f):
	return A*np.sin(2*np.pi*f*t)

time_vect = np.linspace(0, 1, 1001)


#%%
time1 = time.time()
tf = np.fft.fft(sinus(time_vect, 1, 10))
plt.figure()
plt.plot(time_vect, sinus(time_vect, 1, 10))

time2 = time.time()
print((time2-time1))
    
#%%
time1 = time.time()
sig = sinus(time_vect, 1, 10)
tf = np.fft.fft(sig)
plt.figure()
plt.plot(time_vect, sig)

time2 = time.time()
print((time2-time1))

#%%

def sinus_w(t, A=1, f=100):
    if isinstance(t, np.ndarray):
        Te = t[1]-t[0]	
        if(1/Te < 2*f):
            print('Shannon sampling frequency warning !!')
    return A*np.sin(2*np.pi*f*t)

time_vect = np.linspace(0, 1, 101)
sig = sinus_w(time_vect)
