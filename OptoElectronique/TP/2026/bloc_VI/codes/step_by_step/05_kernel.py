"""05_kernel.py
Kernel creation with OpenCV
.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>

@see: https://iogs-lense-training.github.io/image-processing/contents/opencv_erod_dila.html
"""

import cv2
from matplotlib import pyplot as plt

# Kernel
M, N = 3, 7
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (M,N))

plt.figure()
plt.imshow(kernel, cmap='gray')
plt.show()

M, N = 5, 3
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (M,N))

plt.figure()
plt.imshow(kernel, cmap='gray')
plt.show()
