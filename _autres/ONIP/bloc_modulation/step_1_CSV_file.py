#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Outils Numériques / Semestre 5 / Institut d'Optique

File Opening / CSV file

Created on 10/dec/2023

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""

import numpy as np
import matplotlib.pyplot as plt
import base64

#%% First test on files
raw_f1 = open('data/B3_data_01.csv', 'r')
print(type(raw_f1))

data1 = raw_f1.read()
print(type(data1))

raw_f2 = open('data/B3_data_02.txt', 'rb')
print(type(raw_f2))

data2 = raw_f2.read()
print(type(data2))

#%% 
x = np.array([1, 2, 2.5, 5])
print(x)
print(x.shape)
print(type(x[0]))
x2 = x.astype(np.int16)
print(x2)
print(x2.shape)
print(type(x2[0]))

#%%
data2_d = base64.b64decode(data2)
print(len(data2))
print(len(data2_d))