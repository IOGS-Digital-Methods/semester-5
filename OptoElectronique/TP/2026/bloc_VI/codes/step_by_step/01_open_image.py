"""01_open_image.py
Image opening with OpenCV
.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>

@see: https://iogs-lense-training.github.io/image-processing/contents/opencv.html#open-an-image
@see: https://iogs-lense-training.github.io/image-processing/contents/opencv.html#display-an-image
"""

import cv2
from matplotlib import pyplot as plt


image_rgb = cv2.imread('./_data/robot.jpg', cv2.IMREAD_UNCHANGED)
image_rgb = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2RGB)

image_gray = cv2.imread('./_data/robot.jpg', cv2.IMREAD_GRAYSCALE)

plt.figure()
plt.imshow(image_rgb)
plt.figure()
plt.imshow(image_gray) #, cmap='gray')
plt.show()

# Information on the images
print(f'Type RGB image: {type(image_rgb)} / Dtype: {image_rgb.dtype}')
print(f'RGB shape: {image_rgb.shape}')
print(f'Gray shape: {image_gray.shape}')

