from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')

x = [1,9,4,7]
y = [5,1,8,2]

x2 = [3,1,9,4]
y2 = [2,4,6,5]

plt.plot(x, y, linewidth=4, label="2016")
plt.plot(x2, y2, linewidth=7, label="2017")

plt.title("Demo chart")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.legend()

plt.show()
