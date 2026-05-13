# Paul Cheneau

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

lam = np.array([i for i in range(360,760,10)])
bleu = np.array([9, 11, 14, 18, 23, 28, 31, 33.5, 39, 46, 49, 48.5, 45, 40, 34, 28, 23.5, 18, 14.5, 11.5, 9.5, 8.5, 8, 8, 7.5, 7.5, 8, 9, 10, 11.5, 12, 12, 11, 10.75, 10.5,10.5, 11,12,13,15])
jaune = np.array([12.5, 11.5, 11, 10, 9, 8.5, 8, 8, 7.75, 8, 8, 8.5, 9, 13, 27, 49, 67, 78, 83, 86, 87, 87.5, 87.5, 87, 86, 85.5, 85, 84.5, 84.75, 85, 86, 86, 87, 87, 85, 83, 85, 83, 85, 88])
rouge = np.array([15, 14, 12.5, 10.75, 9.5, 9.25, 9, 9, 8.5, 8.5, 8, 7, 6.5, 6.25, 6, 6, 6, 6, 6, 6.25, 7, 10, 16, 27, 42, 47.5, 55, 57, 61, 63.5, 65.5, 67, 67.5, 68.5, 69.5, 70, 70, 70.5, 71, 71.25])
vert = np.array([12.5, 12.5, 12, 12.25, 11.5, 11, 10.75, 10.75, 10.75, 11, 11.5, 12, 13, 18.5, 34, 53, 61.5, 61.5, 58, 52.5, 46, 39.75, 33, 26.25, 21, 18, 16.75, 16, 15.5, 15.5, 15.75, 16.25, 18, 20, 22, 24, 24, 23.25, 23.5, 27])

lam2 = np.array([i for i in range(360,751,1)])


fb = interp1d(lam, bleu, kind='cubic')  # 'linear', 'quadratic', 'cubic'
fr = interp1d(lam, rouge, kind='cubic')  # 'linear', 'quadratic', 'cubic'
fg = interp1d(lam, vert, kind='cubic')  # 'linear', 'quadratic', 'cubic'
fj = interp1d(lam, jaune, kind='cubic')  # 'linear', 'quadratic', 'cubic'



# Constantes du systeme
Top = 1
Spx = (10*10**(-6))**2
N = 4
h = 6.62*10**(-34)
c = 3*10**8
QE_max = 1
g = 2.4
sigma = 15* 10**(0)
#lambdas = np.arange(420, 661, 1)  # 420 à 660 nm, pas de 1 nm
lambdas = lam2
#source_peaks = [ (460, 0.7, 40),  (520, 0.5, 40),  (630, 1.0, 40) ] # Chaque pic des sourvces : (lambda_c, amplitude, largeur_sigma)



#A faire varier
texp_us = input('Temps integration ? (us) ')
texp = int(texp_us)*10**(-6)


# Listes pour les calculs
signal = [] #Signal electric
E = [] #Eclairement de la source
QE = [] #FOnction de lamba pour la transfo photon electron
R = [] #Reflectivité de l'objet


R = fj(lambdas)/100
for i in lambdas:
    """Choisir parmis les 3 sources RVB"""
    #E.append( 1*np.exp(-((i - 630*10**(0))**2) / (2 * sigma**2))) #source rouge
    E.append( 1*np.exp(-((i - 600*10**(0))**2) / (2 * sigma**2))) #source 700
    #E.append(0.7*np.exp(-((i - 460*10**(0))**2) / (2 * sigma**2))) #source bleue
    #E.append(0.5*np.exp(-((i - 515*10**(0))**2) / (2 * (sigma)**2))) #source verte
    # Blanc
    #E.append(1 * np.exp(-((i - 630 * 10 ** (0)) ** 2) / (2 * sigma ** 2))  + (0.7*np.exp(-((i - 460*10**(0))**2) / (2 * sigma**2))) + (0.5*np.exp(-((i - 515*10**(0))**2) / (2 * (sigma)**2))))


    # QE (courbe a trouver ?)
    QE.append(1*np.exp(-((i - 550*10**(0))**2) / (2 * (400*10**(0))**2))) # A determier plus precisement
    #QE.append(0.5) #Approx simpliste


    # Choix de la reflectivité (objet)

    # R Jaune
    #R.append((40 / (np.pi / 2) * np.arctan(i - 525) + 50) / 100)

    # R Rouge
    #R.append((40 / (np.pi / 2) * np.arctan(i - 600) + 50) / 100)

    '''
    # R bleu
    if i <= 460:
        R.append((0.5*i-180)/100)
    if (460 < i) and (i<=550):
        R.append((-0.33*i+203)/100)
    if 550 < i:
        R.append(10/100)
    '''
for i in range(len(E)):
    E[i]=E[i]*0.01

for i in range(len(lambdas)):
    l = lambdas[i]
    signal.append(Top * Spx / (h*c*4*N**2) * (l*10**(-9)) * E[i] * QE[i] * R[i] * texp)


pixel_signal = sum(signal)

ADU = pixel_signal / g
if ADU > 2**(12)-1:
    ADU = 2 ** (12) - 1

print(f"---------- ADU = {ADU:.2f}, Ecart Type = {np.sqrt(pixel_signal / g):.2f} ----------")
print("----------- Bloc Jaune sous lumière Rouge ----------------------")
print(f"----------- temps d'exposition = {texp*10**6:.2f} microsecondes -----------")



# Graphiques

fig, axes = plt.subplots(1, 4, figsize=(18, 5))  # 1 ligne, 4 colonnes

# --- Premier graphique : E(λ) ---
axes[0].plot(lambdas, E, color='Red')
axes[0].set_title('Spectre de la source E(λ)')
axes[0].set_xlabel('Longueur d\'onde (nm)')
axes[0].set_ylabel('Irradiance (W/m²/nm)')

# --- Deuxième graphique : Ry(λ) ---
axes[1].plot(lambdas, R, color='Red')
axes[1].set_title('Réflectance R(λ)')
axes[1].set_xlabel('Longueur d\'onde (nm)')
axes[1].set_ylabel('Réflectance (0-1)')

# --- Troisième graphique : QE(λ) ---
axes[2].plot(lambdas, QE, color='Red')
axes[2].set_title('Quantum Efficiency QE(λ)')
axes[2].set_xlabel('Longueur d\'onde (nm)')
axes[2].set_ylabel('QE (0-1)')

# ---Quatrième graphique : signal(λ) ---
axes[3].plot(lambdas, signal, color='Black')
axes[3].set_title('Signal(λ)')
axes[3].set_xlabel('Longueur d\'onde (nm)')
axes[3].set_ylabel('ADU')

plt.tight_layout()
plt.show()