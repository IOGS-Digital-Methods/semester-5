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
KCp = 100
KAp = 0.2
KaKbKcTaTi = [
    (KAp, 1, KCp, 1e-1, 0),
    (KAp, 1, KCp, 1e-1, 1e-1),
    (KAp, 1, KCp, 1e-1, 1e-3),
    (KAp, 1, KCp, 1e-1, 1e-5)
]

systems_A = []
systems_C  =[]
systems_B = []
systems_loop = []

for KA, KB, KC, TA, TI in KaKbKcTaTi:
    num_A = [KA]
    den_A = [TA, 1]
    sys_A = ct.tf(num_A, den_A)
    systems_A.append(sys_A)
    
    num_B = [KB]
    den_B = [1]
    sys_B = ct.tf(num_B, den_B)  
    systems_B.append(sys_B)

    if TI == 0:
        num_C = [KC]
        den_C = [1]
    else:
        num_C = [KC*TI, 1]
        den_C = [TI, 0]
    sys_C = ct.tf(num_C, den_C)  
    systems_C.append(sys_C)
    
    sys_AC = ct.series(sys_A, sys_C)
    sys_L = ct.feedback(sys_AC, sys2=sys_B, name='C')
    systems_loop.append(sys_L)

# Bode diagram
w = np.logspace(-1, 5, 101)

plt.figure()
plt.title(f'Parameters : Ka = {KaKbKcTaTi[0][0]} / Kb = {KaKbKcTaTi[0][1]} / Ta = {KaKbKcTaTi[0][3]} s / KC={KaKbKcTaTi[0][2]}')

freq_resp_A = ct.frequency_response(systems_A[0], w)
mag_A = 20*np.log10(freq_resp_A.magnitude)
plt.semilogx(w, mag_A, label='Initial system A', linestyle='dashed')

for k in range(len(KaKbKcTaTi)):
    freq_resp_L = ct.frequency_response(systems_loop[k], w)
    mag_L = 20*np.log10(freq_resp_L.magnitude)    
    plt.semilogx(w, mag_L, label=f'Control system ABC / TI={KaKbKcTaTi[k][4]}')
    plt.xlabel('Pulsation in rd/s')
    plt.ylabel('Gain in dB')
plt.legend()
plt.grid()

## Step Response
time = np.arange(0, 0.5, 0.0001)
T, youtA = ct.step_response(systems_A[0], time)

plt.figure()
plt.title(f'Parameters : KA={KaKbKcTaTi[0][0]} / KB={KaKbKcTaTi[0][1]}')
plt.plot(T, youtA, label=f'Initial system', linestyle='dashed')

for k in range(len(KaKbKcTaTi)):
    T, youtL = ct.step_response(systems_loop[k], time)
    plt.plot(T, KaKbKcTaTi[k][0]*KaKbKcTaTi[k][1]*youtL, label=f'Control system (x KA.KB) - Ti = {KaKbKcTaTi[k][4]} s')
plt.xlabel("time (s)")
plt.ylabel("Step Response")
plt.legend()
plt.grid()

plt.show()