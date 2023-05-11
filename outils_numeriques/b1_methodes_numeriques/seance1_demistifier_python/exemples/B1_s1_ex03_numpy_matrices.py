#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Outils Numériques / Semestre 5 / Institut d'Optique

Numpy, manipulateur de matrices

Created on 26/Apr/2023

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""


#%% Premiers vecteurs
import numpy as np
x = np.array( [1,2,3] )
y = np.sin(x)

print(f'type de x : {type(x)} - shape de x : {x.shape}')
print(f'type de y : {type(y)} - shape de y : {y.shape}')

print( y )

# Que contient x ? Que contient y ?

#%% Premières matrices

mb = np.array( [[1,2,3] , [4,5,6]] )
mc = np.array( [[1,2,3] , [4,5,6]] ) 
mm = mb + mc
print( mm )

# Que contient mm ?

#%% Matrices particulières

vz = np.zeros( 10 )
print( f'shape de vz : {vz.shape}' )
print( f'valeurs de vz : {vz}' )

# A quoi sert la fonction zeros ?

#%%
mo = np.ones( (10,3) )
print( f'shape de mo : {mo.shape}' )
print( f'values de mo : {mo}' )

# A quoi sert la fonction ones ?

#%%
vlin = np.linspace( -1, 3, 21 )
vlog = np.logspace( 1, 5, 11 )
vara = np.arange( 5, step=0.5 )

# Quel est le rôle des fonctions linspace, logspace et arange ?

# TO DO

#%% Calculs sur les matrices

mb = np.array( [[1,2,3] , [4,5,6]] )

total = np.sum(mb) 
total_c = np.sum(mb, axis=0)
total_r = np.sum(mb, axis=1)

# Quel est le rôle de la fonction sum et du paramètre axis ?

# TO DO

#%%
moy = np.mean(mb) 
moy_c = np.mean(mb, axis=0)
moy_r = np.mean(mb, axis=1)

# Quel est le rôle de la fonction mean et du paramètre axis ?

# TO DO

#%% Matrices partielles
vect = np.arange( 100 ) 
vect_p = vect[ 10 : 30 ]
vect_s = vect[ 50 : ]

# A quoi servent les deux dernières instructions ?

# TO DO

#%%
mb = np.array( [[1,2,3] , [4,5,6]] )
mc = mb[ : , 1:3 ]

# A quoi sert la dernière instruction ?

# TO DO


#%% Tests sur les matrices
vect = np.arange( 100 ) 
c = vect[(vect > 2) & (vect < 11)]
tf = (vect > 2) & (vect < 11)

# Que contiennent c et tf ?

# TO DO
