"""09_fft.py
Blur and mean on images with OpenCV
.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>

@see: https://iogs-lense-training.github.io/image-processing/contents/opencv_blur.html
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
from images_manipulation import *

# Image
trame = sine_trame(300, 500, step=20, angle=30)

plt.figure()
plt.imshow(trame, cmap='gray')

# FFT
fft_image = np.fft.fftshift(np.fft.fft2(trame))

plt.figure()
plt.imshow(np.log(np.abs(fft_image)+0.001), cmap='gray')


slice_x = trame[:,150]
slice_y = trame[250,:]

plt.figure()
plt.plot(slice_x)
plt.plot(slice_y)
plt.show()