"""06_erosion_dilation.py
Erosion and dilation on images with OpenCV
.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>

@see: https://iogs-lense-training.github.io/image-processing/contents/opencv_erod_dila.html
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

## EROSION
eroded_image_cross_3 = cv2.erode(image, cross_kernel_3, iterations=1)
eroded_image_square_3 = cv2.erode(image, square_kernel_3, iterations=1)

# Display images
fig, ax = plt.subplots(nrows=1, ncols=3)
ax[0].imshow(image, cmap='gray')
ax[0].set_title('Initial Gray Image / Erosion')
ax[1].imshow(eroded_image_cross_3, cmap='gray')
ax[1].set_title('Cross 3x3 Kernel')
ax[2].imshow(eroded_image_square_3, cmap='gray')
ax[2].set_title('Square 3x3 Kernel')

## DILATION
dilated_image_cross_3 = cv2.dilate(image, cross_kernel_3, iterations=1)
dilated_image_square_3 = cv2.dilate(image, square_kernel_3, iterations=1)
fig, ax = plt.subplots(nrows=1, ncols=3)
ax[0].imshow(image, cmap='gray')
ax[0].set_title('Initial Gray Image / Dilation')
ax[1].imshow(dilated_image_cross_3, cmap='gray')
ax[1].set_title('Cross 3x3 Kernel')
ax[2].imshow(dilated_image_square_3, cmap='gray')
ax[2].set_title('Square 3x3 Kernel')
plt.show()
