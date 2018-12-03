import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Создание и сохранение ответа.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

r = requests.get(url)
print('Status code:', r.status_code)

# Сохранение ответа API в переменной.
response_dict = r.json()
print('Количество репозиториев:', response_dict['total_count'])

# Анализ информации о репозиториях.
repo_dicts = response_dict['items']

names, stars = [], []
for item in repo_dicts:
	names.append(str(repo_dicts['name']))
	stars.append(int(repo_dicts['stargazers_count']))

max_stargazers_count = 0
most_popular_item = {}
for item in repo_dicts:
	if item['stargazers_count'] > max_stargazers_count:
		max_stargazers_count = item['stargazers_count']
		most_popular_item = item

print('The max stargazers count ', max_stargazers_count)
print('Full name ', most_popular_item['full_name'])
print('Html url ', most_popular_item['html_url'])
print('Description ', most_popular_item['description'])

my_style = LS('#33366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)














