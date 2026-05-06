import control as ct
from matplotlib import pyplot as plt
import numpy as np
import scipy.signal as signal


## Parameters
final_time = 1e-4
sampling_time = 1e-7
time_pts = np.arange(0,final_time, sampling_time)

## Initial System
den_sys_A = [1]
num_sys_A = [1]

sys_A = ct.tf(num_sys_A, den_sys_A)

## Measure
f0 = 1e5
den_sys_M = [1/(2*np.pi*f0), 1]
num_sys_M = [1]
sys_M = ct.tf(num_sys_M, den_sys_M)

## PID correction
K_p = 1
K_i = 1e6
K_d = 1e-1
tau_d = 1e-2

sys_P = ct.tf([K_p], [1])
sys_I = ct.tf([K_i], [1, 0])
sys_D = ct.tf([K_d, 0], [tau_d, 1])
sys_PID = ct.parallel(sys_P, sys_I, sys_D)
sys_PID = ct.parallel(sys_P, sys_I)

response_PID = ct.step_response(sys_PID, time_pts)

plt.figure()
plt.plot(time_pts, response_PID.outputs, label='PID step response')
plt.legend()
plt.title('PID controller step response')


## Control System
sys_cs = ct.series(sys_A, sys_PID, sys_M)
response_cs = ct.step_response(sys_cs, time_pts)
sys_fb = ct.feedback(ct.series(sys_A, sys_PID), sys_M)
response_fb = ct.step_response(sys_fb, time_pts)


plt.figure()
#plt.plot(time_pts, response_cs.outputs, label='global open-loop system')
plt.plot(time_pts, response_fb.outputs, label='controlled system - correction')
plt.legend()
plt.grid()
plt.title('Step response global system')

# Forced response
f_sq = 3e4
u = signal.square(2 * np.pi * f_sq * time_pts)

t, y_cs = ct.forced_response(sys_cs, time_pts, u)
t, y_fb = ct.forced_response(sys_fb, time_pts, u)

plt.figure()
plt.plot(time_pts, y_cs, label='global open-loop system')
plt.plot(time_pts, y_fb, label='controlled system - correction')
plt.legend()
plt.grid()
plt.title('Forced response global system')

plt.show()
