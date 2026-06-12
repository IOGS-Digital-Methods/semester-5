import numpy as np
import cv2
from matplotlib import pyplot as plt

# Open image
image = cv2.imread("./_data/forms_small.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# Slice
line_number = 15

image_slice = image[line_number, :, :]



# Display images
plt.figure()
plt.imshow(image, vmin=0, vmax=255)
plt.figure()
plt.imshow(image_gray, cmap='gray', vmin=0, vmax=255)

plt.figure()
plt.plot(image_slice)



plt.show()