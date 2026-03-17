# Joséphine Bechu

import numpy as np
import matplotlib.pyplot as plt


lam = np.array([i for i in range(360,760,10)])
bleu = np.array([9, 11, 14, 18, 23, 28, 31, 33.5, 39, 46, 49, 48.5, 45, 40, 34, 28, 23.5, 18, 14.5, 11.5, 9.5, 8.5, 8, 8, 7.5, 7.5, 8, 9, 10, 11.5, 12, 12, 11, 10.75, 10.5,10.5, 11,12,13,15])
jaune = np.array([12.5, 11.5, 11, 10, 9, 8.5, 8, 8, 7.75, 8, 8, 8.5, 9, 13, 27, 49, 67, 78, 83, 86, 87, 87.5, 87.5, 87, 86, 85.5, 85, 84.5, 84.75, 85, 86, 86, 87, 87, 85, 83, 85, 83, 85, 88])
rouge = np.array([15, 14, 12.5, 10.75, 9.5, 9.25, 9, 9, 8.5, 8.5, 8, 7, 6.5, 6.25, 6, 6, 6, 6, 6, 6.25, 7, 10, 16, 27, 42, 47.5, 55, 57, 61, 63.5, 65.5, 67, 67.5, 68.5, 69.5, 70, 70, 70.5, 71, 71.25])
vert = np.array([12.5, 12.5, 12, 12.25, 11.5, 11, 10.75, 10.75, 10.75, 11, 11.5, 12, 13, 18.5, 34, 53, 61.5, 61.5, 58, 52.5, 46, 39.75, 33, 26.25, 21, 18, 16.75, 16, 15.5, 15.5, 15.75, 16.25, 18, 20, 22, 24, 24, 23.25, 23.5, 27])


plt.close()
plt.figure()
plt.plot(lam, bleu, color='blue',label='Cube Bleu', linestyle='--', marker='o')
plt.plot(lam, jaune, color='gold',label='Cube Jaune', linestyle='--', marker='o')
plt.plot(lam, rouge, color='red',label='Cube Rouge', linestyle='--', marker='o')
plt.plot(lam, vert, color='forestgreen',label='Cube Vert', linestyle='--', marker='o')
plt.xticks([i for i in range(350,760,50)])
plt.yticks([10,20,30,40,50,60,70,80,90,100])
plt.xlabel("Longueur d'onde en nm")
plt.ylabel("Refléctance en %")
plt.title("Réflectance des cubes en fonction de la longueur d'onde d'éclairage")
plt.axis()
plt.grid()
plt.legend()
plt.show()