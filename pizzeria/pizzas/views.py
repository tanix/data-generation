from django.shortcuts import render
from .models import Pizza, Topping

# Create your views here.

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