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


#%% Expression avec des dérivées
# Déclaration des symboles et des fonctions
t, tau = sympy.symbols('t tau')
vs = sympy.Function('V_s')(t)

# On souhaite par la suite étudiée l'expression suivante : 𝑉𝑠(𝑡)+𝜏⋅𝑑𝑉𝑠(𝑡)𝑑𝑡=0
dvs = sympy.Derivative(vs, t)
exp = vs + tau * dvs
display(exp)

# Que donne l'affichage précédent ?


#%% Résolution d'une équation différentielle
result = sympy.dsolve(exp, vs)
vs_t = result.rhs
print(f'vs_t = {vs_t}')

# L'expression donnée est-elle juste ?

init_conds = {vs.subs(t,0): 5}
result = sympy.dsolve(exp, vs, ics=init_conds)
vs_t = result.rhs
print(f'vs_t = {vs_t}')

# Que devient l'expression dans ce nouveau cas ?