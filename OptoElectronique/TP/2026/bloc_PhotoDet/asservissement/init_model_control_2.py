import control as ct
from matplotlib import pyplot as plt
import numpy as np
import scipy.signal as signal


## Parameters
final_time = 1e-4
sampling_time = 1e-7
time_pts = np.arange(0,final_time, sampling_time)

## Initial System
f_A = 3e7
den_sys_A = [1/(2*np.pi*f_A), 1]
num_sys_A = [1]

sys_A = ct.tf(num_sys_A, den_sys_A)

## Measure
f_M = 1e5
den_sys_M = [1/(2*np.pi*f_M), 1]
num_sys_M = [1]
sys_M = ct.tf(num_sys_M, den_sys_M)

# First test
response_A = ct.step_response(sys_A, time_pts)
response_M = ct.step_response(sys_M, time_pts)

plt.figure()
plt.plot(time_pts, response_A.outputs, label='Initial system')
plt.plot(time_pts, response_M.outputs, label='measure system')
plt.legend()
plt.title('Step response of initial system and measure system')


## Control System
sys_cs = ct.series(sys_A, sys_M)
response_cs = ct.step_response(sys_cs, time_pts)
sys_fb = ct.feedback(sys_A, sys_M)
response_fb = ct.step_response(sys_fb, time_pts)

plt.figure()
plt.plot(time_pts, response_cs.outputs, label='global open-loop system')
plt.plot(time_pts, response_fb.outputs, label='controlled system - no correction')
plt.legend()
plt.title('Step response global system')

# Forced response
f_sq = 3e4
u = signal.square(2 * np.pi * f_sq * time_pts)

t, y_cs = ct.forced_response(sys_cs, time_pts, u)
t, y_fb = ct.forced_response(sys_fb, time_pts, u)

plt.figure()
plt.plot(time_pts, y_cs, label='global open-loop system')
plt.plot(time_pts, y_fb, label='controlled system - no correction')
plt.legend()
plt.title('Forced response global system')

plt.show()
