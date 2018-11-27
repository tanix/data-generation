import csv

from matplotlib import pyplot as plt
from datetime import datetime

# Чтение температур из файла.
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	# for index, column_header in enumerate(header_row):
	# 	print(index, column_header)

	hights, dates, lows = [], [], []
	for row in reader:
		high = int(row[1])
		low = int(row[3])
		hights.append(high - 33)
		dates.append(datetime.strptime(row[0], '%Y-%m-%d'))
		lows.append(low - 33)

	# print(hights)

# Нанесение данных на диаграмму.
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, hights, c = 'red')
plt.plot(dates, lows, c = 'blue')

plt.title("Daily high and low temperatures - 2014", fontsize=24) 
plt.xlabel('', fontsize=6)
fig.autofmt_xdate()
plt.ylabel("Temperature (С)", fontsize=16)
# plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
