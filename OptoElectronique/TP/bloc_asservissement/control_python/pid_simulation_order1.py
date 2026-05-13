import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import control as ct

### Parameters
FINAL_TIME = 1e-4
SAMPLING_TIME = 1e-8
time_pts = np.arange(0, FINAL_TIME, SAMPLING_TIME)


### Systems definition
def create_lowpass(f_cutoff, gain=1):
    """Create a first order lowpass filter."""
    return ct.tf([gain], [1 / (2 * np.pi * f_cutoff), 1])

### Main system
# Initial System
f_AOP = 1e4
sys_A = ct.tf([1], [1])
sys_A = create_lowpass(f_AOP)

# Measure system
f0 = 1e5
sys_M = create_lowpass(f0)
sys_M = ct.tf([1], [1])

### Controller definition
def create_pid(kp=0, ki=0, kd=0, tau_d=1e-3):
    """Create PID controller with kp, ki, kd, tau_d parameters."""
    sys_p = ct.tf([kp], [1]) if kp != 0 else ct.tf([0], [1])
    sys_i = ct.tf([ki], [1, 0]) if ki != 0 else ct.tf([0], [1])
    sys_d = ct.tf([kd, 0], [tau_d, 1]) if kd != 0 else ct.tf([0], [1])
    return ct.parallel(sys_p, sys_i, sys_d)

def create_closed_loop(sys_plant, sys_controller, sys_sensor):
    """Create controlled system."""
    return ct.feedback(ct.series(sys_plant, sys_controller), sys_sensor)


### Process systems
K_p_values = [0.1, 1, 5, 20]
K_i = 1e6

# Results
results_p_only = {}
results_pi = {}
results_pi_ki = {}

for kp in K_p_values:
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

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Step response - P correction
ax1 = axes[0]
ax1.plot(step_time, step_value, 'k--', alpha=0.5, linewidth=1.5, label='Step')
for kp, response in results_p_only.items():
    ax1.plot(time_pts * 1e6, response.outputs, label=f'Kp = {kp}')
ax1.set_xlabel('Time (µs)')
ax1.set_ylabel('Amplitude')
ax1.set_title('Step response - P correction')
ax1.set_ylim(-0.1, 2)
ax1.legend()
ax1.grid(True)

# Step response - PI correction
ax2 = axes[1]
ax2.plot(step_time, step_value, 'k--', alpha=0.5, linewidth=1.5, label='Step')
for kp, response in results_pi.items():
    ax2.plot(time_pts * 1e6, response.outputs, label=f'Kp = {kp}, Ki = {K_i:.0e}')
ax2.set_xlabel('Time (µs)')
ax2.set_ylabel('Amplitude')
ax2.set_title('Step response - PI correction')
ax2.set_ylim(-0.1, 2)
ax2.legend()
ax2.grid(True)

plt.tight_layout()

### Forced response to a square signal
f_sq = 3e4
u = signal.square(2 * np.pi * f_sq * time_pts)

fig2, axes2 = plt.subplots(1, 2, figsize=(14, 5))

# Forced response - P correction
ax3 = axes2[0]
ax3.plot(time_pts * 1e6, u, 'k--', alpha=0.5, label='Step point')
for kp in K_p_values:
    sys_P = create_pid(kp=kp)
    sys_fb_P = create_closed_loop(sys_A, sys_P, sys_M)
    _, y = ct.forced_response(sys_fb_P, time_pts, u)
    ax3.plot(time_pts * 1e6, y, label=f'Kp = {kp}')
ax3.set_xlabel('Time (µs)')
ax3.set_ylabel('Amplitude')
ax3.set_title('Forced response to a square - P Correction')
ax3.legend()
ax3.grid(True)

# Réponse forcée - Correcteur PI
ax4 = axes2[1]
ax4.plot(time_pts * 1e6, u, 'k--', alpha=0.5, label='Step point')
for kp in K_p_values:
    sys_PI = create_pid(kp=kp, ki=K_i)
    sys_fb_PI = create_closed_loop(sys_A, sys_PI, sys_M)
    _, y = ct.forced_response(sys_fb_PI, time_pts, u)
    ax4.plot(time_pts * 1e6, y, label=f'Kp = {kp}')
ax4.set_xlabel('Time (µs)')
ax4.set_ylabel('Amplitude')
ax4.set_title('Forced response to a square - PI Correction')
ax4.legend()
ax4.grid(True)


plt.tight_layout()
plt.show()


### Integral
K_i_values = [1e5, 1e6, 1e7]
kp = 1

for ki in K_i_values:
    # Correcteur PI
    sys_PI = create_pid(kp=kp, ki=ki)
    sys_fb_PI = create_closed_loop(sys_A, sys_PI, sys_M)
    results_pi_ki[ki] = ct.step_response(sys_fb_PI, time_pts)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Step response - P correction
ax1 = axes[0]
ax1.plot(step_time, step_value, 'k--', alpha=0.5, linewidth=1.5, label='Step')
for ki, response in results_pi_ki.items():
    ax1.plot(time_pts * 1e6, response.outputs, label=f'Ki = {ki:.0e}')
ax1.plot(time_pts * 1e6, results_p_only[kp].outputs, linestyle= 'dotted', linewidth=2, label='P only')
ax1.set_xlabel('Time (µs)')
ax1.set_ylabel('Amplitude')
ax1.set_title(f'Step response - PI correction (Kp = {kp})')
ax1.set_ylim(-0.1, 2)
ax1.legend()
ax1.grid(True)

# Step response - PI correction
ax2 = axes[1]
ax2.plot(step_time, step_value, 'k--', alpha=0.5, linewidth=1.5, label='Step')
for kp, response in results_pi.items():
    ax2.plot(time_pts * 1e6, response.outputs, label=f'Kp = {kp}, Ki = {K_i:.0e}')
ax2.set_xlabel('Time (µs)')
ax2.set_ylabel('Amplitude')
ax2.set_title('Step response - PI correction')
ax2.set_ylim(-0.1, 2)
ax2.legend()
ax2.grid(True)

plt.tight_layout()

plt.show()