import matplotlib.pyplot as plt
import numpy as np

# Constants (adjust as needed)
G = 6.67430e-11  # Gravitational constant
M = 2e30  # Mass of the object (e.g., a black hole)
c = 299792458  # Speed of light

# Define the radial range
r = np.linspace(2 * G * M / c**2, 10 * G * M / c**2, 100)

# Calculate A(r)
A = 1 / (1 - 2 * G * M / (r * c**2))

# Plot A(r)
plt.plot(r, A)
plt.xlabel('r')
plt.ylabel('A(r)')
plt.title('Radial Component of the Schwarzschild Metric')
plt.grid(True)
plt.show()
