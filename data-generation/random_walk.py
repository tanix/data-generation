import matplotlib.pyplot as plt
from random import choice

class RandomWalk():
	def __init__(self, num_points=5000):
		self.num_points = num_points
		self.x_values = [0]
		self.y_values = [0]

	def fill_walk(self):
		while len(self.x_values) < self.num_points:
			x_direction = choice([1, -1])
			x_distance = choice([0, 1, 2, 3, 4])
			x_step = x_direction * x_distance
			y_direction = choice([1, -1])
			y_distance = choice([0, 1, 2, 3, 4])
			y_step = y_direction * y_distance

			if x_step == 0 and y_step ==0:
				continue

			next_x = self.x_values[-1] + x_step
			next_y = self.y_values[-1] + y_step

			self.x_values.append(next_x)
			self.y_values.append(next_y)



rw = RandomWalk()
rw.fill_walk()
plt.figure(figsize=(10, 6))

# plt.scatter(rw.x_values, rw.y_values, c=rw.x_values, cmap= plt.cm.Blues,edgecolor='none', s=15)
# plt.scatter(0, 0, c='green', edgecolor='none', s=100)
# plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

plt.plot(rw.x_values, rw.y_values)

plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)


plt.show()