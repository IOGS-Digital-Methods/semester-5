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
	x_bary = np.floor(np.sum(XX * tab2D) // sum_tab)
	y_bary = np.floor(np.sum(YY * tab2D) // sum_tab)
	return int(x_bary), int(y_bary)


if __name__ == '__main__':
	image_tif = Image.open('Profil1.tif')
	image = image_tif.convert("L")
	image = np.asarray(image)
	plt.figure()
	plt.imshow(image)
	x_b, y_b = barycentre(image)
	plt.axvline(x_b)
	plt.axhline(y_b)

	# slice
	slice_image = image[x_b, :]
	plt.figure()
	plt.plot(slice_image)
	
	# Image PNG Brute
	image_png = Image.open('Profil1_b.png')
	image = image_png.convert("L")
	image = np.asarray(image)
	plt.figure()
	plt.imshow(image)
	x_b, y_b = barycentre(image)
	plt.axvline(x_b)
	plt.axhline(y_b)
	
	# slice
	slice_image = image[x_b, :]
	plt.figure()
	plt.plot(slice_image)
	plt.show()