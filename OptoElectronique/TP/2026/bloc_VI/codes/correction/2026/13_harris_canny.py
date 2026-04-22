"""13_harrys_canny.py
Harrys and Canny process with OpenCV
.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>

"""

import cv2
from matplotlib import pyplot as plt

image_gray = cv2.imread('./_data/gray_blocks.png', cv2.IMREAD_GRAYSCALE)

## HARRIS
image_harris = cv2.cornerHarris(image_gray , 2, 11, 0.1)

# Display images
fig, ax = plt.subplots(nrows=1, ncols=2)
ax[0].imshow(image_gray, cmap='gray')
ax[0].set_title('Initial Gray Image')
ax[1].imshow(image_harris, cmap='gray')
ax[1].set_title('Harris Process')


image_gray = cv2.imread('./_data/bricks2.jpg', cv2.IMREAD_GRAYSCALE)
## CANNY
image_canny = cv2.Canny(image_gray,100,110)

# Display images
fig, ax = plt.subplots(nrows=1, ncols=2)
ax[0].imshow(image_gray, cmap='gray')
ax[0].set_title('Initial Gray Image')
ax[1].imshow(image_canny, cmap='gray')
ax[1].set_title('Canny Process')
plt.show()