import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression


def plot_linear_regression_with_noise(x, y, noise_level):
    # Add noise to the y data
    noise = np.random.normal(0, noise_level, y.shape)
    y += noise

    # Reshape x for sklearn
    x_reshaped = x.reshape(-1, 1)

    # Create linear regression model
    model = LinearRegression()
    model.fit(x_reshaped, y)

    # Predict y values
    y = model.predict(x_reshaped)

    # Get the coefficients of the linear regression line
    slope = model.coef_[0]
    intercept = model.intercept_

    plt.figure()

    # Plot raw data with noise
    plt.scatter(x, y, color='blue', label='Noisy data (noise level = {})'.format(noise_level))

    # Plot regression line
    plt.plot(x, y, color='red', linewidth=2, label='Linear regression')

    # Add the equation of the linear regression line to the plot
    equation_text = f'y = {slope:.2f}x + {intercept:.2f}'
    plt.text(0.05, 0.95, equation_text, transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')

    # Add labels and legend
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Linear Regression with Noise Level = {}'.format(noise_level))
    plt.legend()


# Generate sample data
np.random.seed(0)  # For reproducibility
x = np.linspace(0, 10, 20)  # 20 points from 0 to 10
y = 2.5 * x - 4.2  #

# Noise levels to test
noise_levels = [0.5, 1, 2, 3, 5, 7, 10]

# Plot for each noise level
for noise_level in noise_levels:
    plot_linear_regression_with_noise(x, y, noise_level)

plt.show()
