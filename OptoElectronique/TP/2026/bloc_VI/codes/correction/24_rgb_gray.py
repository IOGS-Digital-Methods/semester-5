"""24_rgb_gray.py
Image opening with OpenCV
.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>

"""

import cv2
import numpy as np
from matplotlib import pyplot as plt


image_rgb = cv2.imread('./_data/couleurs_4.png', cv2.IMREAD_UNCHANGED)
image_rgb = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2RGB)

image_rgb_modif = image_rgb.copy()
image_rgb_modif[:,:,2] = 0

plt.figure()
plt.imshow(image_rgb)
plt.figure()
plt.imshow(image_rgb_modif) #, cmap='gray')
plt.show()

print(f'Size : {image_rgb.shape}')

rect_1_B_m = np.mean(image_rgb[0:199,0:199,2])
rect_1_B_std = np.std(image_rgb[0:199,0:199,2])
print(f'rect_1_B : {rect_1_B_m} / {rect_1_B_std}')


image_rgb = cv2.imread('./_data/cubes.jpg', cv2.IMREAD_UNCHANGED)
image_rgb = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2RGB)

cube_jaune = image_rgb[150:200,150:200,:]



plt.figure()
plt.imshow(image_rgb)
plt.figure()
plt.imshow(cube_jaune)
plt.show()


jaune_R_m = np.mean(cube_jaune[:,:,0])
jaune_R_std = np.std(cube_jaune[:,:,0])
print(f'Jaune : {jaune_R_m} / {jaune_R_std}')


print('Gray Scale / Mean')
# Gray Scale
image_gray = cv2.imread('./_data/couleurs_4.png', cv2.IMREAD_GRAYSCALE)

# Mean
image_gray_mean = image_rgb[:,:,0] // 3 + image_rgb[:,:,1] // 3 + image_rgb[:,:,2] // 3

plt.figure()
plt.imshow(image_gray, cmap='gray')
plt.figure()
plt.imshow(image_gray_mean, cmap='gray')
plt.show()


# Rec. 709
# 0,2126, 0,7152 et 0,0722
Y_lum = 0.2126 * image_rgb[0, 0, 0] + 0.7152 * image_rgb[0, 0, 1] + 0.0722 * image_rgb[0, 0, 2]

