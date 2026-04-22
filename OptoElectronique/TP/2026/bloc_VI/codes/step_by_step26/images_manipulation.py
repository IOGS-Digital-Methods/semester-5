# -*- coding: utf-8 -*-
"""*images_manipulation.py* file.

*images_manipulation* file contains extra functions for image manipulation.

This file is attached to a 1st year of engineer training labwork in digital interface development.

.. note:: LEnsE - Institut d'Optique - version 0.1

.. moduleauthor:: Julien VILLEMEJANE <julien.villemejane@institutoptique.fr>
.. creation:: 22/nov/2024
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt


def sine_trame(height, width, step, angle = 0):
    """
    Create a 2D image with a sine waveform.
    
    :param height:  Height of the image.In pixel.
    :param width:   Width of the image. In pixel.
    :param step:    Spatial period of the sine. In pixel.
    :param angle:   Angle of the 2D sine shape. In degree.
    """
    x = np.arange(0,height)
    y = np.arange(0,width)
    XX, YY = np.meshgrid(x, y)
    alpha_rad = np.radians(angle)
    return 0.5*(1 + np.cos(2*np.pi*XX/step*np.cos(alpha_rad) + 2*np.pi*YY/step*np.sin(alpha_rad) ))


def generate_gaussian_noise_image(rows, cols, mean=0, std_dev=1):
    """
    Create a 2D array with a gaussian noise.
    
    :param rows: Number of rows.
    :param cols: Number of columns.
    :param mean: Mean of the gaussian distribution.
    :param std_dev: Stander deviation of the gaussian distribution.
    :return: 2D array.
    """
    gaussian_noise = np.random.normal(mean, std_dev, (rows, cols))    
    return gaussian_noise


def generate_uniform_noise_image(rows, cols, min_val=0, max_val=1):
    """
    Create a 2D array with a uniform noise.
    
    :param rows: Number of rows.
    :param cols: Number of columns.
    :param min_val: Minimum value of the uniform distribution.
    :param max_val: Maximum value of the uniform distribution.
    :return: 2D array.
    """
    uniform_noise = np.random.uniform(min_val, max_val, (rows, cols))    
    return uniform_noise


def generate_gaussian_noise_image_percent(rows, cols, percent_pixels=10, mean=0, std_dev=1):
    """
    Create a 2D array with a gaussian noise - on a part of the image.
    
    :param rows: Number of rows.
    :param cols: Number of columns.
    :param mean: Mean of the gaussian distribution.
    :param std_dev: Standard deviation of the gaussian distribution.
    :percent_pixels: Percent of pixels where to add noise.
    :return: 2D array.
    """
    image = np.zeros((rows, cols))
    
    total_pixels = rows * cols
    num_pixels = (percent_pixels * total_pixels) // 100
    indices = np.random.choice(total_pixels, num_pixels, replace=False)
    
    row_indices = indices // cols
    col_indices = indices % cols
   
    image[row_indices, col_indices] = np.random.normal(mean, std_dev, num_pixels)

    return image


def zoom_array(im_array: np.ndarray, zoom_factor: int = 1):
    """Zoom inside an array in 2D.
    :param im_array: Array to change.
    :param zoom_factor: Zoom factor.
    :return: Modified array.
    """
    return np.repeat(np.repeat(im_array, zoom_factor, axis=0), zoom_factor, axis=1)


def process_hist_from_array(array: np.ndarray, bins: list) -> (np.ndarray, np.ndarray):
    """
    Calculate a histogram from an array and bins definition.
    :param array: Array containing data.
    :param bins: Bins to calculate the histogram.
    :return: Tuple of np.ndarray: bins and hist data.
    """
    plot_hist, plot_bins_data = np.histogram(array, bins=bins)
    return plot_bins_data, plot_hist


def display_hist(data: np.ndarray, data_hist: np.ndarray, bins: np.ndarray,
              title: str = 'Image Histogram'):
    """
    Display a histogram from data.
    :param data: Data to process.
    :param data_hist: Histogram data from np.histogram function.
    :param bins: Bins of the histogram.
    :param title: Title of the figure. Default: Image Histogram.
    :param file_name: Name of the file to store the PNG image. Default: histogram.png.
    :param informations: Informations to display in the graph.
    """
    n = len(bins)
    mean_data = np.mean(data)
    if mean_data > bins[n//2]:
        x_text_pos = 0.30  # text on the left
    else:
        x_text_pos = 0.95  # text on the right
    plt.figure(figsize=(6, 5), dpi=150)
    plt.bar(bins[:-1], data_hist, width=np.diff(bins),
            edgecolor='black', alpha=0.75, color='blue')
    plt.title(title)
    text_str = f'Mean = {mean_data:.2f}\nStdDev = {np.std(data):.2f}'
    plt.text(x_text_pos, 0.95, text_str, fontsize=10, verticalalignment='top',
             horizontalalignment='right',
             transform=plt.gca().transAxes, bbox=dict(facecolor='white', alpha=0.5))
    plt.show()


def compare_blur_fft(image_path: str, kernel_size: (int, int) = (5,5)):
    """
    Display a 2x3 figure to compare on original image and its blurred version.
    FFT are also displayed.
    :param image_path:      Path to the image to process.
    :param kernel_size:     Size of the kernel of the gaussian blur.
    """
    # Open an image - Grayscale
    image_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    blurred_image_gauss = cv2.GaussianBlur(image_gray, kernel_size, 0)

    ### TF
    tf_orig = np.fft.fft2(image_gray)
    tf_blur = np.fft.fft2(blurred_image_gauss)
    tf_diff_log = np.log(0.1+np.abs(np.fft.fftshift(tf_orig)))-np.log(0.1+np.abs(np.fft.fftshift(tf_blur)))

    # Display all
    fig, ax = plt.subplots(nrows=2, ncols=3)
    # Plot data in each subplot
    ax[0,0].imshow(image_gray, cmap='gray')
    ax[0,0].set_title('Original Image')
    ax[0,1].imshow(blurred_image_gauss, cmap='gray')
    ax[0,1].set_title(f'Blurred Image (Size = {kernel_size})')
    ax[0,2].imshow(image_gray-blurred_image_gauss, cmap='gray')
    ax[0,2].set_title('Difference')

    ax[1,0].imshow(np.log(0.1+np.abs(np.fft.fftshift(tf_orig))), cmap='gray')
    ax[1,0].set_title('Original Image / FFT')
    ax[1,1].imshow(np.log(0.1+np.abs(np.fft.fftshift(tf_blur))), cmap='gray')
    ax[1,1].set_title('Blurred Image / FFT')
    ax[1,2].imshow(tf_diff_log, cmap='gray')
    ax[1,2].set_title('Difference / FFT')
    plt.show()


def circular_mask(radius, image, inverted: bool=False):
    """
    Return an image with a circular mask.
    :param radius: Radius of the circular mask.
    :param image: Image to process.
    :param inverted: True to invert the mask.
    :return:
    """
    h, w = image.shape
    center_y, center_x = h // 2, w // 2
    Y, X = np.ogrid[:h, :w]
    # Distance from center to pixel
    dist_from_center = np.sqrt((X - center_x) ** 2 + (Y - center_y) ** 2)
    # Create a circular mask (1 inside the circle, 0 outside)
    if inverted:
        mask = dist_from_center > radius
    else:
        mask = dist_from_center <= radius
    return image * mask
	
	
def elliptic_mask(image, cx=0, cy=0, a=0.5, b=0.5):
    """
	Return elliptic mask from an image size.
    :param image: initial image to mask
    :param cx: X-axis center, from -1 to 1
    :param cy: Y-axis center, from -1 to 1
    :param a: X-axis dimension, from -1 to 1
    :param b: Y-axis dimension, from -1 to 1
    """
    height, width = image.shape
    x = np.linspace(-1, 1, width)
    y = np.linspace(-1, 1, height)
    X, Y = np.meshgrid(x, y)
    return ((X - cx) ** 2) / a ** 2 + ((Y - cy) ** 2) / b ** 2 <= 1
