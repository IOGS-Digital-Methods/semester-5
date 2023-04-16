# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 10:10:42 2023

@author: Villou
"""

import numpy as np

'''
'''
class ODESolver:
    def __init__(self, f):
        '''
        

        Parameters
        ----------
        f : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        # Wrap user’s f in a new function that always
        # converts list/tuple to array (or let array be array)
        self.f = lambda t, u: np.asarray(f(t,u), float)
        
    def set_initial_condition(self, u0):
        '''
        Set the initial condition of the model.

        Parameters
        ----------
        u0 : float
            Initial condition of the function.

        Returns
        -------
        None.

        '''
        if isinstance(u0, (float,int)): # scalar ODE
            self.neq = 1 # no of equations
            u0 = float(u0)
        else: # system of ODEs
            u0 = np.asarray(u0)
            self.neq = u0.size # no of equations
        self.u0 = u0
        
    def solve(self,t_span, N):
        '''
        Compute solution for the values of t_vect.

        Parameters
        ----------
        t_span : tuple float
            Time initial Value and Time final value.
        N : int
            Number of steps.

        Returns
        -------
        None.

        '''
        t0,T = t_span
        self.dt = T/N
        self.t = np.zeros(N+1) #N steps ~ N+1 time points
        if self.neq == 1:
            self.u = np.zeros(N+1)
        else:
            self.u = np.zeros((N+1,self.neq))
        self.t[0] = t0
        self.u[0] = self.u0
        for n in range(N):
            self.n = n
            self.t[n+1] = self.t[n] + self.dt
            self.u[n+1] = self.advance()
        return self.t, self.u
    
    
class ForwardEuler(ODESolver):
    def advance(self):
        u, f, n, t = self.u, self.f, self.n, self.t
        dt = self.dt
        unew = u[n] + dt*f(t[n], u[n])
        return unew
    
class ExplicitMidpoint(ODESolver):
    def advance(self):
        u, f, n, t = self.u, self.f, self.n, self.t
        dt = self.dt
        dt2 = dt/2.0
        k1 = f(t[n], u[n])
        k2 = f(t[n] + dt2, u[n] + dt2*k1)
        unew = u[n] + dt*k2
        return unew

class RungeKutta4(ODESolver):
    def advance(self):
        u, f, n, t = self.u, self.f, self.n, self.t
        dt = self.dt
        dt2 = dt/2.0
        k1 = f(t[n], u[n], )
        k2 = f(t[n] + dt2, u[n] + dt2*k1, )
        k3 = f(t[n] + dt2, u[n] + dt2*k2, )
        k4 = f(t[n] + dt, u[n] + dt*k3, )
        unew = u[n] + (dt/6.0)*(k1 + 2*k2 + 2*k3 + k4)
        return unew
    
