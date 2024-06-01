#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Conception Electronique / Semestre 5 / Institut d'Optique

Filtrage actif / Modélisation et simulation

Created on 10/Jul/2023

Author : Julien Villemejane / LEnsE / IOGS
"""

import numpy as np
from matplotlib import pyplot as plt


#%% Paramètres du système
H0 = 10	# Gain bande-passante
f0 = 1e4	# Frequence caractéristique
w0 = 2*np.pi*f0
m = 0.3	# Facteur d'amortissement

#%% Modele (version Numpy)
f = np.logspace(2, 6, 101)	# Vecteur des fréquences à analyser
w = 2*np.pi*f

H = H0 / (1 + 2.0j*m*w/w0 + (1.0j*w/w0)**2)

#%% Affichage
g_db_h = 20*np.log10(abs(H))
plt.figure()
plt.semilogx(f, g_db_h)
plt.grid()
plt.grid(which = "major", linewidth = 1)
plt.grid(which = "minor", linewidth = 0.2)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (dB)')
plt.title('Frequency response of a 2nd order filter')
plt.show()

#%% Réponses en fréquence pour différentes valeurs de m
m_param = np.array([0.1, 0.3, 0.7, 1.0, 1.5])

H_param = np.zeros((len(m_param), len(w)))

for k in range(len(m_param)):
	H_temp = H0 / (1 + 2.0j*m_param[k]*w/w0 + (1.0j*w/w0)**2)
	H_param[k,:] = 20*np.log10(np.abs(H_temp))

plt.figure()
for k in range(len(m_param)):
	plt.semilogx(f, H_param[k, :], label=f'm = {m_param[k]}')

plt.grid()
plt.grid(which = "major", linewidth = 1)
plt.grid(which = "minor", linewidth = 0.2)
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (dB)')
plt.title('Frequency response of a 2nd order filter')
plt.legend()
plt.show()

#%% Modele (version control)


