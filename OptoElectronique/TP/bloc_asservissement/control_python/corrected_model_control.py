import control as ct
from matplotlib import pyplot as plt
import numpy as np
import scipy.signal as signal


## Parameters
final_time = 1e-4
sampling_time = 1e-8
time_pts = np.arange(0,final_time, sampling_time)

## Initial System
f_AOP = 1e7
den_sys_A = [1/(2*np.pi*f_AOP), 1]
den_sys_A = [1]
num_sys_A = [1]

sys_A = ct.tf(num_sys_A, den_sys_A)

response_cs_A = ct.step_response(sys_A, time_pts)

## Measure
f0 = 1e5
den_sys_M = [1/(2*np.pi*f0), 1]
den_sys_M = [1]
num_sys_M = [1]
sys_M = ct.tf(num_sys_M, den_sys_M)

## PID correction
K_p = 5
K_i = 5e6
K_d = 0
tau_d = 1e-3

sys_P = ct.tf([K_p], [1])
sys_I = ct.tf([K_i], [1, 0])
sys_D = ct.tf([K_d, 0], [tau_d, 1])
sys_PID = ct.parallel(sys_P, sys_I, sys_D)
sys_P = ct.parallel(sys_P)
sys_PI = ct.parallel(sys_P, sys_I)


## Control System
sys_cs_P = ct.series(sys_A, sys_P, sys_M)
sys_cs_PI = ct.series(sys_A, sys_PI, sys_M)
sys_cs_PID = ct.series(sys_A, sys_PID, sys_M)
response_cs_P = ct.step_response(sys_cs_P, time_pts)
response_cs_PI = ct.step_response(sys_cs_PI, time_pts)
response_cs_PID = ct.step_response(sys_cs_PID, time_pts)
sys_fb_P = ct.feedback(ct.series(sys_A, sys_P), sys_M)
sys_fb_PI = ct.feedback(ct.series(sys_A, sys_PI), sys_M)
sys_fb_PID = ct.feedback(ct.series(sys_A, sys_PID), sys_M)
response_fb_P = ct.step_response(sys_fb_P, time_pts)
response_fb_PI = ct.step_response(sys_fb_PI, time_pts)
response_fb_PID = ct.step_response(sys_fb_PID, time_pts)

plt.figure()
plt.plot(time_pts, response_cs_P.outputs, label='global open-loop system')
plt.plot(time_pts, response_fb_P.outputs, label='controlled system - correction - P')
plt.plot(time_pts, response_fb_PI.outputs, label='controlled system - correction - PI')
plt.legend()
plt.grid()
plt.title('Step response global system')

## Step response for different P values
K_P = [1, 5, 10]




# Forced response
f_sq = 3e4
u = signal.square(2 * np.pi * f_sq * time_pts)

t, y_cs_P = ct.forced_response(sys_cs_P, time_pts, u)
t, y_fb_P = ct.forced_response(sys_fb_P, time_pts, u)
t, y_fb_PI = ct.forced_response(sys_fb_PI, time_pts, u)
t, y_fb_PID = ct.forced_response(sys_fb_PID, time_pts, u)

plt.figure()
plt.plot(time_pts, u, label='input step_point')
plt.plot(time_pts, y_cs_P, label='global open-loop system')
plt.plot(time_pts, y_fb_P, label='controlled system - correction - P')
plt.plot(time_pts, y_fb_PI, label='controlled system - correction - PI')
#plt.plot(time_pts, y_fb_PID, label='controlled system - correction - PID')
plt.legend()
plt.grid()
plt.title('Forced response global system')

plt.show()
