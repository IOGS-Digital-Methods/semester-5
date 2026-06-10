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
kernel_size = (3, 3)
# Blur
#blurred_image_1 = cv2.GaussianBlur(image_gray, kernel_size, 2)
blurred_image = cv2.blur(image_gray, kernel_size)
blurred_image_slice = blurred_image[line_number, :]


# Display images
plt.figure()
plt.imshow(image, vmin=0, vmax=255)
plt.figure()
plt.imshow(image_gray, cmap='gray', vmin=0, vmax=255)

plt.figure()
plt.plot(image_slice, label='initial gray image')
plt.plot(blurred_image_slice, label='blurred gray image')
plt.legend()

plt.figure()
plt.imshow(blurred_image, cmap='gray', vmin=0, vmax=255)





plt.show()
