import matplotlib.pyplot as plt

COUNT = 10

x = [i for i in range(COUNT)]
y = [i*i for i in x]

#plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.scatter(x,y,s=100)
ax.set_title("Suqare of numbers")
ax.set_xlabel("values")
ax.set_ylabel("square of values")

plt.show()
