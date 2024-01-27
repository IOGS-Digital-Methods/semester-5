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
    max_ind = np.argmax(tab2D)
    width = tab2D.shape[0]
    length = tab2D.shape[1]
    ind_x = int(max_ind / length)
    ind_y = int(max_ind % width)
    return ind_x, ind_y


if __name__ == '__main__':
    """
    # Test image
    image = np.zeros((100, 200))
    image[52, 69] = 100
    
    x, y = find_max(image)
    print(f'x = {x} / y = {y}')
    """

    
	# Airy
    image_png = Image.open('airy_2mm.bmp')
    image = image_png.convert("L")
    image = np.asarray(image)
    plt.figure()
    plt.imshow(np.log(image+0.1))
    
    # Find max 
    i_max_x, i_max_y = find_max(image)
    plt.axvline(i_max_y)
    plt.axhline(i_max_x)
    x_b0, y_b0 = barycentre(image)
    plt.axvline(x_b0, color='g')
    plt.axhline(y_b0, color='g')
    
    # Crop 
    pas = 300
    if(i_max_x < pas):
        pas = i_max_x
    if(i_max_y < pas):
        pas = i_max_y
    print(f'pas = {pas}')
    image_crop = image[i_max_x-pas:i_max_x+pas, i_max_y-pas:i_max_y+pas]
    print(f'Shape = {image_crop.shape}')
    
    # Find barycenter
    x_b, y_b = barycentre(image_crop)
    print(f'x_b={x_b} / y_b={y_b}')

    plt.figure()
    plt.imshow(np.log(image_crop+0.1))
    plt.axvline(x_b)
    plt.axhline(y_b)
	
	# slice
    pas_slice_a = 5
    pas_slice_b = 50
    plt.axhline(y_b-pas_slice_a, color='g')
    plt.axhline(y_b+pas_slice_a, color='g')
    plt.axhline(y_b-pas_slice_b, color='r')
    plt.axhline(y_b+pas_slice_b, color='r')
    
    # slices
    slice_image_one = image_crop[x_b, :]
    slice_image_a = image_crop[x_b-pas_slice_a:x_b+pas_slice_a, :]
    slice_image_a_sum = np.sum(slice_image_a, axis=0)
    slice_image_b = image_crop[x_b-pas_slice_b:x_b+pas_slice_b, :]
    slice_image_b_sum = np.sum(slice_image_b, axis=0)
    
    plt.figure()
    plt.plot(slice_image_one, label='1 line')
    plt.plot(slice_image_a_sum /(2*pas_slice_a+1), label=f'{pas_slice_a*2+1} lines')
    plt.plot(slice_image_b_sum /(2*pas_slice_b+1), label=f'{pas_slice_b*2+1} lines')
    plt.legend()
    
    plt.show()