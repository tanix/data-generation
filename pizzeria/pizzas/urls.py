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
	url(r'^pizzas/(?P<pizza_id>\d+)/$', views.topping, name='topping'),

	# Страница для добавления новой темы.
	url(r'^new_pizza/$', views.new_pizza, name='new_pizza'),

	# Страница для добавления новых игнредиентов.
	url(r'^new_topping/(?P<pizza_id>\d+)/$', views.new_topping, name='new_topping'),

	# Страница для редактирования игнредиентов.
    url(r'^edit_topping/(?P<topping_id>\d+)/$', views.edit_topping, name='edit_topping'),
   
]
