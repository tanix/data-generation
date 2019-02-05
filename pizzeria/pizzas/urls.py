"""Определяет схемы URL для learning_logs. """
from django.conf.urls import url
from . import views

app_name = 'pizzas'

urlpatterns = [
	# Домашняя страница
	url(r'^$', views.index, name='index'),

	# Вывод всех пиц
	url(r'^pizzas/$', views.pizzas, name='list'),

	# Страница с подробной информацией по ингредиенитам
	url(r'^pizzas/(?P<pizza_id>\d+)/$', views.topping, name='topping')
]
