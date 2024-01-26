# Test Barycentre Python / 

import numpy as np
from PIL import Image 
from matplotlib import pyplot as plt


def barycentre(tab2D):
	width = tab2D.shape[0]
	length = tab2D.shape[1]
	Y = np.linspace(0,width-1,width)
	X = np.linspace(0,length-1,length)
	XX,YY= np.meshgrid(X,Y)
	sum_tab = np.sum(tab2D)
	x_bary = np.sum(XX * tab2D) // sum_tab
	y_bary = np.sum(YY * tab2D) // sum_tab
	return x_bary, y_bary


if __name__ == '__main__':
	image = Image.open('Profil1.tif')
	plt.figure()
	plt.imshow(image)
	plt.show()
