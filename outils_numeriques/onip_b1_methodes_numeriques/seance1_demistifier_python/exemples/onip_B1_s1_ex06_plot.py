#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Outils Numériques / Semestre 5 / Institut d'Optique

Affichage / Rendu avec LaTeX

Created on 25/Apr/2023

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""

import numpy as np
from matplotlib import pyplot as plt

#%%
theta1 = np.linspace(0, 2*np.pi, 14)
y1 = np.sin(theta1)
theta2 = np.linspace(0, 2*np.pi, 101)
y2 = np.sin(theta2)


plt.figure()
plt.plot(theta1, y1, '*', label='14 points')
plt.plot(theta2, y2, label='101 points')
plt.xlabel(r'$\theta$  (rd)')
plt.ylabel(r'fonction $\sin(\theta)$')
plt.legend()
plt.show()
