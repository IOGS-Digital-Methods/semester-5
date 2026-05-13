import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import control as ct


### Parameters
FINAL_TIME = 1e-4
SAMPLING_TIME = 1e-8
time_pts = np.arange(0, FINAL_TIME, SAMPLING_TIME)

### System
f_cutoff = 1e5
sys_test = ct.tf([1 / (2 * np.pi * f_cutoff), 1], [1 / (2 * np.pi * f_cutoff), 2])

results = ct.step_response(sys_test, time_pts)

plt.figure()
plt.plot(time_pts, results.outputs, label='Step')
plt.show()