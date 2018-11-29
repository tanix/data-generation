import json
from matplotlib import pyplot as plt
from country_codes import get_country_code
from pygal.maps.world import World
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS

# Список заполняется данными.
filename = 'population_data.json'
country = 'United Kingdom'
year = 2016

population, years = [], []
cc_population = {}

with open(filename) as f:
	pop_data = json.load(f)

	for pop_dict in pop_data:	
		# Выборка значений для страны.
		if pop_dict['Country Name'] == country:		
			populat = int(float(pop_dict['Value']))
			year = int(pop_dict['Year'])
			population.append(populat)
			years.append(year)			

		# Выборка численности населения по году.
		if pop_dict['Year'] == year:
			cntr = pop_dict['Country Name']
			populat = int(float(pop_dict['Value']))
			code = get_country_code(cntr)		
			if code:
				cc_population[code] = populat

# Группировка численности населения.
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_population.items():
	if pop < 10000000:
		cc_pops_1[cc] = pop
	elif pop < 1000000000:
		cc_pops_2[cc] = pop
	else:
		cc_pops_3[cc] = pop

# Численность населения страны за год.
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(years, population)
plt.title('Population of years ' + country)
fig.autofmt_xdate()
plt.xlabel('Years')
plt.ylabel('Population')
plt.show()

# Мировая численность населения.
wm_style = RS('#336699')
wm = World(style=wm_style)
wm.title = 'Word Population in 2016, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)
wm.render_to_file('word_population.svg')


