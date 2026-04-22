import cv2
import numpy as np
import matplotlib.pyplot as plt

# Charger l'image
img = cv2.imread("./_data/hsv_rgb_test_image.png")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# =========================
# 1) SEGMENTATION RGB
# =========================
R, G, B = img_rgb[:,:,0], img_rgb[:,:,1], img_rgb[:,:,2]

mask_rgb = (R > 140) & (G < 100) & (B < 100)
mask_rgb = mask_rgb.astype(np.uint8) # * 255

# =========================
# 2) SEGMENTATION HSV
# =========================
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Rouge = deux plages !
lower_red1 = np.array([0, 70, 50])
upper_red1 = np.array([10, 255, 255])

lower_red2 = np.array([170, 70, 50])
upper_red2 = np.array([179, 255, 255])

mask_hsv1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask_hsv2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask_hsv = cv2.bitwise_or(mask_hsv1, mask_hsv2)

print(f'Type mask = {mask_hsv.dtype} (HSV) / {mask_rgb.dtype} (RGB)')

# =========================
# 3) VISUALISATION
# =========================
fig, ax = plt.subplots(1, 3, figsize=(15,5))

ax[0].imshow(img_rgb)
ax[0].set_title("Image originale")
ax[0].axis("off")

ax[1].imshow(mask_rgb, cmap="gray")
ax[1].set_title("Masque RGB")
ax[1].axis("off")

ax[2].imshow(mask_hsv, cmap="gray")
ax[2].set_title("Masque HSV")
ax[2].axis("off")


area_rgb = np.sum(mask_rgb > 0)
area_hsv = np.sum(mask_hsv > 0)

print("Aire RGB :", area_rgb)
print("Aire HSV :", area_hsv)

plt.show()
