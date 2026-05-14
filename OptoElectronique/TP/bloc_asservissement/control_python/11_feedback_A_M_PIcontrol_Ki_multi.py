import matplotlib.pyplot as plt
from scipy import signal
from main_parameters import *

## Example of open-loop system vs feedback
# Main system - only gain - A = K_A
# Measure system - B = 1

# Results
results_ol = {}
results_fb = {}
KA = 1
KM = 1
# Correction
TI = 1e-6
KI = 1/TI

sys_A = create_lowpass(f_A, gain=KA)
sys_M = create_gain(gain=KM)
sys_NO = create_pid(kp=1)
results_ol[1] = ct.step_response(ct.series(sys_A, sys_M), time_pts)
sys_fb_NO = create_closed_loop(sys_A, sys_NO, sys_M)
results_fb[0] = ct.step_response(sys_fb_NO, time_pts)
for ki in K_i:
    sys_PI = create_pid(kp=1, ki=ki)
    sys_fb_PI = create_closed_loop(sys_A, sys_PI, sys_M)
    results_fb[ki] = ct.step_response(sys_fb_PI, time_pts)

### Display results
step_time = [-5, time_pts[0] * 1e6, time_pts[0] * 1e6, time_pts[0] * 1e6, time_pts[-1] * 1e6]
step_value = [0, 0, 0, 1, 1]
tau_value = [0.63, 0.63, 0.63, 0.63, 0.63]

### Step response - I controller
plt.figure()
plt.plot(step_time, step_value, 'k--', alpha=0.5, linewidth=1.5, label='Step')
plt.plot(time_pts * 1e6, results_ol[1].outputs, label=f'Open-loop')
plt.plot(time_pts * 1e6, results_fb[0].outputs, label=f'Controlled system - No correction')
for ki in K_i:
    plt.plot(time_pts * 1e6, results_fb[ki].outputs, label=f'Controlled system - PI correction (Ti = {1/ki*1e6:.0e} us)')
plt.xlabel('Time (µs)')
plt.ylabel('Amplitude')
plt.title(f'Step response - A = 1 / M = 1 / Integral TI = {KI/1e6:.0e} us')
#plt.ylim(-0.1, 1.5)
plt.legend()
plt.grid(True)

plt.show()