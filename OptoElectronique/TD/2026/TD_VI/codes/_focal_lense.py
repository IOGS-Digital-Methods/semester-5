from matplotlib import pyplot as plt
import numpy as np

def d_objet(d_image, focal):
    return 1/(1/d_image - 1/focal)

d_o_list = []

d_image = 0.01
focals = [0.0065 * (n+1) for n in range(100)]

for f in focals:
    d_o_list.append(d_objet(d_image, f))
    

plt.figure()
plt.plot(focals, d_o_list)
plt.show()
