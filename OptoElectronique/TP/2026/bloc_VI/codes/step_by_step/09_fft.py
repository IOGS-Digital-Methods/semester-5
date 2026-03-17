"""09_fft.py
Blur and mean on images with OpenCV
.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>

@see: https://iogs-lense-training.github.io/image-processing/contents/opencv_blur.html
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
from images_manipulation import *

# Image
image = cv2.imread('./_data/robot.jpg', cv2.IMREAD_GRAYSCALE)
plt.figure()
plt.imshow(image, cmap='gray')

# FFT
fft_image = np.fft.fftshift(np.fft.fft2(image))

plt.figure()
plt.imshow(np.log(np.abs(fft_image)+0.001), cmap='gray')

## MASK ON FFT
radius = 20
fft_mask = circular_mask(radius, fft_image)

plt.figure()
plt.imshow(np.log(np.abs(fft_mask)+0.001), cmap='gray')
plt.show()

new_image = np.fft.ifft2(np.fft.ifftshift(fft_mask))

# Display images
fig, ax = plt.subplots(nrows=2, ncols=2)
ax[0,0].imshow(image, cmap='gray')
ax[0,0].set_title('Initial Gray Image')
ax[0,1].imshow(np.log(np.abs(fft_image)+0.001), cmap='gray')
ax[0,1].set_title('FFT of Initial Gray Image')
ax[1,0].imshow(np.abs(new_image), cmap='gray')
ax[1,0].set_title('New Gray Image')
ax[1,1].imshow(np.log(np.abs(fft_mask)+0.001), cmap='gray')
ax[1,1].set_title('FFT of Initial Gray Image')
plt.show()


