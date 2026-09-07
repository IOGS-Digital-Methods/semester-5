#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Control library test / Definition of a first order system

Created on 07/Sep/2026

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""

import numpy as np
from matplotlib import pyplot as plt
import control as ct


# Parameters of the system

KaKbTa = [
    (1, 1, 1e-1),
    (10, 1, 1e-1),
    (1e7, 1e-4, 1e-1)
]

systems_A = []
systems_B = []
systems_loop = []

for KA, KB, TA in KaKbTa:
    num_A = [KA]
    den_A = [TA, 1]
    sys_A = ct.tf(num_A, den_A)
    systems_A.append(sys_A)
    
    num_B = [KB]
    den_B = [1]
    sys_B = ct.tf(num_B, den_B)  
    systems_B.append(sys_B)
    
    sys_C = ct.feedback(sys_A, sys2=sys_B, name='C')
    systems_loop.append(sys_C)

# Bode diagram
w = np.logspace(-1, 5, 101)

for k in range(len(KaKbTa)):
    freq_resp_A = ct.frequency_response(systems_A[k], w)
    mag_A = 20*np.log10(freq_resp_A.magnitude)
    freq_resp_L = ct.frequency_response(systems_loop[k], w)
    mag_L = 20*np.log10(freq_resp_L.magnitude)    
    plt.figure()
    plt.title(f'Parameters : Ka = {KaKbTa[k][0]:.2e} / Kb = {KaKbTa[k][1]:.2e} / Ta = {KaKbTa[k][2]:.2e} s')
    plt.semilogx(w, mag_A, label='Initial system A')
    plt.semilogx(w, mag_L, label='Control system AB')
    plt.grid()
    plt.legend()
    plt.xlabel('Pulsation in rd/s')
    plt.ylabel('Gain in dB')
    
plt.show()

'''
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
'''