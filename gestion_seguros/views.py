from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AltaClienteForm

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

    if request.method == "POST":
        alta_cliente_form = AltaClienteForm(request.POST)
        if alta_cliente_form.is_valid():
            print(alta_cliente_form.cleaned_data['razonSocial'])
            return redirect("index")
    else:
        alta_cliente_form = AltaClienteForm()
    context = {'clientes': clientes, 'form': alta_cliente_form}
    print(request.POST)
    return render(request, 'gestion_seguros/gestion_clientes.html', context)

def gestion_polizas(request):
    context={}
    return render(request, 'gestion_seguros/gestion_polizas.html', context)

def gestion_asegurados(request):
    context={}
    return render(request, 'gestion_seguros/gestion_asegurados.html', context)