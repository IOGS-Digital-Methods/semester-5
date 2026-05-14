import matplotlib.pyplot as plt
from scipy import signal
from main_parameters import *

## Example of open-loop system vs feedback
# Main system - only gain - A = K_A
# Measure system - B = 1

# Results
results_ol = {}
results_fb = {}

for km in K_M:
    # Correcteur P seul
    sys_A = create_gain(1)
    sys_P = create_pid(kp=1)
    sys_M = create_gain(km)
    sys_fb_P = create_closed_loop(sys_A, sys_P, sys_M)
    results_ol[km] = ct.step_response(sys_fb_P, time_pts)

### Display results
step_time = [-5, time_pts[0] * 1e6, time_pts[0] * 1e6, time_pts[0] * 1e6, time_pts[-1] * 1e6]
step_value = [0, 0, 0, 1, 1]

# Step response - no correction (Kp = 1)
plt.figure()
plt.plot(step_time, step_value, 'k--', alpha=0.5, linewidth=1.5, label='Step')
for kp, response in results_ol.items():
    plt.plot(time_pts * 1e6, response.outputs, label=f'KM = {kp:.0e}')
plt.xlabel('Time (µs)')
plt.ylabel('Amplitude')
plt.title('Step response - Different gain for M (KA = 1)')
#plt.ylim(-0.1, 1.5)
plt.legend()
plt.grid(True)

plt.show()

### Forced response to a square signal

