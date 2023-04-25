#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Outils Numériques / Semestre 5 / Institut d'Optique

Résolution de systèmes linéaires

Created on 25/Apr/2023

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""

import numpy as np

#%% Résolution d'équation polynomiale

# -6.x^2 - 2.x + 4 = 0

import numpy.polynomial.polynomial as nppol

X = nppol.polyroots([4, -2, -6])
print(X)

#%% Système d'équations
from scipy import linalg

A = np.array([[1, 2], [3, 4]])
b = np.array([[5], [6]])
X = linalg.solve(A, b)
print(X)