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

#%% Version Simple
# u' = -2 * u - 1

N = 5      # nombre de points
T = 2       # durée totale (en seconde)
dt = T/N    # pas d'intégration
u0 = 10      # condition initiale

# Creation des vecteurs temps et solution de l'equation
t = np.zeros(N+1)
u = np.zeros(N+1)

u[0] = u0

for n in range(N):
    t[n+1] = t[n] + dt
    u[n+1] = u[n] + dt * (-2 * u[n] - 1)

# Que donne ce bloc d'instruction ?

# TO DO

#%% Version avec fonction

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

t1, u1 = explicit_euler(F, 10, 2, 21)

# Que donne ce bloc d'instruction ?
# Affichez les deux courbes sur un même graphique pour comparer.

# TO DO
