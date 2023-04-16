#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Outils Numériques / Semestre 5 / Institut d'Optique

Differential Equation Resolution
- SEIR model for disease propagation / 
    Susceptible, Exposed, Infected, and Recovered

Created on 16/Apr/2023

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
@see : ode_book.pdf - part 5
"""

from ODESolver import RungeKutta4
import numpy as np
import matplotlib.pyplot as plt

class SEIR:
    def __init__(self, beta, mu, nu, gamma):
        self.beta = beta
        self.mu = mu
        self.nu = nu
        self.gamma = gamma
        
    def __call__(self, t, u):
        S, E, I, R = u
        N = S+I+R+E
        dS = -self.beta*S*I/N + self.gamma*R
        dE = self.beta*S*I/N - self.mu*E
        dI = self.mu*E - self.nu*I
        dR = self.nu*I - self.gamma*R
        return [dS,dE,dI,dR]



S0 = 7e7
E0 = 0
I0 = 1
R0 = 0
model = SEIR(beta=1.0, mu=1.0/10,nu=1.0/7,gamma=1.0/50)

solver= RungeKutta4(model)
solver.set_initial_condition([S0,E0,I0,R0])

TF = 500
N = 1000

time_points = np.linspace(0, TF, N)

t, u = solver.solve((0,TF),N)

S = u[:,0]; E = u[:,1]; I = u[:,2]; R = u[:,3]
plt.plot(t,S, label='Susceptible')
plt.plot(t,E, label='Exposed')
plt.plot(t,I, label='Infected')
plt.plot(t,R, label='Recovered')
plt.legend()
plt.show()

