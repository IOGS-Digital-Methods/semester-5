"""03_enhance_contrast_brithness.py
Image enhancing with OpenCV (contrast and brithness)
.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>

@see: https://iogs-lense-training.github.io/image-processing/contents/opencv.html#histogram-of-an-image
"""

import cv2
from matplotlib import pyplot as plt
import numpy as np

image_gray = cv2.imread('./_data/robot.jpg', cv2.IMREAD_GRAYSCALE)

alpha = 0.4
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



## CORRECTION
fig, ax = plt.subplots(nrows=2, ncols=2)
ax[0,0].imshow(image_gray, cmap='gray', vmin=0, vmax=255)
ax[0,0].set_title('Initial Gray Image')
ax[0,1].imshow(image2, cmap='gray', vmin=0, vmax=255)
ax[0,1].set_title('Image after contrast/brithness modification')
# Plot the histogram as bar
ax[1,0].bar(x, histogram[:,0], width=1, color='black')
ax[1,0].set_xlim([0, 256])  # Limits for the x-axis
ax[1,0].set_title('Histogram of initial image')
ax[1,1].bar(x, histogram2[:,0], width=1, color='black')
ax[1,1].set_xlim([0, 256])  # Limits for the x-axis
ax[1,1].set_title('Histogram of modified image')
plt.show()

# CAS RGB

image_rgb = cv2.imread('./_data/robot.jpg')
image_rgb = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2RGB)

alpha = 0.4
beta = 10
image2 = cv2.convertScaleAbs(image_rgb, alpha=alpha, beta=beta)
# Display images
fig, ax = plt.subplots(nrows=2, ncols=2)
ax[0,0].imshow(image_rgb)
ax[0,0].set_title('Initial RGB')
ax[0,1].imshow(image2)
ax[0,1].set_title('Image after contrast/brithness modification')

histogram = cv2.calcHist([image_rgb], [0], None, [256], [0, 256])
histogram2 = cv2.calcHist([image2], [0], None, [256], [0, 256])
# Plot the histogram as bar / Red
ax[1,0].bar(x, histogram[:,0], width=1, color='black')
ax[1,0].set_xlim([0, 256])  # Limits for the x-axis
ax[1,0].set_title('Histogram of initial image')
ax[1,1].bar(x, histogram2[:,0], width=1, color='black')
ax[1,1].set_xlim([0, 256])  # Limits for the x-axis
ax[1,1].set_title('Histogram of modified image')
plt.show()

plt.show()
