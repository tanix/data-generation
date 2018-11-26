from die import Die
import pygal

# Создание кубика D6.
die_1 = Die()
die_2 = Die()

# Моделирование серии бросков с сохранением результатов в списке.
results = []
for roll_num in range(1000):
	result = die_1.roll() + die_2.roll()
	results.append(result)

print(results)

# Анализ результатов.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(1, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)

print(frequencies)

# Визуализация результатов.
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = []
max_numb_slides = die_1.num_sides + die_2.num_sides
for value in range(2, max_numb_slides):
	hist.x_labels.append(value)

hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')