#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Outils Numériques / Semestre 5 / Institut d'Optique

Bonnes pratiques - Exemple 2

Created on 29/Nov/2023

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""

import time
import numpy as np

data = np.random.rand(1000,5)
print(data.shape)
print(type(data[1,1]))


#%%
time1 = time.time()
for k in range(1000):
    v1 = []
    v2 = []
    for i in range(len(data)):
        v1.append(data[i, 1])
        v2.append(data[i, 2])
time2 = time.time()
print(type(v1))
print((time2-time1)/1000)
    
#%%
time1 = time.time()
for k in range(100000):
    v1 = data[:,1]
    v2 = data[:,2]
time2 = time.time()
print(type(v1))
print((time2-time1)/100000)