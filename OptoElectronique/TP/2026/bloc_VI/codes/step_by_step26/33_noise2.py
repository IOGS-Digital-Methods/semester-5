'''
Débruitage (Gaussian)

Contours (Canny)

Approximation polygonale (Douglas–Peucker)

Classification par :

nombre de côtés

circularité

ratio largeur/hauteur

compactness
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt
import math

def classify_shape(contour):
    # --- Aire + périmètre ---
    area = cv2.contourArea(contour)
    if area < 300:
        return None
    
    perimeter = cv2.arcLength(contour, True)
    
    # --- Circularité ---
    circularity = 4 * math.pi * (area / (perimeter * perimeter))

    # --- Approximation polygonale ---
    epsilon = 0.02 * perimeter
    approx = cv2.approxPolyDP(contour, epsilon, True)
    vertices = len(approx)

    # --- Bounding box ---
    x, y, w, h = cv2.boundingRect(contour)
    ratio = w / float(h)

    # --- Classification simple ---
    if vertices > 8 and circularity > 0.70:
        return "Cercle / rondelle"

    if vertices == 4:
        if 0.8 < ratio < 1.2:
            return "Carré"
        else:
            return "Rectangle"

    if vertices == 6:
        return "Écrou (hexagone)"

    # Détection vis : forme longiligne avec bords parallèles
    if ratio > 2.2 or ratio < 0.45:
        return "Vis (forme allongée)"

    return "Autre"


# ================================
# Pipeline principal
# ================================
img = cv2.imread("./_data/noise_vi_small.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Débruitage
blur = cv2.GaussianBlur(gray, (7, 7), 1.5)

# Canny
edges = cv2.Canny(blur, 50, 150)

# Fermeture morphologique
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
closed = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel)

# Extraction des contours
contours, _ = cv2.findContours(closed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

output = img.copy()

for contour in contours:
    shape = classify_shape(contour)
    if shape is None:
        continue

    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(output, (x, y), (x+w, y+h), (0,255,0), 2)
    cv2.putText(output, shape, (x, y-10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

# Affichage
plt.figure()
plt.imshow(output, cmap='gray')
plt.show()
