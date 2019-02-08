from django.shortcuts import render
from .models import Pizza, Topping

from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse
from django.urls import reverse

from .models import Pizza, Topping
from .forms import PizzaForm, ToppingForm

def index(request):
	""" Домашняя страница приложения """
	return render(request, 'pizzas/index.html')

def pizzas(request):
	""" Выводит список """
	pizza = Pizza.objects.order_by('id')
	context = {'pizza': pizza}

	return render(request, 'pizzas/list.html', context)

def topping(request, pizza_id):
	"""Выводит список ингредиентов."""
	pizza = Pizza.objects.get(id=pizza_id)
	toppings = pizza.topping_set.all()
	context = {'pizza': pizza, 'toppings': toppings}

	return render(request, 'pizzas/topping.html', context)

def new_pizza(request):
	"""Добавление новой пиццы."""
	if request.method != 'POST':
		# Данные не отправлялись; создается пустая форма.
		form = PizzaForm()
	else:
		# Отправлены данные POST; обработать данные.
		form = PizzaForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('pizzas:list'))

	context = {'form': form}
	return render(request, 'pizzas/new_pizza.html', context)

def new_topping(request, pizza_id):
	"""Добавление новых ингредиентов"""
	pizza = Pizza.objects.get(id=pizza_id)
	
	if request.method != 'POST':
		# Данные не отправлялись; создается пустая форма.
		form = ToppingForm()
	else:
		# Отправлены данные POST; обработать данные.
		form = ToppingForm(data=request.POST)
		if form.is_valid():
			new_topping = form.save(commit=False)
			new_topping.pizza = pizza
			new_topping.save()
			return HttpResponseRedirect(reverse('pizzas:topping', args=[pizza_id]))

	context = {'pizza': pizza, 'form': form }
	return render(request, 'pizzas/new_topping.html', context)


def edit_topping(request, topping_id):
	"""Редактирование ингредиентов"""
	topping = Topping.objects.get(id=topping_id)
	pizza = topping.pizza

	if request.method != 'POST':
		# Данные не отправлялись; создается пустая форма.
		form = ToppingForm(instance=topping)
	else:
		# Отправка данных POST; обработать данные.
		form = ToppingForm(instance=topping, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('pizzas:topping', args=[topping.id]))

	context = {'pizza': pizza, 'topping': topping, 'form': form }
	return render(request, 'pizzas/edit_topping.html', context)









































































