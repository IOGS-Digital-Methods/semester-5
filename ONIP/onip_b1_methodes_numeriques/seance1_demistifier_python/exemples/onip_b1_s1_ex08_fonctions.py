#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Outils Numériques / Semestre 5 / Institut d'Optique

Fonctions

Created on 26/Apr/2023

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""

#%% Première Fonction
# Définition de la fonction somme
def somme(a, b):
    c = a + b
    return c

# Utilisation de la fonction somme
k = somme(2, 3)
print(k)

#%% Fonctions et vecteurs
import numpy as np

va = np.arange(10)
vb = np.arange(10)

# Que se passe-t-il si on fournit deux vecteurs à la fonction somme ?

# TO DO 

#%% Documentation des fonctions

# La création de fonctions a un intérêt dans la lecture des programmes, 
# mais également pour la réutilisation de certaines parties du code dans 
# d'autres applications.

# Lorsque vous souhaiterez revenir sur ces fonctions (d'ici quelques jours, 
# quelques mois...) ou les distribuer à des personnes tierces (collègues de 
# travail, communauté de programmeurs...), il ne sera pas évident de retrouver 
# l'objectif et le fonctionnement de ces fonctions.

# Pour faciliter cette démarche, il est indispensable de bien commenter et 
# documenter vos différentes fonctionnalités.

# Pour cela, il existe différentes conventions dont la principale est 
# l'utilisation du format docstring. Cette convention est réutilisée dans 
# différentes interfaces de développement comme Spyder ou PyCharm.

# Sous Spyder, il suffit d'introduire trois apostrophes ''' après la définition
# de la fonction, et Spyder ajoute spontanément les éléments de base

def somme(a, b):
    '''
    Return the sum of a and b

    Parameters
    ----------
    a : int or float
        first term of the addition.
    b : int or float
        second term of the addition.

    Returns
    -------
    int or float
        Return the sum of a and b.

    '''
    return a + b


print(somme(5, 6.3))

print(c)

#%% Variable globale

def show_var():
    print(z)

# z = 3
    
show_var()

