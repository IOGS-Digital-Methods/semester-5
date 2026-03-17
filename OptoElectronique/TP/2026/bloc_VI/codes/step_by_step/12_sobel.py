"""12_sobel.py
Sobel gradient process with OpenCV
.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>

"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

image_gray = cv2.imread('./_data/gray_blocks.png', cv2.IMREAD_GRAYSCALE)

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

# Gradient Magnitude
magnitude = cv2.magnitude(sobelx, sobely)
# Rescale data
magnitude = cv2.convertScaleAbs(magnitude)

# Display images
fig, ax = plt.subplots(nrows=1, ncols=2)
ax[0].imshow(image_gray, cmap='gray')
ax[0].set_title('Initial Gray Image')
ax[1].imshow(magnitude, cmap='gray')
ax[1].set_title('Sobel Process')
plt.show()