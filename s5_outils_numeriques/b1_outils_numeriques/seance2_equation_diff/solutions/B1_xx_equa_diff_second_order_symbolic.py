#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Outils Numériques / Semestre 5 / Institut d'Optique

Differential Equation Resolution - Euler Methods
- RC circuit - Discharge of C in R with initial voltage

Created on 20/Apr/2023

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""

import sympy
from IPython.display import *

import numpy as np
from matplotlib import pyplot as plt

#%% First test
t, m = sympy.symbols('t m')
x = sympy.Function('x')(t)
equation = x.diff(t,2)-x-sympy.sin(t)
display(equation)
print(equation)

init_conds = {x.subs(t,0): 2, x.diff().subs(t,0):-8}

xsol=sympy.dsolve(equation,x, ics=init_conds).rhs
display(xsol)

# Test
# First initial condition
print(xsol.subs(t, 0))
# Second initial condition
print(xsol.diff().subs(t,0))

# Display
func = sympy.lambdify([t], xsol)
t = np.linspace(0, 1, 1001)
ft = func(t)
plt.figure()
plt.plot(t, ft)
plt.show()


#%% Second order filter / RLC
t, R, C, L = sympy.symbols('t R C L')
Vc = sympy.Function('V_c')(t)
Ve = sympy.Function('V_e')(t)

Ve = sympy.sin(10*t)

eqRLC = Vc + R*C * Vc.diff(t, 1) + L*C*Vc.diff(t, 2) - Ve
display(eqRLC)

# Initial Conditions
init_conds = {Vc.subs(t,0): 0, Vc.diff().subs(t,0):0}

# Resolution
xsol=sympy.dsolve(eqRLC, Vc, ics=init_conds).rhs
display(xsol)

# Display
func = sympy.lambdify([t, R, C, L], xsol)
t = np.linspace(0, 10, 1001)
ft = func(t, 1e3, 1e-6, 1e-3)
plt.figure()
plt.plot(t, ft)
plt.show()