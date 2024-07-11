from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pedidos/', views.pedidos, name='pedidos'),
    path('registro/', views.registro, name='registro'),
    path('menu_bodega/', views.menu_bodega, name='menu_bodega'),
]
