import numpy as np

# Create a sample 3D NumPy array
data = np.random.rand(8, 8, 8)

# Save the 3D data as a binary file
np.save('data.npy', data)

