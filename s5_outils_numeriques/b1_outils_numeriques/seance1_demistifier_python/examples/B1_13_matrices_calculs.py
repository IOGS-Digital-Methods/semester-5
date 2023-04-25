#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Outils Numériques / Semestre 5 / Institut d'Optique

Matrices / Calculs sur les matrices

Created on 25/Apr/2023

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""

import numpy as np

mb = np.array( [[1,2,3] , [4,5,6]] )

print(f'shape of mb : {mb.shape}')

#%% Somme sur des matrices
total = np.sum(mb)
print(f'total = {total}')
total_c = np.sum(mb, axis=0)
print(f'total_c = {total_c}')
total_r = np.sum(mb, axis=1)
print(f'total_r = {total_r}')

#%% Moyenne sur des matrices
moy = np.mean(mb)
print(f'moy = {moy}')
moy_c = np.mean(mb, axis=0)
print(f'moy_c = {moy_c}')
moy_r = np.mean(mb, axis=1)
print(f'moy_r = {moy_r}')