import numpy as np
import matplotlib.pyplot as plt

# Générer des valeurs x de 0 à 2*pi
x = np.linspace(0, 2 * np.pi, 100)

# Calculer les valeurs de sinus et de cosinus pour chaque x

plt.figure(figsize = (4.7,3))
# Tracer le sinus en bleu et le cosinus en rouge
plt.plot(x*180/np.pi, np.cos(x), label='Cosinus', color='firebrick', lw = 2)
plt.plot(x*180/np.pi, np.sin(x), label='Sinus', color='teal',lw = 2, ls = "--")

# Ajouter des labels, une légende et un titre
plt.xlabel('Angle (degrés)')
plt.ylabel('Valeur')
plt.legend()
plt.title('Tracé des fonctions sinus et cosinus')

# Afficher la grille
plt.grid(True, alpha = 0.6)
plt.tight_layout()
plt.savefig("nice_fig.png")
# Afficher le graphique
plt.show()
