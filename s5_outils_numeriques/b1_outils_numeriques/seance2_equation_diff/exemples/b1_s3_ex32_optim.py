#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Outils Numériques / Semestre 5 / Institut d'Optique

Méthode d'EUler / Premier exemple

Created on 26/Apr/2023

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""

import numpy as np
from matplotlib import pyplot as plt

#%% Version avec fonction
# u' = -2 * u - 1

def F(t, u):
    return -2*u-1

def explicit_euler(f, u0, T, N):
    dt = T/N
    t = np.zeros(N+1)
    u = np.zeros(N+1)
    u[0] = u0

    for n in range(N):
        t[n+1] = t[n] + dt
        u[n+1] = u[n] + f(t[n], u[n])*dt

    return t, u

t1, u1 = explicit_euler(F, 10, 2, 100)
plt.figure()
plt.plot(t1, u1, label='version F')
plt.legend()

#%% Integrer des paramètres in f function
# u' = k * u + m

class F_km:
    def __init__(self, k, m, u0):
        self.k = k
        self.m = m
        self.u0 = u0
    def __call__(self, t, u): # f(t,u)
        return self.k*u+self.m
    
    
newF = F_km(-2, -1, 8)
tF, uF = explicit_euler(newF, newF.u0, 2, 100)

# Que donne ce bloc d'instruction ?
# Affichez la courbe uF en fonction de tF

# TO DO

# Comparez les résultats pour différentes valeurs de k, m et u0

# TO DO