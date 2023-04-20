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
from IPython.display import *

import scipy 

#%% Definition of symbols
t, R, C = sp.symbols('t R C')
vs = sp.Function('V_s')(t)
init_conds = {vs.subs(t,0): 5}

#%% Differential equation
equation = (sp.Derivative(vs,t) + 1/(R*C)*vs)
print(equation)

result = sp.dsolve(equation, vs, ics=init_conds)
vs_t = result.rhs
print(f'vs_t = {vs_t}')

# Evaluation of the result in different points
t_vect = np.linspace(0,1,1001)

from sympy.utilities.lambdify import lambdify
func = lambdify([t, R, C], vs_t)


plt.figure()
plt.plot(t_vect, func(t_vect, 1e5, 1e-6))


#%% Differential equation - Forced Regime / Sinus

ve = sp.Function('V_e')(t)
ve = sp.sin(10*t)

equation = (sp.Derivative(vs, t) + 1/(R*C)*(vs - ve))
print(equation)

init_conds = {vs.subs(t,0): 0}

result = sp.dsolve(equation, vs, ics=init_conds)
vs_t = result.rhs
print(f'vs_t = {vs_t}')

# Evaluation of the result in different points
t_vect = np.linspace(0, 10, 1001)

from sympy.utilities.lambdify import lambdify
func = lambdify([t, R, C], vs_t)

# Display
plt.figure()
plt.plot(t_vect, func(t_vect, 1e5, 1e-6))