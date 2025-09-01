from django.urls import path
from home.views import home, crear_cliente, listado_clientes

urlpatterns = [
    path('', home, name='home'),
    path('clientes', listado_clientes, name='listado_clientes'),
    path('clientes/crear/', crear_cliente, name='crear_cliente')
]