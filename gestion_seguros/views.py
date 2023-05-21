from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import AltaClienteForm, AltaPolizaForm
from .models import Cliente, Poliza

# Create your views here.
def index(request):
    context={}
    return render(request, 'gestion_seguros/index.html', context)

def gestion_clientes(request):
    clientes=Cliente.objects.all()

    if request.method == "POST":
        form = AltaClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Cliente dado de alta')
            return redirect("gestion_clientes")
        else:
            pass
    else:
        form = AltaClienteForm()
    context = {'clientes': clientes, 'form': form}
    return render(request, 'gestion_seguros/gestion_clientes.html', context)

def gestion_polizas(request):
    polizas=Poliza.objects.all()

    if request.method == "POST":
        form = AltaPolizaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Poliza dada de alta')
            return redirect("gestion_polizas")
        else:
            pass
    else:
        form = AltaPolizaForm()
    context = {'polizas': polizas, 'form': form}
    return render(request, 'gestion_seguros/gestion_polizas.html', context)

def gestion_asegurados(request):
    context={}
    return render(request, 'gestion_seguros/gestion_asegurados.html', context)