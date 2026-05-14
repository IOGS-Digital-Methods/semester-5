import matplotlib.pyplot as plt
from scipy import signal
from main_parameters import *


# Stockage des résultats
results_p_only = {}
results_pi = {}

for kp in K_p:
    # Correcteur P seul
    sys_P = create_pid(kp=kp)
    sys_fb_P = create_closed_loop(sys_A, sys_P, sys_M)
    results_p_only[kp] = ct.step_response(sys_fb_P, time_pts)

    # Correcteur PI
    sys_PI = create_pid(kp=kp, ki=K_i)
    sys_fb_PI = create_closed_loop(sys_A, sys_PI, sys_M)
    results_pi[kp] = ct.step_response(sys_fb_PI, time_pts)

### Display results
step_time = [-5, time_pts[0] * 1e6, time_pts[0] * 1e6, time_pts[0] * 1e6, time_pts[-1] * 1e6]
step_value = [0, 0, 0, 1, 1]

# Step response - P correction
plt.figure()
plt.plot(step_time, step_value, 'k--', alpha=0.5, linewidth=1.5, label='Step')
for kp, response in results_p_only.items():
    plt.plot(time_pts * 1e6, response.outputs, label=f'Kp = {kp}')
plt.xlabel('Time (µs)')
plt.ylabel('Amplitude')
plt.title('Step response - P correction')
plt.ylim(-0.1, 1.5)
plt.legend()
plt.grid(True)

plt.show()

### Forced response to a square signal

