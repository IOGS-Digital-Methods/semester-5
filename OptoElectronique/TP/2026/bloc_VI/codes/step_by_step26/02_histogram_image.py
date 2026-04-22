"""02_histogram_image.py
Image histogram processing with OpenCV
.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>

@see: https://iogs-lense-training.github.io/image-processing/contents/opencv.html#histogram-of-an-image
"""

import cv2
from matplotlib import pyplot as plt
import numpy as np

image_gray = cv2.imread('./_data/robot.jpg', cv2.IMREAD_GRAYSCALE)

histogram = cv2.calcHist([image_gray], [0], None, [256], [0, 256])

print(histogram[100])
print(image_gray.shape)
print(np.sum(histogram))

# Line Version
plt.figure()
plt.title("Grayscale Image Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")
plt.plot(histogram)
plt.xlim([0, 256])  # Limits for the x-axis

# Bar Version
plt.figure()
plt.title("Grayscale Image Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Number of Pixels")
# Create a range of values (0 to 255) for the x-axis
x = np.arange(256)
# Plot the histogram as bars
plt.bar(x, histogram[:,0], width=1, color='black')
plt.xlim([0, 256])  # Limits for the x-axis
plt.show()


