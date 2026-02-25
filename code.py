import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# 1. Generate some noise
# -------------------------------
np.random.seed(42)    
n = 50 
data = np.random.normal(0, 1, n)  # mean 0, std 1

# -------------------------------
# 2. Plot the noise
# -------------------------------
plt.plot(data, marker='o', linestyle='-')
plt.title("White Noise")
plt.grid(True)

# -------------------------------
# 3. Save the plot to a file
# -------------------------------
plt.savefig("plot.png", dpi=300) # high dpi, which means dots per inch
plt.show()