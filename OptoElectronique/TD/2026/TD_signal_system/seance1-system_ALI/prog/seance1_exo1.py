#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LEnsE projects / Institut d'Optique

Control library test / Definition of a first order system

Created on 25/Sep/2024

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""

import control as ct
import numpy as np
from matplotlib import pyplot as plt

# Parameters of the system
A0 = 1e5    # V/V
f0 = 30	    # Hz
w0 = 2*np.pi*f0   # rd/s

num_A = [A0]
den_A = [1/w0, 1]

sys_A = ct.tf(num_A, den_A)
print(sys_A)

# Bode diagram
w = np.logspace(1, 6, 101)
ct.bode_plot([sys_A], w)
plt.show()

time = np.arange(0, 0.1, 0.0001)

T, yout = ct.step_response(sys_A, time)
plt.figure()
plt.plot(T, yout)
plt.xlabel("time (s)")
plt.ylabel("Step Response")
plt.grid()


T, yout = ct.impulse_response(sys_A, time)
plt.figure()
plt.plot(T, yout)
plt.xlabel("time (s)")
plt.ylabel("Step Response")
plt.grid()

tf_yout = np.fft.fft(yout)
tf_yout = tf_yout / len(tf_yout)
plt.figure()
plt.semilogx(np.abs(tf_yout[:len(tf_yout)//2]))
plt.xlabel("Freq")
plt.ylabel("Step Response TF")
plt.grid()
plt.show()