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

#%% Limites de fonctions
g = sympy.Function('g')
g = sympy.sin(x/2 + sympy.sin(x))
display(g)

lg = sympy.limit(g, x, sympy.pi)
print(lg)


#%% Limites en 0+, 0- ou +infini
h = sympy.Function('h')(x)
h = 2*sympy.exp(1/x)/(sympy.exp(1/x)+1)
display(h)

# Limite en 0+ de h(x)
lhplus = sympy.limit(h, x, 0, dir='+')
print(lhplus)

# Limite in 0- de h(x)
lhmoins = sympy.limit(h, x, 0, dir='-')
print(lhmoins)
print('\n')

# Limite de m(x) en +infini
m = sympy.Function('m')(x)
m = (sympy.cos(x)-1)/x
display(m)
print(f'Valeur en x=1 : ')
display(m.subs(x, 1))
print(f'Valeur en x=1 : {m.subs(x, 1).evalf()}')
lm = sympy.limit(m, x, sympy.oo)
print(f'Limite en +inf = {lm}')

