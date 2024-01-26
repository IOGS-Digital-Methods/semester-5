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
    
def find_max(tab2D):
    return np.where(tab2D == tab2D.max())


if __name__ == '__main__':
	# Airy
    image_png = Image.open('airy_2mm.bmp')
    image = image_png.convert("L")
    image = np.asarray(image)
    plt.figure()
    plt.imshow(np.log(image+0.1))
    
    # Find max and crop
    i_max_x, i_max_y = find_max(image)
    print(i_max_x.shape)
    print(i_max_x)
    
    """
    pas = 200
    image_crop = image[i_max_x-pas:i_max_x+pas, i_max_y-pas:i_max_y+pas]
    
    plt.figure()
    plt.imshow(np.log(image_crop+0.1))
    
    x_b, y_b = barycentre(image_crop)

    plt.figure()
    plt.imshow(np.log(image_crop+0.1))
    plt.axvline(x_b)
    plt.axhline(y_b)
	
	# slice
    slice_image = image_crop[x_b, :]
    plt.figure()
    plt.plot(np.log(slice_image))
    
    plt.show()
    """