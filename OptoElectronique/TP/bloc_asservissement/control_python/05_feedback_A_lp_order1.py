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
# No correction (Kp = 1)
sys_A = create_lowpass(f_A, gain=KA)
sys_P = create_pid(kp=1)
sys_M = create_gain(KM)
results_ol[1] = ct.step_response(ct.series(sys_A, sys_M), time_pts)
sys_fb_P = create_closed_loop(sys_A, sys_P, sys_M)
results_fb[1] = ct.step_response(sys_fb_P, time_pts)

### Display results
step_time = [-5, time_pts[0] * 1e6, time_pts[0] * 1e6, time_pts[0] * 1e6, time_pts[-1] * 1e6]
step_value = [0, 0, 0, 1, 1]
tau_value = [0.63, 0.63, 0.63, 0.63, 0.63]

# Step response - no correction (Kp = 1)
plt.figure()
plt.plot(step_time, step_value, 'k--', alpha=0.5, linewidth=1.5, label='Step')
plt.plot(time_pts * 1e6, results_ol[1].outputs, label=f'Open-loop')
plt.plot(time_pts * 1e6, results_fb[1].outputs, label=f'Controlled system')
plt.xlabel('Time (µs)')
plt.ylabel('Amplitude')
plt.title(f'Step response - A = {KA} - f_lp = {f_A/1000} kHz / M = {KM}')
#plt.ylim(-0.1, 1.5)
plt.legend()
plt.grid(True)

plt.figure()
plt.plot(step_time, step_value, 'k--', alpha=0.5, linewidth=1.5, label='Step')
plt.plot(step_time, tau_value, 'r--', alpha=0.2, linewidth=1.5, label='63%')
plt.plot(time_pts * 1e6, results_ol[1].outputs / np.max(results_ol[1].outputs), label=f'Open-loop')
plt.plot(time_pts * 1e6, results_fb[1].outputs / np.max(results_fb[1].outputs), label=f'Controlled system')
plt.xlabel('Time (µs)')
plt.ylabel('Amplitude')
plt.title(f'Step response - A = {KA} - f_lp = {f_A/1000} kHz / M = {KM} -- NORMALIZED')
#plt.ylim(-0.1, 1.5)
plt.legend()
plt.grid(True)

plt.show()

### Forced response to a square signal

