"""08_gradient.py
Gradient process on images with OpenCV
.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>

"""

import cv2
from matplotlib import pyplot as plt

# Kernel
N = 3
cross_kernel_3 = cv2.getStructuringElement(cv2.MORPH_CROSS, (N, N))

# Image
image = cv2.imread('./_data/bricks2.jpg', cv2.IMREAD_GRAYSCALE)
plt.figure()
plt.imshow(image, cmap='gray')
plt.show()

## OPENING / CLOSING
erosion_image_cross_3 = cv2.erode(image, cross_kernel_3)
dilation_image_cross_3 = cv2.dilate(image, cross_kernel_3)
grad_image_cross_3 = cv2.morphologyEx(image, cv2.MORPH_GRADIENT, cross_kernel_3)
grad_sub_image_cross_3 = dilation_image_cross_3-erosion_image_cross_3


# Display images
fig, ax = plt.subplots(nrows=1, ncols=3)
ax[0].imshow(image, cmap='gray')
ax[0].set_title('Initial Gray Image / Closing')
ax[1].imshow(grad_image_cross_3, cmap='gray')
ax[1].set_title('Gradient function CV2')
ax[2].imshow(grad_sub_image_cross_3, cmap='gray')
ax[2].set_title('Substract Open and close operation')

plt.show()

