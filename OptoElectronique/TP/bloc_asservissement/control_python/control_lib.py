import control as ct
import numpy as np

### Systems definition
def create_gain(gain=1):
    """Create a simple gain system."""
    return ct.tf([gain], [1])

def create_lowpass(f_cutoff, gain=1):
    """Create a first order lowpass filter."""
    return ct.tf([gain], [1 / (2 * np.pi * f_cutoff), 1])

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