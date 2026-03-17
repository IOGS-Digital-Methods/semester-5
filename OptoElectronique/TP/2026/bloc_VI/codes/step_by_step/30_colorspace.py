"""30_colorspace.py
Image opening with OpenCV
.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>

"""

import cv2
from matplotlib import pyplot as plt


image_rgb = cv2.imread('./_data/couleurs_4.png', cv2.IMREAD_UNCHANGED)
image_rgb = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2RGB)

image_gray = cv2.imread('./_data/couleurs_4.png', cv2.IMREAD_GRAYSCALE)

plt.figure()
plt.imshow(image_rgb)
plt.figure()
plt.imshow(image_gray)
plt.figure()
plt.imshow(image_gray, cmap='gray')
plt.show()
