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
f_A = 1e6
KM = 0.1
f_M = 1e4
# Correction

sys_A = create_lowpass(f_A, gain=KA)
sys_M = create_lowpass(f_M, gain=KM)
for kp in K_p:
    sys_P = create_pid(kp=kp)
    sys_fb_P = create_closed_loop(sys_A, sys_P, sys_M)
    results_fb[kp] = ct.step_response(sys_fb_P, time_pts)

### Display results
step_time = [-5, time_pts[0] * 1e6, time_pts[0] * 1e6, time_pts[0] * 1e6, time_pts[-1] * 1e6]
step_value = [0, 0, 0, 1, 1]
tau_value = [0.63, 0.63, 0.63, 0.63, 0.63]

# Step response - no correction (Kp = 1)
plt.figure()
plt.plot(step_time, step_value, 'k--', alpha=0.5, linewidth=1.5, label='Step')
for kp in K_p:
    plt.plot(time_pts * 1e6, results_fb[kp].outputs, label=f'Kp = {kp}')
plt.xlabel('Time (µs)')
plt.ylabel('Amplitude')
plt.title(f'Step response - A = {KA} - f_lp = {f_A/1000} kHz / M = {KM} - f_lp = {f_M/1000} kHz ')
#plt.ylim(-0.1, 1.5)
plt.legend()
plt.grid(True)

plt.show()

### Forced response to a square signal

### Bode
omega = np.logspace(3, 9, 101)
plt.figure()
for kp in K_p:
    sys_P = create_pid(kp=kp)
    sys_fb_P = create_closed_loop(sys_A, sys_P, sys_M)
    mag, phase, omega = ct.frequency_response(sys_fb_P, omega)
    plt.semilogx(omega, 20*np.log10(mag), label=f'Kp = {kp}')
plt.xlabel('Pulsation (rd/s)')
plt.ylabel('Gain (dB)')
plt.title(f'Bode Diagram - A = {KA} - f_lp = {f_A/1000} kHz / M = {KM} - f_lp = {f_M/1000} kHz ')
#plt.ylim(-0.1, 1.5)
plt.legend()
plt.grid(True)

plt.show()