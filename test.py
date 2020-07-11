import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0, 2, 100)
y = np.sin(np.pi * x)
plt.plot(x, y)
plt.show()