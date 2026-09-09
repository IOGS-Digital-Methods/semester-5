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

KaKbKcTa = [
    (10, 1, 1, 1e-1),
    (10, 1, 10, 1e-1),
    (10, 1, 100, 1e-1),
    (10, 1, 1000, 1e-1)
]

systems_A = []
systems_C  =[]
systems_B = []
systems_loop = []

for KA, KB, KC, TA in KaKbKcTa:
    num_A = [KA]
    den_A = [TA, 1]
    sys_A = ct.tf(num_A, den_A)
    systems_A.append(sys_A)
    
    num_B = [KB]
    den_B = [1]
    sys_B = ct.tf(num_B, den_B)  
    systems_B.append(sys_B)

    num_C = [KC]
    den_C = [1]
    sys_C = ct.tf(num_C, den_C)  
    systems_C.append(sys_C)
    
    sys_AC = ct.series(sys_A, sys_C)
    sys_L = ct.feedback(sys_AC, sys2=sys_B, name='C')
    systems_loop.append(sys_L)

# Bode diagram
w = np.logspace(-1, 5, 101)

plt.figure()
plt.title(f'Parameters : Ka = {KaKbKcTa[0][0]} / Kb = {KaKbKcTa[0][1]} / Ta = {KaKbKcTa[0][2]} s')

freq_resp_A = ct.frequency_response(systems_A[0], w)
mag_A = 20*np.log10(freq_resp_A.magnitude)
plt.semilogx(w, mag_A, label='Initial system A', linestyle='dashed')

for k in range(len(KaKbKcTa)):
    freq_resp_L = ct.frequency_response(systems_loop[k], w)
    mag_L = 20*np.log10(freq_resp_L.magnitude)    
    plt.semilogx(w, mag_L, label=f'Control system ABC / KC={KaKbKcTa[k][2]}')
    plt.xlabel('Pulsation in rd/s')
    plt.ylabel('Gain in dB')
plt.legend()
plt.grid()

'''
## Step Response
time = np.arange(0, 1, 0.0001)
N_sys = 2
T, youtA = ct.step_response(systems_A[N_sys], time)
T, youtL = ct.step_response(systems_loop[N_sys], time)

plt.figure()
plt.title(f'Parameters : KA={KaKbKcTa[N_sys][0]} / KB={KaKbKcTa[N_sys][1]} / KC={KaKbKcTa[N_sys][2]}')
plt.plot(T, youtA, label=f'Initial system')
plt.xlabel("time (s)")
plt.ylabel("Step Response")
plt.legend()
plt.grid()

plt.figure()
plt.title(f'Parameters : KA={KaKbKcTa[N_sys][0]} / KB={KaKbKcTa[N_sys][1]}')
plt.plot(T, youtA, label=f'Initial system')
plt.plot(T, KaKbKcTa[N_sys][0]*KaKbKcTa[N_sys][1]*youtL, label=f'Control system (x KA.KB)')
plt.xlabel("time (s)")
plt.ylabel("Step Response")
plt.legend()
plt.grid()


time = np.arange(0, 0.002, 0.00001)
N_sys = 2
T, youtA = ct.step_response(systems_A[N_sys], time)
T, youtL = ct.step_response(systems_loop[N_sys], time)

plt.figure()
plt.title(f'Parameters : KA={KaKbKcTa[N_sys][0]} / KB={KaKbKcTa[N_sys][1]}')
plt.plot(T, youtA, label=f'Initial system')
plt.plot(T, KaKbKcTa[N_sys][0]*KaKbKcTa[N_sys][1]*youtL, label=f'Control system (x KA.KB)')
plt.xlabel("time (s)")
plt.ylabel("Step Response")
plt.legend()
plt.grid()
'''
plt.show()