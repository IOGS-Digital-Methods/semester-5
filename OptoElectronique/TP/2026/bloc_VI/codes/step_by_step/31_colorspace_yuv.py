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
plt.imshow(image_gray, cmap='gray')
plt.show()


# Rec. 709
# 0,2126, 0,7152 et 0,0722
Y_lum = 0.2126 * image_rgb[0, 0, 0] + 0.7152 * image_rgb[0, 0, 1] + 0.0722 * image_rgb[0, 0, 2]
print(f'First Pixel Luminance (Rec.709) : {Y_lum}')


# Change space color
image_yuv = cv2.cvtColor(image_rgb , cv2.COLOR_RGB2YUV)
print(f'First Pixel YUV : {image_yuv[0, 0]}')