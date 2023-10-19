#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Outils Numériques / Semestre 5 / Institut d'Optique

Approche Système / découverte de la bibliothèque control

Created on 26/Apr/2023

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""

import numpy as np
from matplotlib import pyplot as plt

#%% Définition du système
import control as ct

num = np.array([1, -1])
den = np.array([1, -2, 1])

tf_sys = ct.tf(num, den)

print(tf_sys)

#%% Diagramme de Bode

omega = np.logspace(-2, 2, 101)

ct.bode_plot( tf_sys , omega=omega)