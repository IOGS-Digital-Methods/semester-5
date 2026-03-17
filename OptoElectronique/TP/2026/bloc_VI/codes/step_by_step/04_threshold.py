"""04_threshold.py
Threshold with OpenCV
.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>

@see: https://iogs-lense-training.github.io/image-processing/contents/opencv.html#binarize-an-image
"""

import cv2
from matplotlib import pyplot as plt

image_gray = cv2.imread('./_data/bricks2.jpg', cv2.IMREAD_GRAYSCALE)
max_value = 255
threshold = 100

retval, binary_image = cv2.threshold(image_gray, threshold, max_value, cv2.THRESH_BINARY)

retval_otsu, binary_image_otsu = cv2.threshold(image_gray, threshold, max_value, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

binary_image_gauss = cv2.adaptiveThreshold(image_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

print(f'Retval: {retval_otsu}')

# Display images
fig, ax = plt.subplots(nrows=1, ncols=2)
ax[0].imshow(image_gray, cmap='gray')
ax[0].set_title('Initial Gray Image')
ax[1].imshow(binary_image, cmap='gray')
ax[1].set_title('Binary Image')

fig, ax = plt.subplots(nrows=1, ncols=2)
ax[0].imshow(binary_image_otsu, cmap='gray')
ax[0].set_title('Ostu Binary Image')
ax[1].imshow(binary_image_gauss, cmap='gray')
ax[1].set_title('Gauss Binary Image')

plt.show()
