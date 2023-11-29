#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Outils Numériques / Semestre 5 / Institut d'Optique

Bonnes pratiques - Exemple 4 - Files

Created on 29/Nov/2023

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""

import time
import numpy as np
import matplotlib.pyplot as plt

#%%
time1 = time.time()

f = open("../donnees/B3_data_01.csv", "r")
cpt = 0
HEADER = 2
NB_DATA = 4000
delimiter = ','

t = np.zeros(4000)
v = np.zeros(4000)

for line in f:
    if (cpt > HEADER) and (cpt < (HEADER + NB_DATA + 1)) :
        data = line.split(delimiter)
        t[cpt-HEADER-1] = float(data[1])
        v[cpt-HEADER-1] = float(data[2])
    cpt += 1
f.close()

time2 = time.time()

print(time2-time1)

plt.figure()
plt.plot(t, v)
plt.show()

#%%
time1 = time.time()
data = np.genfromtxt("../donnees/B3_data_01.csv", delimiter=',', skip_header=2, skip_footer=6)
t = data[:,1]
v = data[:,2]
time2 = time.time()

print(time2-time1)

plt.figure()
plt.plot(t, v)
plt.show()

#%%
import pandas
time1 = time.time()
df_data = pandas.read_csv("../donnees/B3_data_01.csv", delimiter=',', header=2, skipfooter=6, engine='python')
t = df_data['Time(s)'].to_numpy()
v = df_data['Volt(V)'].to_numpy()
time2 = time.time()

print(time2-time1)

plt.figure()
plt.plot(t, v)
plt.show()