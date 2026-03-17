# Paul Cheneau

import cv2
import numpy as np

MIN_AREA = 200          # taille min bruit objet (pas de bruit)
APPROX_EPSILON = 0.02   # tolérance pour la fonction approxPolyDP

img_gray = cv2.imread('../step_by_step/_data/gray_blocks.png', cv2.IMREAD_GRAYSCALE)

#clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
#img_contrast = clahe.apply(img_gray)

#Petit blur
img_contrast = cv2.GaussianBlur(img_gray, (15,15), 0)
img_contrast = img_gray

thresh_value, img_thresh = cv2.threshold(img_contrast, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
#print(thresh_value)


#Contours
contours, _ = cv2.findContours(img_thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

img_out = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)

for cnt in contours:
    area = cv2.contourArea(cnt)
    if area < MIN_AREA:
        continue

    # on dit que c'est un polygone
    peri = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, APPROX_EPSILON * peri, True)

    # Identifier le polygone
    n_sides = len(approx)
    if n_sides == 3:
        shape_type = "Triangle"
    elif n_sides == 4:
        # Utilisation minAreaRect pour tenir compte de l'orientation
        rect = cv2.minAreaRect(cnt)
        w, h = rect[1]
        ratio = w / float(h) if w > h else h / float(w)
        shape_type = "Carre" if 0.9 < ratio < 1.1 else "Rectangle"
    elif n_sides == 5:
        shape_type = "Pentagone"
    elif n_sides > 5:
        shape_type = "Cercle"
    else:
        shape_type = f"{n_sides}-gon"

    # draw
    cv2.drawContours(img_out, [approx], -1, (255,0,0), 2)

    # txt
    M = cv2.moments(cnt)
    if M["m00"] != 0:
        cX = int(M["m10"]/M["m00"])
        cY = int(M["m01"]/M["m00"])
        cv2.putText(img_out, shape_type, (cX-30, cY),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)




cv2.imshow("Seuil Otsu", img_thresh)
cv2.imshow("Polygones detectes", img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()
