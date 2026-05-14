from control_lib import *
from scipy import signal

### Parameters
FINAL_TIME = 1e-4
SAMPLING_TIME = 1e-8
time_pts = np.arange(0, FINAL_TIME, SAMPLING_TIME)

# Main system
f_AOP = 1e7
f_A = 1e4
K_A = [0.1, 1, 5, 20]
# Initial System
sys_A_lp = create_lowpass(f_A)
sys_A = ct.tf([1], [1])

# Measure system
f_M = 1e3
K_M = [1e-2, 0.1, 1, 5, 20]
sys_M = create_lowpass(f_M)
sys_M = ct.tf([1], [1])


# PID system
K_p = [0.1, 1, 5, 20]
K_i = [1e7, 1e5, 1e3, 1]


### Forced response to a square signal
f_sq = 3e4
u = signal.square(2 * np.pi * f_sq * time_pts)