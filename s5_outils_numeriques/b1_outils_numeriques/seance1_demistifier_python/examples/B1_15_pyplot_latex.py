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

plt.figure()
eta = np.arange(10)
tau = np.exp(eta)
plt.plot(eta,tau,'bx-')
plt.xlabel(r'$\tau(\eta)$')
plt.ylabel(r'$\eta$')
plt.title(r'$\tau (\eta) = e^{\eta}$')
plt.show()