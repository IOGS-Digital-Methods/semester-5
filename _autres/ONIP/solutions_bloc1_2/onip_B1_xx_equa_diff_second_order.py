#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Outils Numériques / Semestre 5 / Institut d'Optique

Differential Equation Resolution
- RC circuit - Discharge of C in R with initial voltage

Created on 15/Apr/2023

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""

import numpy as np
from matplotlib import pyplot as plt

from scipy import integrate


class RLC_forced:
    def __init__(self, R, L, C, Ve):
        self.R = R
        self.L = L
        self.C = C
        self.Ve = Ve
    def __call__(self, t, y):
        Vs = y[0]
        u = y[1]
        return [u, -self.R/self.L*u - (Vs - self.Ve(t)) / (self.L*self.C)]

class sinus_sig:
    def __init__(self, f, A=1):
        self.f = f
        self.A = A
    def __call__(self, t):
        return self.A * np.sin(2*np.pi*self.f*t)

class step_sig:
    def __init__(self, A=1):
        self.A = A
    def __call__(self, t):
        return self.A

# Sine
sinus = sinus_sig(20)
# Equations
rlc_forced = RLC_forced(1e2, 1e-3, 1e-4, sinus)
rlc_step = RLC_forced(1e2, 1e-3, 1e-4, step_sig())

t0 = 0
tf = 0.1
t = np.linspace(t0, tf, 101)

solu_forced = integrate.solve_ivp(rlc_forced, [t[0], t[-1]], y0=[0,0], t_eval=t)
solu_step = integrate.solve_ivp(rlc_step, [t[0], t[-1]], y0=[0,0], t_eval=t)


# Display
plt.figure()
plt.plot(solu_forced.t, solu_forced.y[0].T, label='Sine Response')
plt.plot(t, sinus(t), label='Sine input')
plt.plot(solu_step.t, solu_step.y[0].T, label='Step Response')
plt.legend()
plt.show()




#%% Integrate parameters in f function

class C_discharge:
    def __init__(self, R, C, u0):
        self.C = C
        self.R = R
        self.u0 = u0
    def __call__(self, t, u): # f(t,u)
        return -u/(self.R*self.C)

class second_order_low_pass:
    '''
    Second order low pass model with differential equation
    We asssume that Ve = 1 at t = 0 (step response)
    '''
    def __init__(self, G0, w0, m, u0):
        self.G0 = G0
        self.w0 = w0
        self.m = m
        self.u0 = u0
        
    def __call__(self, t, u): # f(t,u)
        return (u[1], (self.G0 - u[0])*self.w0**2 - 2*self.m*self.w0*u[1])


#%% Numerical method / ivp from scipy
from scipy import integrate

sec_order = second_order_low_pass(1, 1e3, 0.1, [0,0])
print(sec_order.u0)
t0 = 0
tf = 0.1
t = np.linspace(t0, tf, 1001)
solu = integrate.solve_ivp(sec_order, [t0, tf], sec_order.u0, vectorized=True, t_eval=t, method='RK45')

y = solu.y[0,:]

plt.figure()
plt.plot(solu.t, y, label='ivp solver from Scipy')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.legend()
plt.show()


#%% Parametric

m_crit = 1/np.sqrt(2)
m = [m_crit*100, m_crit*10, m_crit, m_crit/5, m_crit/50]

plt.figure()
for k in range(len(m)):
    sec_order = second_order_low_pass(1, 1e3, m[k], [0,0])
    solu = integrate.solve_ivp(sec_order, [t0, tf], sec_order.u0, vectorized=True, t_eval=t, method='RK45')
    y = solu.y[0,:]
    plt.plot(solu.t, y, label=f'Step response - m={np.round(m[k], decimals=3)}')
plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.show()
