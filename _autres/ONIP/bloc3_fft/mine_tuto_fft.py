#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tutoriels MINE / Python

FFT

Created on 28/nov/2023

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""

#%%
n = 100 # sur 100 points
a = np.zeros(n)
a[1] = 1

plt.figure()
plt.plot(a, '*')
plt.show()

A = np.fft.fft(a)

plt.figure()
plt.subplot(211)
plt.plot(np.real(A))
plt.ylabel("partie reelle")
plt.subplot(212)
plt.plot(np.imag(A))
plt.ylabel("partie imaginaire")
plt.show()


#%%
n = 100
p = 5
m = np.linspace(0, 2*p*np.pi-2*np.pi/p, n)
a = np.cos(m)

plt.figure()
plt.plot(m, a)
plt.xlabel('Angle (rd)')
plt.ylabel('Cosinus')

A = np.fft.fft(a)
plt.figure()
plt.subplot(211)
plt.plot(np.abs(A), '.')
plt.ylabel('Module')
plt.subplot(212)
plt.plot(np.angle(A), '.')
plt.ylabel('Phase (rd)')
plt.show()