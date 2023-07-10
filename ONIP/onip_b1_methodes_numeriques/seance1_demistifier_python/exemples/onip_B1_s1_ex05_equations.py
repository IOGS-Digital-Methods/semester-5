#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Outils Numériques / Semestre 5 / Institut d'Optique

Equations polynomiales et systèmes d'équations

Created on 26/Apr/2023

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""

#%% Résolution d'équation polynomiale

import numpy.polynomial.polynomial as nppol

# On cherche à résoudre l'équation : -6 x^2 - 2 x + 4 = 0

X = nppol.polyroots( [ 4, -2, -6] )
print( X )

# Que vaut X ?

#%% Système d'équations
import numpy as np
from scipy import linalg

# Résoudre le système d'équations suivant :
    #   x + 2 y = 5
    #   3 x + 4 y = 6

A = np.array([[1, 2], [3, 4]])
b = np.array([[5], [6]])

X = linalg.solve(A, b)
print(X)
