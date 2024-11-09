import numpy as np
import pandas as pd

# Define the range of input parameters
r_range = np.linspace(1, 10, 100)
theta_range = np.linspace(0, np.pi, 50)
phi_range = np.linspace(0, 2*np.pi, 50)
chi_range = np.linspace(0, 2*np.pi, 50)

# Calculate the metric tensor values
ds2 = []
for r in r_range:
    for theta in theta_range:
        for phi in phi_range:
            for chi in chi_range:
                A = 1 / (1 - 1 / (2.998e8**2 * 6.67e-11 * r**2))
                ds2.append(A * 2.998e8**2 * r**2 - r**2 * (theta**2 + np.sin(theta)**2 * phi**2 + np.sin(theta)**2 * np.sin(phi)**2 * chi**2))

# Create the CSV data
data = {
    'r': np.repeat(r_range, len(theta_range) * len(phi_range) * len(chi_range)),
    'theta': np.tile(np.repeat(theta_range, len(phi_range) * len(chi_range)), len(r_range)),
    'phi': np.tile(phi_range * len(chi_range), len(r_range) * len(theta_range)),
    'chi': np.tile(chi_range, len(r_range) * len(theta_range) * len(phi_range)),
    'ds2': ds2
}

df = pd.DataFrame(data)
df.to_csv('metric_tensor_data.csv', index=False)
