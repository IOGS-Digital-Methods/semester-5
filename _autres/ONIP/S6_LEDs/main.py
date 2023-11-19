import numpy as np
from matplotlib import pyplot as plt

def led_intensity(alpha, I0, directivity):
    return I0*np.exp(-(4*np.log(2))*(alpha / directivity)**2)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    alpha = np.linspace(0, np.pi, 101)
    led_intens = led_intensity(alpha, 1, 90*np.pi/180)
    plt.figure()
    plt.plot(alpha*180/np.pi, led_intens)
    plt.figure()
    plt.polar(alpha, led_intens)
    plt.show()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
