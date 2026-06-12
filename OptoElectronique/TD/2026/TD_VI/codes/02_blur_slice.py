import numpy as np
import cv2
from matplotlib import pyplot as plt

# Open image
image = cv2.imread("./_data/forms_small.png")
image = cv2.imread("./_data/noise_image.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# Slice
line_number = 20

image_slice = image_gray[line_number, :]

# Kernel
kernel_size1 = (1, 3)
kernel_size2 = (1, 5)
kernel_size3 = (1, 9)
# Blur
#blurred_image_1 = cv2.GaussianBlur(image_gray, kernel_size, 2)
blurred_image = cv2.blur(image_gray, kernel_size1)
blurred_image1 = cv2.blur(image_slice, kernel_size1)
blurred_image2 = cv2.blur(image_slice, kernel_size2)
blurred_image3 = cv2.blur(image_slice, kernel_size3)


# Display images
plt.figure()
plt.imshow(image_gray, cmap='gray', vmin=0, vmax=255)
plt.figure()
plt.imshow(blurred_image, cmap='gray', vmin=0, vmax=255)

plt.figure()
plt.plot(image_slice, label='initial gray image')
plt.plot(blurred_image1, label='blurred gray image - kernel 3')
plt.plot(blurred_image2, label='blurred gray image - kernel 5')
plt.plot(blurred_image3, label='blurred gray image - kernel 9')
plt.legend()




plt.show()