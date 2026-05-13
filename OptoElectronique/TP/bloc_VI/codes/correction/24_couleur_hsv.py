import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rgb_v = cv2.imread('./_data/formes_bruit.png')
zone_vert_rgb = img_rgb_v[250:350, 700:800, :]
img_hsv = cv2.cvtColor(img_rgb_v, cv2.COLOR_BGR2HSV)
zone_vert_hsv = img_hsv[250:350, 700:800, :]

# zone_vert_rgb = cv2.GaussianBlur(zone_vert_rgb, (15, 15), 4)

img_rgb_b = cv2.imread('./_data/forms_vi.png')
zone_bleu_rgb = img_rgb_b[430:510, 700:780, :]
img_hsv = cv2.cvtColor(img_rgb_b, cv2.COLOR_BGR2HSV)
zone_bleu_hsv = img_hsv[430:510, 700:780, :]


histogram_v_rgb = cv2.calcHist([zone_vert_rgb], [2], None, [256], [0, 256])
histogram_v_hsv = cv2.calcHist([zone_vert_hsv], [0], None, [256], [0, 256])

histogram_b_rgb = cv2.calcHist([zone_bleu_rgb], [2], None, [256], [0, 256])
histogram_b_hsv = cv2.calcHist([zone_bleu_hsv], [0], None, [256], [0, 256])

# =========================
#   AFFICHAGE
# =========================
fig, ax = plt.subplots(nrows=2, ncols=3)
ax[0,0].imshow(img_rgb_b)
ax[0,0].set_title('Initial RGB Image / Blue')
ax[0,1].imshow(zone_bleu_rgb)
ax[0,1].set_title('Blue zone')
ax[0,2].plot(histogram_b_rgb, label='RGB')
ax[0,2].plot(histogram_b_hsv, label='HSV')
ax[0,2].set_title('Histogramme / Blue zone')
ax[1,0].imshow(img_rgb_v)
ax[1,0].set_title('Initial RGB Image / Green')
ax[1,1].imshow(zone_vert_rgb)
ax[1,1].set_title('Green zone')
ax[1,2].plot(histogram_v_rgb, label='RGB')
ax[1,2].plot(histogram_v_hsv, label='HSV')
ax[1,2].legend()
ax[1,2].set_title('Histogramme / Green zone')
plt.show()
