import json
from matplotlib import pyplot as plt 

filename = 'json/gdp_json.json'

with open(filename) as f:
	date = json.load(f)

# Последний год в наборе данных.
max_year = 0
for dt in date:
	if dt['Year'] > max_year:
		max_year = dt['Year']

countries, values = [], []
for dt in date:
	if dt['Year'] == max_year:
		countries.append(dt['Country Name'])
		values.append(dt['Value'])

fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(countries, values)
plt.title('Gross Domestic Product by ')
plt.xlabel('Country', fontsize=8)
plt.ylabel('Value')
fig.autofmt_xdate()
plt.show()

