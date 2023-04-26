#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Outils Numériques / Semestre 5 / Institut d'Optique

Calcul symbolique SymPy

Created on 15/Apr/2023

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""

import math
import sympy
from IPython.display import *

x, y = sympy.symbols('x y')

#%% Fonctions
f = sympy.Function('f')
f = x**2 + y
display(f)

display(f.subs(x, 4))
display(f.subs(y, 1))
print(f.subs({x:1, y: 2}))

# Pourquoi est-il préférable d'utiliser display dans les 
# deux premiers cas ? Et print dans le dernier cas ?

#%% Vectorisation
g = sympy.Function('g')
g = sympy.sin(x/2 + sympy.sin(x))
display(g)

# On souhaite afficher cette fonction sur l'intervalle 
# [−𝜋,𝜋]
import numpy as np
xlin = np.linspace(-np.pi, np.pi, 21)

result = g.subs(x, xlin)
display(result)

# Que donnents les instructions précédentes ?

print(type(result))

#%% Transformation en fonction
from sympy.utilities.lambdify import lambdify
func = lambdify([x], g)

print(type(func))

yres = func(xlin)
print(type(yres))
print(yres.shape)

# A quoi correspond yres ?
# Affichez la fonction g(x) en fonction de xlin



