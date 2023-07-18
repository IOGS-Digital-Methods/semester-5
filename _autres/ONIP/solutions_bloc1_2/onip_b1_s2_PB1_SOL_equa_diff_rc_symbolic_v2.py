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
from sympy.utilities.lambdify import lambdify

#%% Linéarisation d'une fonction
x = sp.symbols('x')
g = sp.Function ('g')
g = sp.sin(x/2 + sp.sin(x))

xlin = np.linspace(-np.pi, np.pi, 21)

func_g = lambdify([x], g)
yres_g = func_g(xlin)

print(yres_g)
plt.figure()
plt.plot(xlin, yres_g)
plt.show()


#%% Fonction différentielle d'ordre 1 / RC
t = sp.symbols('t')
vs = sp.Function('Vs')(t)
equation = vs + 0.001*sp.Derivative(vs, t)

display(equation)
init_conds = {vs.subs(t,0): 5}

result = sp.dsolve(equation, vs, ics=init_conds)
vs_t = result.rhs
display(f'vs_t = {vs_t}')

t_lin = np.linspace(0, 0.01, 101)
func_vs = lambdify([t], vs_t)
yres_vs = func_vs(t_lin)

plt.figure()
plt.plot(t_lin, yres_vs)
plt.show()