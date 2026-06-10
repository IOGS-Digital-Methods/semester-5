#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LEnsE projects / Institut d'Optique

FFT on images / Sine Trame Generator

Created on 25/Sep/2024

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

def sine_trame(height, width, step, angle):
    x = np.arange(0,height)
    y = np.arange(0,width)
    XX, YY = np.meshgrid(x, y)
    alpha_rad = np.radians(angle)
    return 0.5*(1 + np.cos(2*np.pi*XX/step*np.cos(alpha_rad) + 2*np.pi*YY/step*np.sin(alpha_rad) )) 


image1 = sine_trame(300, 200, 10, 40)
image2 = sine_trame(300, 200, 40, 40)
image3 = sine_trame(300, 200, 20, 10)
image4 = sine_trame(300, 200, 3, 80)

# Display images
plt.figure(figsize=(10, 5))
plt.imshow(image1, cmap='gray')
plt.title('Image in Gray')
plt.show()

## FFT
fft_trame = np.fft.fft2(image1)

# Display images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image1, cmap='gray')
plt.title('Original Image in Gray')

plt.subplot(1, 2, 2)
plt.imshow(np.fft.fftshift(np.abs(fft_trame)), cmap='gray')
plt.title('FFT')
plt.show()

# FFT Shift effect
image = cv2.imread('../prog/test_image.png', cv2.IMREAD_GRAYSCALE)
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image in Gray')

plt.subplot(1, 2, 2)
plt.imshow(np.fft.fftshift(image), cmap='gray')
plt.title('FFT')
plt.show()

## Comparison
# Display images
plt.figure(figsize=(10, 5))

plt.subplot(2, 2, 1)
plt.imshow(image1, cmap='gray')
plt.title('Trame - Step = 10 / Angle = 40°')

fft_trame = np.fft.fft2(image1-np.mean(image1))
plt.subplot(2, 2, 2)
plt.imshow(np.fft.fftshift(np.abs(fft_trame)), cmap='gray')
plt.title('FFT - Step = 10 / Angle = 40°')

plt.subplot(2, 2, 3)
plt.imshow(image2, cmap='gray')
plt.title('Trame - Step = 40 / Angle = 40°')

fft_trame = np.fft.fft2(image2-np.mean(image2))
plt.subplot(2, 2, 4)
plt.imshow(np.fft.fftshift(np.abs(fft_trame)), cmap='gray')
plt.title('FFT - Step = 40 / Angle = 40°')

# Display images
plt.figure(figsize=(10, 5))

plt.subplot(2, 2, 1)
plt.imshow(image3, cmap='gray')
plt.title('Trame - Step = 20 / Angle = 10°')

fft_trame = np.fft.fft2(image3-np.mean(image3))
plt.subplot(2, 2, 2)
plt.imshow(np.fft.fftshift(np.abs(fft_trame)), cmap='gray')
plt.title('FFT - Step = 20 / Angle = 10°')

plt.subplot(2, 2, 3)
plt.imshow(image4, cmap='gray')
plt.title('Trame - Step = 3 / Angle = 80°')

fft_trame = np.fft.fft2(image4-np.mean(image4))
plt.subplot(2, 2, 4)
plt.imshow(np.fft.fftshift(np.abs(fft_trame)), cmap='gray')
plt.title('FFT - Step = 3 / Angle = 80°')

plt.show()