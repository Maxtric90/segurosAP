from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import AltaClienteForm
from .models import Cliente

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
    context={}
    return render(request, 'gestion_seguros/gestion_polizas.html', context)

def gestion_asegurados(request):
    context={}
    return render(request, 'gestion_seguros/gestion_asegurados.html', context)