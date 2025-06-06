#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Digital methods / Semester 5 / Institut d'Optique

First example of using Python for scientific purpose.
/!\ This code shows bad programming behaviors !

Created on 03/Sept/2024

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""


import numpy as nu

def fonctionA(a, b, c):
    return a * nu.sin(2*3.14 * b * c)


if __name__ == '__main__':
    a1=20
    b1=850
    c1=nu.linspace(0,50, 101)

    r1 = fonctionA(a1, b1, c1)
    print(r1)

    plt.figure()
    plt.plot(c1, r1)
    plt.show()
