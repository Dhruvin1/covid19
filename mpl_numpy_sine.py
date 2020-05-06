import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2*np.pi+0.1, 0.1);
y = np.sin(x)
plt.plot(x, y)
print(x,y)
plt.show()
