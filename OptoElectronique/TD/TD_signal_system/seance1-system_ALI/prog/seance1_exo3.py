#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LEnsE projects / Institut d'Optique

Control library test / Definition of a second order system

Created on 25/Sep/2024

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""

import control as ct
import numpy as np
from matplotlib import pyplot as plt

# Parameters of the system
A0 = 10    # V/V
f0 = 1000	    # Hz
w0 = 2*np.pi*f0   # rd/s
m = [0.1, 0.5, 0.707, 1, 2]
m_n = ['0,1', '0,5', '0,707', '1', '2']

sys_H = []

for i, mm in enumerate(m):
    num = [A0/(w0**2), 0, 0]
    den = [1/w0**2, 2*float(mm)/w0, 1]
    nameH = f'H{i} / m={m_n[i]}'
    sys = ct.tf(num, den, name=nameH)
    sys_H.append(sys)

# Bode diagram
w = np.logspace(2, 6, 101)
ct.bode_plot(sys_H, w)
plt.legend()

# Step Response
time = np.arange(0, 0.01, 0.00001)
plt.figure()
for i, sys in enumerate(sys_H):
    T, yout_H = ct.step_response(sys, time)
    plt.plot(T, yout_H, label=f'H{i}')
plt.xlabel("time (s)")
plt.ylabel("Step Response")
plt.grid()
plt.legend()
plt.show()
