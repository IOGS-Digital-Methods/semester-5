import cv2
import numpy as np
from matplotlib import pyplot as plt

# Identification des contours
def detect_shape(cnt):
    area = cv2.contourArea(cnt)
    if area < MIN_AREA:
        return None, None

    peri = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, APPROX_FACTOR * peri, True)
    n = len(approx)

    if n == 3:
        shape = "Triangle"
    elif n == 4:
        rect = cv2.minAreaRect(cnt)
        w, h = rect[1]
        if h == 0 or w == 0:
            shape = "Inconnu"
        else:
            ratio = max(w, h) / min(w, h)
            shape = "Carre" if 0.90 < ratio < 1.10 else "Rectangle"
    elif n == 5:
        shape = "Pentagone"
    else:
        shape = f"{n}-gon"

    return shape, approx, peri

# Parameters
MIN_AREA = 1
APPROX_FACTOR = 0.02
GAUSS_SIZE = (7, 7)         # Taille du flou gaussien
GAUSS_SIGMA = 1.9

img_gray = cv2.imread('./_data/formes_blanc_30ms.png', cv2.IMREAD_GRAYSCALE)

# Prétraitement : flou + Otsu
img_blur = cv2.GaussianBlur(img_gray, GAUSS_SIZE, GAUSS_SIGMA)
#img_blur = img_gray
_, img_thresh = cv2.threshold(
    img_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

# Image de sortie (couleur)
img_out = cv2.cvtColor(img_blur, cv2.COLOR_GRAY2BGR)


# Détection des cercles
circles = cv2.HoughCircles(
    img_blur,
    cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=20,
    param1=50,
    param2=30,
    minRadius=50,
    maxRadius=100
)

if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        cv2.circle(img_out, (x, y), r, (0, 255, 0), 3)
        cv2.putText(img_out, "Cercle", (x - 20, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


# =========================
#   AFFICHAGE
# =========================
plt.figure()
plt.imshow(img_gray, cmap='gray')
plt.title("Image Initiale")

plt.figure()
plt.imshow(img_blur, cmap='gray')
plt.title("Seuil Opening")

plt.figure()
plt.imshow(img_out)
plt.title("Formes détectées (polygones + cercles)")

plt.show()
