"""11_line_detection.py
Line detection on images with OpenCV
.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>

"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Open an image - Grayscale
image_gray = cv2.imread('./_data/forms_opening_closing.png', cv2.IMREAD_GRAYSCALE)

# Transform image in binary image
(T, image_bw) = cv2.threshold(image_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# Create the kernel for horizontal lines detection
hor_size = 100
hor_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (hor_size, 1))

# Apply erosion and dilation
horizontal1 = cv2.erode(image_bw, hor_kernel)
horizontal2 = cv2.dilate(horizontal1, hor_kernel)

# Display images
fig, ax = plt.subplots(nrows=1, ncols=3)
ax[0].imshow(image_gray, cmap='gray')
ax[0].set_title('Initial Gray Image')
ax[1].imshow(horizontal1, cmap='gray')
ax[1].set_title('Horizontal / Erosion')
ax[2].imshow(horizontal2, cmap='gray')
ax[2].set_title('Horizontal / Dilation')
plt.show()

    