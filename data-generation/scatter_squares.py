import matplotlib.pyplot as plt

x_values_2 = list(range(1, 5000))
y_values_2 = [x**2 for x in x_values_2]

x_values_3 = list(range(1, 5000))
y_values_3 = [x**3 for x in x_values_3]

# plt.scatter(x_values_2, y_values_2, c='red', edgecolor='none', s=20)
# plt.scatter(x_values_3, y_values_3, c='b' ,cmap=plt.cm.Blues, edgecolor='none', s=20)

ax = plt.subplot();
ax.plot(x_values_2, y_values_2)
ax.plot(x_values_3, y_values_3)

# plt.title("Square Numbers", fontsize=24)
# ax.xlabel("Value", fontsize=14)
# ax.ylabel("Square of Value", fontsize=14)

# ax.tick_params(axis='both', which='major', labelsize=14)


plt.show()