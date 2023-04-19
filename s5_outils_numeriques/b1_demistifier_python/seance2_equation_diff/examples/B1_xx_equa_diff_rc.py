#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Outils Numériques / Semestre 5 / Institut d'Optique

Differential Equation Resolution - Euler Methods
- RC circuit - Discharge of C in R with initial voltage

Created on 15/Apr/2023

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""

#%%
import numpy as np
from matplotlib import pyplot as plt


#%% Numerical method / Explicit Euler Method
# Values of the problem
R = 1e5
C = 1e-6

# Simple Version - Discharge of C in R
# @see : ode_book.pdf pp. 7/112 --> 9/112

N = 20
T = 1
dt = T/N
u0 = 5

t = np.zeros(N+1)
u = np.zeros(N+1)

u[0] = u0

for n in range(N):
    t[n+1] = t[n] + dt
    u[n+1] = (1 - dt/(R*C))*u[n]

plt.figure()
plt.plot(t,u)
plt.show()


# Version 1.1 - Discharge of C in R with a function
def f_disc_c_r(t, u, tau=1e-1):
    return -u/tau

def explicit_euler(f, u0, T, N):
    dt = T/N
    t = np.zeros(N+1)
    u = np.zeros(N+1)
    u[0] = u0

    for n in range(N):
        t[n+1] = t[n] + dt
        u[n+1] = u[n] + f(t[n], u[n])*dt

    return t, u

N_val = [10, 20, 50, 200, 1000]

plt.figure()
for k in range(len(N_val)):
    t, u = explicit_euler(f_disc_c_r, 5, 1, N_val[k])
    plt.plot(t,u, label=f'N = {N_val[k]}')
plt.title('Discharge of a capacitor into a resistance - Explicit Euler Method')
plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')

plt.show()


# Version 1.1.a - Discharge of C in R with a function / with time measurement
import time
def f_disc_c_r(t, u, tau=1e-1):
    return -u/tau

def explicit_euler(f, u0, T, N):
    dt = T/N
    t = np.zeros(N+1)
    u = np.zeros(N+1)
    u[0] = u0

    for n in range(N):
        t[n+1] = t[n] + dt
        u[n+1] = u[n] + f(t[n], u[n])*dt

    return t, u

N_val = [10, 20, 50, 200, 1000]

plt.figure()
for k in range(len(N_val)):
    st = time.process_time()
    for i in range(1000):
        t, u = explicit_euler(f_disc_c_r, 5, 1, N_val[k])
    et = time.process_time()
    vt = int((et-st) * 1e3)
    plt.plot(t,u, label=f'N = {N_val[k]} - T = {vt} ms')
plt.title('Discharge of a capacitor into a resistance - Explicit Euler Method')
plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')

plt.show()


#%% Integrate parameters in f function

class C_discharge:
    def __init__(self, R, C, u0):
        self.C = C
        self.R = R
        self.u0 = u0
    def __call__(self, t, u): # f(t,u)
        return -u/(self.R*self.C)


c_disc1 = C_discharge(1e5, 1e-6, 5)
c_disc2 = C_discharge(1e5, 1e-6, 1)
c_disc3 = C_discharge(1e5, 1e-7, 5)
c_disc = [c_disc1, c_disc2, c_disc3]

plt.figure()
for k in range(len(c_disc)):
    t, u = explicit_euler(c_disc[k], c_disc[k].u0, 1, 200)
    tau_RC = c_disc[k].R * c_disc[k].C
    u0 = c_disc[k].u0
    plt.plot(t,u, label=f'RC = {tau_RC} s - u0 = {u0} V')
    
plt.title('Discharge of a capacitor into a resistance - Explicit Euler Method')
plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')


#%% Numerical method / ivp from scipy
from scipy import integrate

t0 = 0
tf = 2
t, u = explicit_euler(c_disc1, c_disc1.u0, 2, 200)
solu = integrate.solve_ivp(c_disc1, [t0, tf], [c_disc1.u0], vectorized=True)

plt.figure()
plt.plot(t, u, label='Explicit Euler Method')
plt.plot(solu.t, solu.y.flat, "+", label='ivp solver from Scipy')
plt.legend()
plt.show()

#%% Numerical method / ivp from scipy

t0 = 0
tf = 0.5
t = np.linspace(t0, tf, 1001)
solu = integrate.solve_ivp(c_disc1, [t0, tf], [c_disc1.u0], vectorized=True, t_eval=t, method='RK45')
# with a specific method and time vector

plt.figure()
plt.plot(solu.t, solu.y.flat, label='ivp solver from Scipy')
plt.legend()
plt.show()
