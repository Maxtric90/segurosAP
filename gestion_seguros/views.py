from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context={}
    return render(request, 'gestion_seguros/index.html', context)

def gestion_clientes(request):
    clientes=[
        {'nombre': 'La Caja S.A.',
         'CUIT': '23-31232132-2',
         'polizas_activas': 3},
        {'nombre': 'LTA Brokers.',
         'CUIT': '23-55555555-2',
         'polizas_activas': 0}
    ]

    context={
        'clientes': clientes
    }
    return render(request, 'gestion_seguros/gestion_clientes.html', context)

def gestion_polizas(request):
    context={}
    return render(request, 'gestion_seguros/gestion_polizas.html', context)

def gestion_asegurados(request):
    context={}
    return render(request, 'gestion_seguros/gestion_asegurados.html', context)