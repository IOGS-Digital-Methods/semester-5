"""03_enhance_contrast_brithness.py
Image enhancing with OpenCV (contrast and brithness)
.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>

@see: https://iogs-lense-training.github.io/image-processing/contents/opencv.html#histogram-of-an-image
"""

import cv2
from matplotlib import pyplot as plt
import numpy as np

image_gray = cv2.imread('./_data/robot.jpg', cv2.IMREAD_GRAYSCALE)

alpha = 1.2
beta = 10
image2 = cv2.convertScaleAbs(image_gray, alpha=alpha, beta=beta)

# Display images
fig, ax = plt.subplots(nrows=2, ncols=2)
ax[0,0].imshow(image_gray, cmap='gray')
ax[0,0].set_title('Initial Gray Image')
ax[0,1].imshow(image2, cmap='gray')
ax[0,1].set_title('Image after contrast/brithness modification')

# Process histogram
histogram = cv2.calcHist([image_gray], [0], None, [256], [0, 256])
histogram2 = cv2.calcHist([image2], [0], None, [256], [0, 256])
x = np.arange(256)
# Plot the histogram as bar
ax[1,0].bar(x, histogram[:,0], width=1, color='black')
ax[1,0].set_xlim([0, 256])  # Limits for the x-axis
ax[1,0].set_title('Histogram of initial image')
ax[1,1].bar(x, histogram2[:,0], width=1, color='black')
ax[1,1].set_xlim([0, 256])  # Limits for the x-axis
ax[1,1].set_title('Histogram of modified image')
plt.show()