from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('gestion_clientes/', views.gestion_clientes, name='gestion_clientes'),
    path('gestion_polizas/', views.gestion_polizas, name='gestion_polizas'),
    path('gestion_asegurados/', views.gestion_asegurados, name='gestion_asegurados'),
]
