import matplotlib.pyplot as plt

COUNT = 10

x = [i for i in range(COUNT)]
y = [i*i for i in x]

#plt.style.use('seaborn')
fig, (ax1,ax2) = plt.subplots(1,2)

ax1.scatter(x,y,cmap=plt.cm.Blues,s=10)
ax1.set_title("Suqare of numbers")
ax1.set_xlabel("values")
ax1.set_ylabel("square of values")

ax2.plot(x,y)
ax2.set_title("Suqare of numbers")
ax2.set_xlabel("values")
ax2.set_ylabel("square of values")

plt.savefig('square_plot.png')
plt.show()

