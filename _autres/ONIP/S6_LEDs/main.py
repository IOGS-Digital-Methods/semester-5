"""
LED Illuminance cartography
    Semester 6 project of ONIP (Numerical Tools for Physicians)

Help at : https://www.hindawi.com/journals/mpe/2021/8099757/
"""

import numpy as np
from matplotlib import pyplot as plt


class working_plan:
    def __init__(self, width, length, step):
        """

        :param width:   float, width of the screen (in meters)
        :param length:  float, length of the screen (in meters)
        :param step:    float, step of the screen grid
        """
        self.width = width
        self.length = length
        self.step = step
        self.nb_x_len = int(self.length / self.step + 1)
        self.x_len = np.linspace(0, self.length, self.nb_x_len)
        self.nb_y_width = int(self.width / self.step + 1)
        self.y_width = np.linspace(0, self.width, self.nb_y_width)

    def __str__(self):
        return f'Plan (L = {self.longueur} / l = {self.largeur}'

    def get_mesh(self):
        self.mesh_x, self.mesh_y = np.meshgrid(self.x_len, self.y_width)
        return self.mesh_x, self.mesh_y

    def calculate_source_cart(self, source=None):
        x_mesh, y_mesh = self.get_mesh()
        zs = np.sqrt(x_mesh ** 2 + y_mesh ** 2)
        return x_mesh, y_mesh, zs

    def get_x_y_vector(self):
        return self.x_len, self.y_width

class LED_source:

    def __init__(self, I0, delta, x=0, y=0, z=1, theta=0, zeta=0):
        '''

        :param I0:  float, maximal light intensity
        :param delta:   float, half-angle of emission (in degree)
        :param x:   float, x position of the source
        :param y:   float, y position of the source
        :param z:   float, z position of the source
        :param theta:   float, angle of emission
        :param zeta:   float, angle of emission
        '''
        self.I0 = I0
        self.delta = delta*np.pi / 180

        self.x, self.y, self.z, self.theta, self.zeta = x, y, z, theta, zeta
        # definition of ux, uy, uz = unitary vector of the main source direction
        self.ux = np.cos(self.theta)*np.sin(self.zeta)
        self.uy = np.sin(self.theta)*np.cos(self.zeta)
        self.uz = -(1-(self.ux**2+self.uy**2))**(1/2)

    def __str__(self):
        return f'LED (I0={self.I0} / delta={self.delta})'

    def led_intensity(self, angle):
        """
        indicatrice de rayonnement
        :param angle:   float, angle
        :return:
            value of the light intensity in the specific angle
        """
        return self.I0*np.exp(-(4*np.log(2))*(angle / self.delta)**2)

    def led_illumination(self, distance, angle):
        """

        :param distance:    float, distance between light source and the point of view (in meters)
        :param angle:   float, angle between normal vector of the light source and the point of view (in degrees)
        :return:
            illumination value at a specific distance and angle

        help from : https://fr.wikibooks.org/wiki/Photographie/Photom%C3%A9trie/Calculs_photom%C3%A9triques_usuels
        """
        angle_new = angle * np.pi / 180
        return self.led_intensity(angle) * np.cos(angle_new) / (distance**2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    alpha = np.linspace(0, np.pi, 101)
    led1 = LED_source(1, 30)
    print(led1)
    led_intens = led1.led_intensity(alpha)
    led_illumi = led1.led_illumination(0.5, alpha)
    plt.figure()
    plt.plot(alpha*180/np.pi, led_intens)
    plt.plot(alpha*180/np.pi, led_illumi)
    plt.figure()
    plt.polar(alpha, led_intens)
    plt.show()

    wp = working_plan(2, 1, 0.01)

    grid_x, grid_y = wp.get_mesh()
    print(grid_x.shape)

    # Test graph

    xx, yy, zz = wp.calculate_source_cart(source=led1)
    plt.figure()
    h = plt.contourf(xx, yy, zz)
    plt.colorbar()
    plt.show()
