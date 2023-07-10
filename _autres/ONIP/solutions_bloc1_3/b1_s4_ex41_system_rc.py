#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Outils Numériques / Semestre 5 / Institut d'Optique

System approach - RC filter

Created on 20/Apr/2023

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""

import control as ct
from IPython.display import *

import numpy as np
from matplotlib import pyplot as plt

#%% System definition
class sys_filter_RC_LP:
    def __init__(self, R, C):
        self.R = R
        self.C = C
        self.num = np.array([1])
        self.den = np.array([self.R*self.C, 1])
        self.tf_sys = ct.tf(self.num, self.den)
        
    def getTF(self):
        return self.tf_sys


sysRC = sys_filter_RC_LP(1e3, 1e-6)

display(sysRC.getTF())

#%% Frequency Response / Bode
w = np.logspace(1, 6, 101)
mag, phase, w = ct.bode_plot(sysRC.getTF(), w, plot=True)
mag_db = 20*np.log(mag)
phase_deg = phase * 180 / np.pi
f = w/(2*np.pi)

# Display Bode
fig, axs = plt.subplots(2, 1)
fig.suptitle('Frequency Response of a RC low-pass filter')
axs[0].plot(f, mag_db)
axs[0].set_ylabel('Magnitude (dB)')
axs[0].set_xscale('log')
axs[0].grid()
axs[0].grid(which = "major", linewidth = 1)
axs[0].grid(which = "minor", linewidth = 0.2)
axs[0].minorticks_on()
axs[1].plot(f, phase_deg)
axs[1].set_ylabel('Phase (degrees)')
axs[1].set_xscale('log')
axs[1].grid()
axs[1].grid(which = "major", linewidth = 1)
axs[1].grid(which = "minor", linewidth = 0.2)
axs[1].minorticks_on()
axs[1].set_xlabel('Frequency (Hz)')

#%% Margins :
( GM , PM , wg , wp ) = ct.margin(sysRC.getTF())
print ('GM [1 ( not dB )] = ', GM)
print ('PM [ deg ] = ', PM)
print ('wg [ rad / s ] = ', wg)
print ('wp [ rad / s ] = ', wp)

#%% Step response
t, y = ct.step_response(sysRC.getTF())
plt.figure()
plt.plot(t, y)
plt.title('Step Response of a low-pass RC filter')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.grid()
plt.minorticks_on()
plt.show()

#%% Impulse response
t = np.linspace(0,1, 10001)
t, y = ct.impulse_response(sysRC.getTF(), T=t)
plt.figure()
plt.plot(t, y)
plt.title('Impulse Response of a low-pass RC filter')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.grid()
plt.minorticks_on()
plt.show()

import scipy as sc

tf = sc.fft.fft(y)/len(y)
tf_half = tf[0:len(tf)//2]
plt.figure()
plt.plot(20*np.log10(np.abs(tf_half)))
plt.xscale('log')
plt.show()

#%% Forced response
t = np . linspace (0, 1, 1001)  # time vector
u = 2 * np.sin(2*np.pi*20*t)   # signal vector - sine at 20 Hz and 2V

## Simulation :
t, y = ct.forced_response(sysRC.getTF(), t, u)        # X0 : initial state
plt.figure()
plt.plot(t, y)
plt.title('Forced Response of a low-pass RC filter')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.grid()
plt.minorticks_on()
plt.show()