import matplotlib.pyplot as plt
import matplotlib
import random
import numpy as np
from labellines import labelLines

def open_data(file):
	"""
	open file and gives all data points
	"""
	data_points = np.array([[0,0]])
	with open(file) as f:
		line = f.readline()
		data_points.concatenate((line))
	return data_points

plt.figure(figsize=(10,10))
ax = plt.axes(projection="3d")
file=""
end = 30
x = np.array([random.randint(-100,100) for _ in range(end)])
y = np.array([random.randint(-100,100) for _ in range(end)])
z = np.array([random.randint(-100,100) for _ in range(end)])
data_points = [[x[i], y[i], z[i]] for i in range(len(x))]
labels = []
for point in data_points:
	q = np.arange(-100, 100)
	ax.scatter(q, 0, 0, c="black")
	ax.scatter(0, q, 0, c="black")
	ax.scatter(0, 0, q, c="black")
	ax.scatter([0, point[0]], [0, point[1]], [0, point[2]], marker="v", c="red")
	label = f"{point[0]}i + {point[1]}j + {point[2]}k"
	labels.append(label)
	ax.plot([0, point[0]], [0, point[1]], [0, point[2]], label=label)
	ax.text(point[0], point[1], point[2], label, fontsize=7)
	i = data_points.index(point)
	if i == len(data_points)-1:
		pass
	else:
		ax.plot([data_points[i][0], data_points[i+1][0]], [data_points[i][1], data_points[i+1][1]], [data_points[i][2], data_points[i+1][2]])
plt.title("Vector Visualizer")
plt.show()
