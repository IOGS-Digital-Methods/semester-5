"""10_blur_mean.py
Blur and mean on images with OpenCV
.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>

@see: https://iogs-lense-training.github.io/image-processing/contents/opencv_blur.html
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Image
image = cv2.imread('./_data/noise_vi_small.png', cv2.IMREAD_GRAYSCALE)
plt.figure()
plt.imshow(image, cmap='gray')
plt.show()

# Kernel
kernel_size = (11, 11)
# Blur
blurred_image_1 = cv2.GaussianBlur(image, kernel_size, 2)
blurred_image_2 = cv2.blur(image, kernel_size)

# Display images
fig, ax = plt.subplots(nrows=2, ncols=3)
ax[0,0].imshow(image, cmap='gray')
ax[0,0].set_title('Initial Gray Image / Filter')
ax[0,1].imshow(blurred_image_1, cmap='gray')
ax[0,1].set_title('Gaussian Blur')
ax[0,2].imshow(blurred_image_2, cmap='gray')
ax[0,2].set_title('Box blur')

ax[1,1].imshow(image - blurred_image_1, cmap='gray')
ax[1,1].set_title('Gaussian Blur')
ax[1,2].imshow(image - blurred_image_2, cmap='gray')
ax[1,2].set_title('Box blur')

plt.show()
