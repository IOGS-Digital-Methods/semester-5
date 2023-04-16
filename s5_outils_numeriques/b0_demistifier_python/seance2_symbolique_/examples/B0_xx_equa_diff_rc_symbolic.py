#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Outils Numériques / Semestre 5 / Institut d'Optique

Differential Equation Resolution - Symbolic
- RC circuit - Discharge of C in R with initial voltage

Created on 15/Apr/2023

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""
import numpy as np
from matplotlib import pyplot as plt
import sympy as sp
from sympy import *
import scipy 

#%% Definition of symbols
t, R, C = sp.symbols('t R C')
vs = sp.Function('V_s')
init_conds = {vs(0): 5}

#%% Differential equation
equation = (sp.Derivative(vs(t),t) + 1/(R*C)*vs(t))
print(equation)

result = sp.dsolve(equation, vs(t), ics=init_conds)
vs_t = result.rhs
print(f'vs_t = {vs_t}')

# Evaluation of the result in different points
t_vect = np.linspace(0,1,1001)
vs_t_final = np.zeros(len(t_vect))

for k in range(len(t_vect)):
    vs_t_final[k] = vs_t.evalf(subs={t:t_vect[k], R:1e5, C:1e-6})

plt.figure()
plt.plot(t_vect, vs_t_final)
