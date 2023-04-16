#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Outils Numériques / Semestre 5 / Institut d'Optique

Differential Equation Resolution
- SIR model for disease propagation / Susceptible, Infected, and Recovered

Created on 15/Apr/2023

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
        
    def __call__(self,u,t):
        S, E, I, R = u
        N = S+I+R+E
        dS = -self.beta*S*I/N + self.gamma*R
        dE = self.beta*S*I/N - self.mu*E
        dI = self.mu*E - self.nu*I
        dR = self.nu*I - self.gamma*R
        return [dS,dE,dI,dR]



S0 = 1000
E0 = 0
I0 = 1
R0 = 0
model = SEIR(beta=1.0, mu=1.0/5,nu=1.0/7,gamma=1.0/50)

solver= RungeKutta4(model)
solver.set_initial_condition([S0,E0,I0,R0])

time_points = np.linspace(0, 100, 101)

t, u = solver.solve((0,100),101)
'''
S = u[:,0]; E = u[:,1]; I = u[:,2]; R = u[:,3]
plt.plot(t,S,t,E,t,I,t,R)
plt.show()
'''
