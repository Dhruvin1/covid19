import matplotlib.pyplot as plt
#import numpy as np

numbers = [0,1,2,3,4,5]
squares = [0,1,4,9,16,25]

fig, ax = plt.subplots()

ax.plot(numbers, squares)

#x = np.arange(0, 5, 0.1);
#y = np.sin(x)
#plt.plot(x, y)

plt.show()
