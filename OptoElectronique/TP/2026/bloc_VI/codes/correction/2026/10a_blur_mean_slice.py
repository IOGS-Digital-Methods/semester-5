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

# Kernel
kernel_size = (11, 11)
# Blur
blurred_image_1 = cv2.GaussianBlur(image, kernel_size, 2)
blurred_image_2 = cv2.blur(image, kernel_size)

# Slice
line_number = 300
# Display Slice
fig, ax = plt.subplots(nrows=2, ncols=3)
ax[0,0].plot(image[line_number,:])
ax[0,0].set_title('Initial Gray Image / Filter')
ax[0,1].plot(blurred_image_1[line_number,:])
ax[0,1].set_title('Gaussian Blur')
ax[0,2].plot(blurred_image_2[line_number,:])
ax[0,2].set_title('Box blur')

ax[1,0].imshow(image, cmap='gray')
ax[1,0].set_title('Initial Gray Image / Filter')
ax[1,0].axhline(y=line_number, color='red', linewidth=2)
ax[1,1].imshow(image - blurred_image_1, cmap='gray')
ax[1,1].set_title('Gaussian Blur')
ax[1,1].axhline(y=line_number, color='red', linewidth=2)
ax[1,2].imshow(image - blurred_image_2, cmap='gray')
ax[1,2].set_title('Box blur')
ax[1,2].axhline(y=line_number, color='red', linewidth=2)
plt.show()


##
# Slice Gradient
dy1 = np.gradient(blurred_image_1[line_number,:].astype(float))
dy2 = np.gradient(blurred_image_2[line_number,:].astype(float))

# Display Slice Gradient
fig, ax = plt.subplots(nrows=2, ncols=3)
ax[0,0].plot(image[line_number,:])
ax[0,0].set_title('Initial Gray Image / Filter')
ax[0,1].plot(blurred_image_1[line_number,:])
ax[0,1].set_title(f'Gaussian Blur')
ax[0,2].plot(blurred_image_2[line_number,:])
ax[0,2].set_title(f'Box blur')

ax[1,0].imshow(image, cmap='gray')
ax[1,0].set_title('Initial Gray Image / Filter')
ax[1,0].axhline(y=line_number, color='red', linewidth=2)
ax[1,1].plot(dy1)
ax[1,1].set_title(f'Gaussian Blur')
ax[1,2].plot(dy2)
ax[1,2].set_title(f'Box blur')
plt.show()

