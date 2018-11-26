from die import Die
import pygal
import matplotlib.pyplot as plt

# Кол-во бросков.
number_of_rolling = 1000

# Кол-во сторон кубика.
number_of_sides_1 = 6
number_of_sides_2 = 10
max_numb_slides = number_of_sides_1 + number_of_sides_2

# Название осей графиков.
x_title = "Result"
y_title = "Frequency of Result"

# Создание кубиков.
die_1 = Die(number_of_sides_1)
die_2 = Die(number_of_sides_2)

def get_chart_title(cube_sides_1, cube_sides_2, num_rolling):
	# str = "Results of rolling a " + str(cube_sides_1) + " and a " + str(cube_sides_2) + " times." + str(num_rolling) + " times."
	return "Results of rolling a " + str(cube_sides_1) + " and a " + str(cube_sides_2) + " times." + str(num_rolling) + " times."

def gen_sides(num):
	list_sides = []
	for value in range(2, num + 1):
		list_sides.append(value)

	return list_sides


# Моделирование серии бросков с сохранением результатов в списке.
results = []
for roll_num in range(number_of_rolling):
	result = die_1.roll() + die_2.roll()
	results.append(result)

# Анализ результатов.
frequencies = []
max_results = die_1.num_sides + die_2.num_sides
for value in range(1, max_results+1):
	frequency = results.count(value)
	frequencies.append(frequency)

print(frequencies)

# Генерирование чат бара в svg
# hist = pygal.Bar()
# hist.title = get_chart_title(number_of_sides_1, number_of_sides_2, number_of_rolling)
# hist.x_labels = gen_sides(max_numb_slides)
# hist.x_title = x_title
# hist.y_title = y_title
# hist.add('', frequencies)
# hist.render_to_file('dice_visual.svg')

# Генерирование pyplot
# print(gen_sides(max_numb_slides))
x_values = gen_sides(max_numb_slides)
y_values = [0, 17, 31, 55, 58, 68, 94, 96, 94, 106, 113, 87, 72, 59, 34, 16]
# print(input_values)
squares = [1, 4, 9, 16, 25]
plt.scatter(x_values, y_values)
plt.show()


