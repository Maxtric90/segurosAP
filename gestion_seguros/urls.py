from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gestion_clientes/', views.gestion_clientes, name='gestion_clientes'),
    path('gestion_polizas/', views.gestion_polizas, name='gestion_polizas'),
    path('gestion_asegurados/', views.gestion_asegurados, name='gestion_asegurados'),
    path('cartera_cliente/<int:cliente_id>', views.cartera_cliente, name='cartera_cliente'),
    path('detalle_cliente/<int:cliente_id>', views.detalle_cliente, name='detalle_cliente'),
]
