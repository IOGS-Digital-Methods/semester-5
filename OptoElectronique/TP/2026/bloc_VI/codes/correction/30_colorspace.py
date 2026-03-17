"""30_colorspace.py
Image opening with OpenCV
.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>

"""

import cv2
import numpy as np
from matplotlib import pyplot as plt


image_rgb = cv2.imread('./_data/couleurs_4.png', cv2.IMREAD_UNCHANGED)
image_rgb = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2RGB)

image_gray = cv2.imread('./_data/couleurs_4.png', cv2.IMREAD_GRAYSCALE)

image_mean = image_rgb.astype(np.float64).mean(axis=2).astype(np.uint8)

print(f'M={image_mean.dtype} / G={image_gray.dtype} / R={image_rgb.dtype} / ShM={image_mean.shape} / MAX={np.max(image_rgb)}')

plt.figure()
plt.imshow(image_rgb)
plt.figure()
plt.imshow(image_mean, cmap='gray')
plt.figure()
plt.imshow(image_gray, cmap='gray')
plt.show()


