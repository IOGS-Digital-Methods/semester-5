"""12_sobel.py
Sobel gradient process with OpenCV
.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>

"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

image_gray = cv2.imread('./_data/gray_blocks.png', cv2.IMREAD_GRAYSCALE)

# Kernel
K_x = np.array([[1, 0], [0, -1]])
K_y = np.array([[0, 1], [-1, 0]])
G_x = cv2.filter2D(image_gray, -1, K_x)
G_y = cv2.filter2D(image_gray, -1, K_y)
Amp = np.sqrt(G_x**2 + G_y**2)

# Display images
fig, ax = plt.subplots(nrows=2, ncols=2)
ax[0,0].imshow(image_gray, cmap='gray')
ax[0,0].set_title('Initial Gray Image')
ax[1,0].imshow(Amp, cmap='gray')
ax[1,0].set_title('Roberts Amplitude')
ax[0,1].imshow(G_x, cmap='gray')
ax[0,1].set_title('Roberts X')
ax[1,1].imshow(G_y, cmap='gray')
ax[1,1].set_title('Roberts Y')
plt.show()