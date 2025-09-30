#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LEnsE projects / Institut d'Optique

FFT on images / Test of circular mask

Created on 25/Sep/2024

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

def circular_mask(radius, image, inverted=False):
    h, w = image.shape
    center_y, center_x = h // 2, w // 2
    Y, X = np.ogrid[:h, :w]
    # Distance from center to pixel
    dist_from_center = np.sqrt((X - center_x)**2 + (Y - center_y)**2)
    if inverted:
        # Create a circular mask (0 inside the circle, 1 outside)
        mask = dist_from_center > radius
    else:
        # Create a circular mask (1 inside the circle, 0 outside)
        mask = dist_from_center <= radius
    return image * mask


def rectangular_mask(image, x_center, y_center, width, height,
                     inverted: bool = False):
    mask = np.zeros_like(image)
    x_0 = x_center - height//2
    x_1 = x_center + height//2
    y_0 = y_center - width//2
    y_1 = y_center + width//2
    if x_0 < 0 or x_1 > image.shape[0]:
        return None
    if y_0 < 0 or y_1 > image.shape[1]:
        return None
    mask[x_0:x_1, y_0:y_1] = 1
    if inverted:
        mask = mask < 0.5
    else:
        mask = mask > 0.5
    return image * mask

# Random 2D array / image
image = cv2.imread('../prog/test_image.png', cv2.IMREAD_GRAYSCALE)

# Process FFT
fft_image = np.fft.fft2(image)
fft_shifted = np.fft.fftshift(fft_image)
# Process masked on FFT
masked_spectrum = circular_mask(20, fft_shifted)
masked_spectrum = circular_mask(20, fft_shifted, inverted=True)
x_center = fft_shifted.shape[0] //2
y_center = fft_shifted.shape[1] //2
masked_spectrum = rectangular_mask(fft_shifted, x_center, y_center, 200, 30)
masked_spectrum = rectangular_mask(fft_shifted, x_center, y_center, 200, 30, inverted=True)
# Process inverse FFT
fft_shifted_inv = np.fft.ifftshift(masked_spectrum)
new_image = np.fft.ifft2(fft_shifted_inv)



# Display
magnitude_spectrum = np.abs(fft_shifted)
log_magnitude_spectrum = np.log(1 + magnitude_spectrum)
magnitude_masked_spectrum = np.abs(masked_spectrum)
log_masked_spectrum = np.log(1 + magnitude_masked_spectrum)





# Display images
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image in Gray')

plt.subplot(1, 2, 2)
plt.imshow(np.real(new_image), cmap='gray')
plt.title('New Image in Gray')


# Display FFT
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("FFT original image")
plt.imshow(log_magnitude_spectrum, cmap='gray')

plt.subplot(1, 2, 2)
plt.title("Masked FFT")
plt.imshow(log_masked_spectrum, cmap='gray')

# Display original image and FFT
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image in Gray')

plt.subplot(1, 2, 2)
plt.title("FFT original image")
plt.imshow(log_magnitude_spectrum, cmap='gray')

plt.show()
