#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Outils Numériques / Semestre 5 / Institut d'Optique

Calcul symbolique SymPy / Intégrales et Dérivées

Created on 15/Apr/2023

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""

import math
import sympy
from IPython.display import *


x, y = sympy.symbols('x y')
f = sympy.Function('f')

#%% Derivees

# Exemple 1
f = x**2 + y
display(f)

dfx = sympy.diff(f, x)
display(dfx)

dfy = sympy.diff(f, y)
display(dfy)

# Exemple 2
k = sympy.Function('k')
l = sympy.Function('l')
k = k(x)
l = l(x + k)
k, l

dfkl = sympy.diff(l, x)
display(dfkl)


#%% Integrales
inte_f = sympy.integrate(f, x)
display(inte_f)