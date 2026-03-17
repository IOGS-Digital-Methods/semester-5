"""07_opening_closing.py
Opening and closing morphological process on images with OpenCV
.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>

@see: https://iogs-lense-training.github.io/image-processing/contents/opencv_open_close.html
"""

import cv2
from matplotlib import pyplot as plt

# Kernel
N = 3
cross_kernel_3 = cv2.getStructuringElement(cv2.MORPH_CROSS, (N, N))
square_kernel_3 = cv2.getStructuringElement(cv2.MORPH_RECT, (N, N))

# Image
image = cv2.imread('./_data/a_letter_noise.jpg')
plt.figure()
plt.imshow(image, cmap='gray')
plt.show()

## OPENING
opening_image_cross_3 = cv2.morphologyEx(image, cv2.MORPH_OPEN, cross_kernel_3)
opening_image_square_3 = cv2.morphologyEx(image, cv2.MORPH_OPEN, square_kernel_3)

# Display images
fig, ax = plt.subplots(nrows=1, ncols=3)
ax[0].imshow(image, cmap='gray')
ax[0].set_title('Initial Gray Image / Opening')
ax[1].imshow(opening_image_cross_3, cmap='gray')
ax[1].set_title('Cross 3x3 Kernel')
ax[2].imshow(opening_image_square_3, cmap='gray')
ax[2].set_title('Square 3x3 Kernel')

## CLOSING
closing_image_cross_3 = cv2.morphologyEx(image, cv2.MORPH_CLOSE, cross_kernel_3)
closing_image_square_3 = cv2.morphologyEx(image, cv2.MORPH_CLOSE, square_kernel_3)

# Display images
fig, ax = plt.subplots(nrows=1, ncols=3)
ax[0].imshow(image, cmap='gray')
ax[0].set_title('Initial Gray Image / Closing')
ax[1].imshow(closing_image_cross_3, cmap='gray')
ax[1].set_title('Cross 3x3 Kernel')
ax[2].imshow(closing_image_square_3, cmap='gray')
ax[2].set_title('Square 3x3 Kernel')

plt.show()
