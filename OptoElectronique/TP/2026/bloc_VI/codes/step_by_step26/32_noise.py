'''
Chargement et conversion en niveaux de gris

Filtrage Gaussien pour réduire le bruit granulaire

Détection des bords (Canny)

Morphologie (fermeture) pour renforcer les contours

Extraction des contours

Filtrage des contours par taille / circularité / forme

Bounding boxes pour visualiser les objets détectés

'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

# --- 1) Charger l'image ---
img = cv2.imread("./_data/noise_vi_small.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img.shape)

# --- 2) Filtre gaussien pour réduire le bruit ---
blur = cv2.GaussianBlur(gray, (7, 7), 1.5)
blur_or = cv2.GaussianBlur(gray, (3, 3), 1.5)

# --- 3) Détection de contours (Canny) ---
edges = cv2.Canny(blur, 50, 150)
edges_or = cv2.Canny(blur_or, 50, 150)

# --- 4) Fermeture morphologique pour lier les contours ---
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

# --- 5) Trouver les contours ---
contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

output = img.copy()

# --- 6) Filtrer les contours + dessiner bounding boxes ---
for c in contours:
    area = cv2.contourArea(c)

    # éliminer le bruit ou petites poussières
    if area < 300:
        continue

    x, y, w, h = cv2.boundingRect(c)
    cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)


# Display images
fig, ax = plt.subplots(nrows=2, ncols=3)
ax[0,0].imshow(img, cmap='gray')
ax[0,0].set_title('Initial Gray Image / Filter')
ax[0,1].imshow(blur, cmap='gray')
ax[0,1].set_title('Gaussian Blur')
ax[0,2].imshow(edges, cmap='gray')
ax[0,2].set_title('Contours')

ax[1,0].imshow(output, cmap='gray')
ax[1,1].set_title('Detected Objects')

ax[1,1].imshow(gray - blur, cmap='gray')
ax[1,1].set_title('Gaussian Blur')
ax[1,2].imshow(edges_or, cmap='gray')
ax[1,2].set_title('Contours')

plt.show()
