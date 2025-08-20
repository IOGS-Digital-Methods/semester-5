#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Digital methods / Semester 5 / Institut d'Optique

Create and use array, from Numpy

Created on 03/Nov/2024

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""

import numpy as np
from matplotlib import pyplot as plt

# Parameters
N, M = 5, 3

## 1D array
# Zeros array
vect = np.zeros(N)
print(vect)

# Ones array
vect = np.ones(N)
print(vect)



## 2D array
array = np.zeros((N,M))
print(array.shape)
print(array)


## Random array
# 1D 
vect_r = np.random.rand(5)  # 5x1 array filled with
# real elements from 0.0 to 1.0 following a uniform distribution
print(vect_r)

# 2D 
data_uni = np.random.rand(2,4) # 2x4 array filled with
# real elements from 0.0 to 1.0 following a uniform distribution
print(data_uni.shape)
print(data_uni)

data_gaus = np.random.randn(3, 3)  # 3x3 array filled with
# values following a normal/gaussian distribution
print(data_gaus.shape)
print(data_gaus)

data_int = np.random.randint(1, 100, size=(5, 5)) # 5x5 array filled with
# integer values following a uniform distribution
print(data_int.shape)
print(data_int)


## Histogram processing
def display_histo(data: np.ndarray, nb_bins: int=10, title=None):
    data_flat = data.flatten()
    plt.figure()
    plt.hist(data_flat, bins=nb_bins, edgecolor='black')  # bins=10 pour 10 intervalles
    plt.xlabel('Values')
    plt.ylabel('Frequencies')
    if title is None:
        plt.title('Histogram')
    else:
        plt.title(title)
        
display_histo(np.random.rand(10000), nb_bins=100, title='Uniform Distribution')
display_histo(np.random.randn(10000), nb_bins=100, title='Gaussian Distribution')

#plt.show()


## Conditionals with arrays
data = np.random.randint(0, 10, size=(10))
k = ((data >= 4) & (data < 8))
print(data)
print(k)

print(k * data)


##### BAD BEHAVIORS !!!
data = np.random.randint(0, 100, size=(20,5))
# Filling arrays
v1 = []
v2 = []
for i in range(len(data)):
    v1.append(data[i, 1])
    v2.append(data[i, 2])

print(v1)

v1_b = [data[i, 1] for i in range(len(data))]
print(v1_b)