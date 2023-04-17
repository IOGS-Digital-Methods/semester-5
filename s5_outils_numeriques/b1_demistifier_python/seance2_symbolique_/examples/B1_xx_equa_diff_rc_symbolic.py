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

from sympy.utilities.lambdify import lambdify
func = lambdify([t, R, C], vs_t)


plt.figure()
plt.plot(t_vect, func(t_vect, 1e5, 1e-6))
