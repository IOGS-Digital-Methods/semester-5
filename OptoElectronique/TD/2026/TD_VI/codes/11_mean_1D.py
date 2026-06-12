import numpy as np
from matplotlib import pyplot as plt

# Create signal
signal_step = np.array(
[5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,
5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5])


# N-sample moving average
def moving_average_N(signal, n = 3):
    x = np.asarray(signal)
    kernel = np.ones(n) / n
    return np.convolve(x, kernel, mode='valid')

def moving_average_weight_N(signal, n = 3, coeffs = [1, 3, 1]):
    x = np.asarray(signal)
    weights = np.asarray(coeffs, dtype=float)
    weights /= weights.sum()
    return np.convolve(x, weights[::-1], mode='valid')

# Process

# Display images
# No weights
plt.figure()
plt.plot(signal_step, label="initial signal")
for k in [3, 5, 10]:    
    averaged_signal = moving_average_N(signal_step, k)
    plt.plot(averaged_signal, label=f"average (N = {k})")

plt.legend()

# With weights
plt.figure()
plt.plot(signal_step, label="initial signal")
k = 3
averaged_signal = moving_average_N(signal_step, k)
plt.plot(averaged_signal, label=f"average (N = {k})")
k = 3
w = [1, 5, 1]
averaged_signal = moving_average_weight_N(signal_step, k, w)
plt.plot(averaged_signal, label=f"average (N = {k} / W = {w})")
k = 5
w = [1, 5, 10, 5, 1]
averaged_signal = moving_average_weight_N(signal_step, k, w)
plt.plot(averaged_signal, label=f"average (N = {k} / W = {w})")

plt.legend()

plt.show()