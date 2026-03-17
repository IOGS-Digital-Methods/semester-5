#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LEnsE projects / Institut d'Optique

Control library test / System with a 0order feedback

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
K = 10

num_A = [A0]
den_A = [1/w0, 1]

sys_A = ct.tf(num_A, den_A, name='A')

sys_B = ct.tf([1],[K])

sys_C = ct.feedback(sys_A, sys2=sys_B, name='C')
#sys_C.update_names(name='C')

# Bode diagram
w = np.logspace(1, 8, 101)
ct.bode_plot([sys_A, sys_C], w)
plt.legend()


# Step Response
time = np.arange(0, 0.1, 0.000001)

T, yout_A = ct.step_response(sys_A, time)
T, yout_C = ct.step_response(sys_C, time)
plt.figure()
plt.plot(T, yout_A, label='A')
plt.plot(T, 1e4*yout_C, label='C (*1e4)')
plt.xlabel("time (s)")
plt.ylabel("Step Response")
plt.grid()

# Zoom
N = 100
plt.figure()
plt.plot(T[:N], yout_A[:N], label='A')
plt.plot(T[:N], 1e4*yout_C[:N], label='C (*1e4)')
plt.xlabel("time (s)")
plt.ylabel("Step Response - Zoom")
plt.grid()
plt.show()
