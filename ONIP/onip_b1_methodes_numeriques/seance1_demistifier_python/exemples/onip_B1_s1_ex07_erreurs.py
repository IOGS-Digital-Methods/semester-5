#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Outils Numériques / Semestre 5 / Institut d'Optique

Gestion des erreurs

Created on 26/Apr/2023

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""

#%% Que donne ce code selon que l'entrée que vous fournissez ?

try:
    g = int(input('Saisir un entier : '))
    a = 5/g
    print(f'g = {g} et a = {a}')
except ValueError :
    print('Vous n\'avez pas saisi un entier !')
except ZeroDivisionError :
    print('Toujours pas possible de diviser par 0 !!')
except:
    print('Erreur !!!')