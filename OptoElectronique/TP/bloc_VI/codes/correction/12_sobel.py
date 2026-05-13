"""12_sobel.py
Sobel gradient process with OpenCV
.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>

"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

image_gray = cv2.imread('./_data/gray_blocks.png', cv2.IMREAD_GRAYSCALE)
image_gray = cv2.imread('./_data/noise_vi_small.png', cv2.IMREAD_GRAYSCALE)

# Kernel
kernel_size = (11, 11)
# Blur
blurred_image_1 = cv2.GaussianBlur(image_gray, kernel_size, 2)

# Kernel
sobel_kernel_x1 = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_kernel_x2 = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
sobelx_1 = cv2.filter2D(image_gray, -1, sobel_kernel_x1)
sobelx_2 = cv2.filter2D(image_gray, -1, sobel_kernel_x2)

# Display images
fig, ax = plt.subplots(nrows=1, ncols=3)
ax[0].imshow(image_gray, cmap='gray')
ax[0].set_title('Initial Gray Image')
ax[1].imshow(sobelx_1, cmap='gray')
ax[1].set_title('Sobel X Gradient -> ')
ax[2].imshow(sobelx_2, cmap='gray')
ax[2].set_title('Sobel X Gradient <- ')
plt.show()


# Sobel Gradients X and Y
sobelx = cv2.Sobel(image_gray, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(image_gray, cv2.CV_64F, 0, 1, ksize=3)
sobelxb = cv2.Sobel(blurred_image_1, cv2.CV_64F, 1, 0, ksize=3)
sobelyb = cv2.Sobel(blurred_image_1, cv2.CV_64F, 0, 1, ksize=3)

# Gradient Magnitude
magnitude = cv2.magnitude(sobelx, sobely)
magnitudeb = cv2.magnitude(sobelxb, sobelyb)
# Rescale data
magnitude = cv2.convertScaleAbs(magnitude)
magnitudeb = cv2.convertScaleAbs(magnitudeb)

# Display images
fig, ax = plt.subplots(nrows=2, ncols=3)
ax[0,0].imshow(image_gray, cmap='gray')
ax[0,0].set_title('Initial Gray Image')
ax[1,0].imshow(magnitude, cmap='gray')
ax[1,0].set_title('Sobel Amplitude')
ax[0,1].imshow(sobelx, cmap='gray')
ax[0,1].set_title('Roberts X')
ax[1,1].imshow(sobely, cmap='gray')
ax[1,1].set_title('Roberts Y')
ax[0,2].imshow(blurred_image_1, cmap='gray')
ax[0,2].set_title('Blur Gray Image')
ax[1,2].imshow(magnitudeb, cmap='gray')
ax[1,2].set_title('Sobel Amplitude (Blur)')
plt.show()


# FFT
fft0 = np.fft.fftshift(np.fft.fft2(image_gray))
fft_a = np.fft.fftshift(np.fft.fft2(magnitude))
fft_b = np.fft.fftshift(np.fft.fft2(magnitudeb))
eps = 0.01

fig, ax = plt.subplots(nrows=2, ncols=3)
ax[0,0].imshow(image_gray, cmap='gray')
ax[0,0].set_title('Initial Gray Image')
ax[1,0].imshow(np.log(np.abs(fft0)+eps), cmap='gray')
ax[1,0].set_title('FFT')
ax[0,1].imshow(magnitude, cmap='gray')
ax[0,1].set_title('Sobel')
ax[1,1].imshow(np.log(np.abs(fft_a)+eps), cmap='gray')
ax[1,1].set_title('FFT')
ax[0,2].imshow(magnitudeb, cmap='gray')
ax[0,2].set_title('Sobel + Blur')
ax[1,2].imshow(np.log(np.abs(fft_b)+eps), cmap='gray')
ax[1,2].set_title('FFT')
plt.show()