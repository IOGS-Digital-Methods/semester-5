#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Outils Numériques / Semestre 5 / Institut d'Optique

Calcul symbolique SymPy - Expressions

Created on 15/Apr/2023

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""

import math
import sympy
from IPython.display import *

#%% Premiers essais
print(math.sqrt(9))
print(math.sqrt(8))

display(sympy.sqrt(9))
print(sympy.sqrt(8))
display(sympy.sqrt(8))

# Quelle différence entre print et display ?
# Quelle différence entre math.sqrt(8) et sympy.sqrt(8)

#%% Nombres rationnels
m = 3/2
print(m)

k = sympy.Rational(3,2)
print(k)
display(k)

#%% Expressions
x, y = sympy.symbols('x y')
expr = x**2 - 4 * x + 5
display(expr)

val = expr.subs(x, 1)
print(val)

# Que contient expr ?
# A quoi sert la fonction subs ?

#%% Développer et factoriser
poly = x*expr
display(poly)

poly_exp = sympy.expand(poly)
display(poly_exp)

poly_fact = sympy.factor(poly_exp)
display(poly_fact)

# Que contiennent les expressions poly_exp et poly_fact ?
# A quoi servent les fonctions expand et factor ?

