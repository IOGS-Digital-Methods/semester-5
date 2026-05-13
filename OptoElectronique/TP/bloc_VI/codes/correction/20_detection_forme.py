import cv2
import numpy as np
from matplotlib import pyplot as plt

# Parameters
MIN_AREA = 1000             # Minimal area of an object
APPROX_FACTOR = 0.02        # Tolérance pour approxPolyDP
GAUSS_SIZE = (7, 7)         # Taille du flou gaussien
GAUSS_SIGMA = 1.9


img_gray = cv2.imread('./_data/forms_vi.png', cv2.IMREAD_GRAYSCALE)
#img_gray = cv2.imread('./_data/noise_vi_small.png', cv2.IMREAD_GRAYSCALE)
img_gray = cv2.imread('./_data/formes_blanc_30ms.png', cv2.IMREAD_GRAYSCALE)


# Prétraitement : flou + Otsu
img_blur = cv2.GaussianBlur(img_gray, GAUSS_SIZE, GAUSS_SIGMA)
img_blur = img_gray
_, img_thresh = cv2.threshold(
    img_blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

edged = cv2.Canny(img_thresh, 30, 200)

# Image de sortie (couleur)
img_out = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)

# =========================
#   DÉTECTION DES CONTOURS
# =========================
contours, _ = cv2.findContours(img_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Tri : plus gros → plus petit (évite certaines erreurs)
contours = sorted(contours, key=cv2.contourArea, reverse=True)

# =========================
# FONCTION IDENTIFICATION
# =========================
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

    return shape, approx


# =========================
#  TRAITEMENT DES POLYGONES
# =========================
for cnt in contours:
    shape, approx = detect_shape(cnt)
    if shape is None:
        continue

    cv2.drawContours(img_out, [approx], -1, (255, 0, 0), 2)

    # Centre du contour
    M = cv2.moments(cnt)
    if M["m00"] != 0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        cv2.putText(img_out, shape, (cX - 30, cY),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

# =========================
#   DÉTECTION DES CERCLES
# =========================
circles = cv2.HoughCircles(
    img_blur,
    cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=30,
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
plt.imshow(img_thresh, cmap='gray')
plt.title("Seuil Otsu")

plt.figure()
plt.imshow(edged, cmap='gray')
plt.title("Canny Edges")

plt.figure()
plt.imshow(img_out)
plt.title("Formes détectées (polygones + cercles)")

plt.show()
