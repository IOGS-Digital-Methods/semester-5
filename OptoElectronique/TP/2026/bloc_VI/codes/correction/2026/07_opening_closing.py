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

#plt.show()





## CORRECTION

# CAS RGB
image_rgb = cv2.imread('./_data/formes_bruit.png')
image_rgb = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2RGB)

N = 15
square_kernel_3 = cv2.getStructuringElement(cv2.MORPH_RECT, (N, N))
closing_image_square = cv2.morphologyEx(image_rgb, cv2.MORPH_CLOSE, square_kernel_3)

opening_image_square = cv2.morphologyEx(image_rgb, cv2.MORPH_OPEN, square_kernel_3)

# Display images
fig, ax = plt.subplots(nrows=1, ncols=3)
ax[0].imshow(image_rgb)
ax[0].set_title('Initial RGB Image')
ax[1].imshow(closing_image_square)
ax[1].set_title('Square 15x15 Kernel - Fermeture')
ax[2].imshow(opening_image_square)
ax[2].set_title('Square 15x15 Kernel - Ouverture')

# CAS GRAY
image_gray = cv2.imread('./_data/formes_bruit.png', cv2.IMREAD_GRAYSCALE)

N = 15
square_kernel_3 = cv2.getStructuringElement(cv2.MORPH_RECT, (N, N))
closing_image_square = cv2.morphologyEx(image_gray, cv2.MORPH_CLOSE, square_kernel_3)

opening_image_square = cv2.morphologyEx(image_gray, cv2.MORPH_OPEN, square_kernel_3)

# Display images
fig, ax = plt.subplots(nrows=1, ncols=3)
ax[0].imshow(image_gray, cmap='gray')
ax[0].set_title('Initial RGB Image')
ax[1].imshow(closing_image_square, cmap='gray')
ax[1].set_title('Square 15x15 Kernel - Fermeture')
ax[2].imshow(opening_image_square, cmap='gray')
ax[2].set_title('Square 15x15 Kernel - Ouverture')

plt.show()