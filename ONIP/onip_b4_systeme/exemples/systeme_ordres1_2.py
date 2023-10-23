#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module Outils Numériques / Semestre 5 / Institut d'Optique

Approche Système / Systèmes du 1er et 2nd ordre

Created on 19/Oct/2023

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""

import control
import numpy as np
from matplotlib import pyplot as plt


def diag_bode(sys, omega=None, labels=None, filename=None):
    fig, axs = plt.subplots(2, 1)
    fig.suptitle('Frequency Response')
    axs[0].set_ylabel('Magnitude (dB)')
    axs[0].set_xscale('log')
    axs[0].grid(which="major", linewidth=1.0)
    axs[0].grid(which="minor", linewidth=0.2)
    axs[0].minorticks_on()

    axs[1].set_ylabel('Phase (rd)')
    axs[1].set_xlabel('Pulsation (rd/s)')
    axs[1].set_xscale('log')
    axs[1].grid(which="major", linewidth=1.0)
    axs[1].grid(which="minor", linewidth=0.2)
    axs[1].minorticks_on()
    k = 0
    for system in sys:
        k += 1
        if omega is None:
            Gmag, Gphase, Gomega = control.bode_plot(system, plot=False)
        else:
            Gmag, Gphase, Gomega = control.bode_plot(system, plot=False, omega=omega)

        if labels is not None:
            axs[0].plot(Gomega, 20 * np.log10(Gmag), label=labels[k - 1])
        else:
            axs[0].plot(Gomega, 20 * np.log10(Gmag))
        axs[1].plot(Gomega, Gphase)

    if labels is not None:
        axs[0].legend()

    if filename is not None:
        plt.savefig(filename)
    plt.show()


def step_sys(sys, time=None, labels=None, filename=None):
    plt.figure()
    plt.title('Step response')
    k = 0
    for system in sys:
        k += 1
        if time is None:
            t, step = control.step_response(system)
        else:
            t, step = control.step_response(system, T=time)

        if labels is not None:
            plt.plot(t, step, label=labels[k-1])
        else:
            plt.plot(t, step)
    plt.grid()
    plt.xlabel('Time (s)')
    plt.ylabel('Step (V)')
    plt.legend()
    if filename is not None:
        plt.savefig(filename)
    plt.show()


# Systeme ordre 1
w0 = 1000

w_log = np.logspace(1, 5, 1001)
t_lin = np.linspace(0, 0.01, 1001)

num1l = np.array([1])
num1h = np.array([1 / w0, 0])
den1 = np.array([1 / w0, 1])

tf1l = control.tf(num1l, den1)
tf1h = control.tf(num1h, den1)

diag_bode([tf1l, tf1h], omega=w_log, labels=['First Order Low-pass Filter', 'First Order High-pass Filter'],
          filename='ceti_first_order_bode.png')

step_sys([tf1l, tf1h], time=t_lin, labels=['First Order Low-pass Filter', 'First Order High-pass Filter'],
          filename='ceti_first_order_step.png')


# Systeme ordre 2
m = [0.01, 0.1, 0.707, 1.1, 2.0]
t_lin = np.linspace(0, 0.03, 1001)

systems = []
labels = []

for k in m:
    num2 = np.array([1])
    den2 = np.array([1 / (w0 * w0), 2 * k / w0, 1])

    tf2 = control.tf(num2, den2)
    systems.append(tf2)
    labels.append(f'm = {k}')

diag_bode(systems, omega=w_log, labels=labels, filename='ceti_second_order_bode.png')

step_sys(systems, time=t_lin, labels=labels,
          filename='ceti_second_order_step.png')
