#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Outils Numériques / Semestre 5 / Institut d'Optique

Bonnes pratiques - Exemple 1

Created on 29/Nov/2023

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""

import time


#%%
N = 1000
time1 = time.time()
for k in range(1000):
    vect = []
    for i in range(N):
    	vect.append(0)
time2 = time.time()
print(type(vect))
print((time2-time1)/1000)
    
#%%
import numpy as np
N = 1000
time1 = time.time()
for k in range(100000):
    vect = np.zeros(N)
time2 = time.time()
print(type(vect))
print((time2-time1)/100000)
