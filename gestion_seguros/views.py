from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.forms.models import model_to_dict
from .forms import AltaClienteForm, AltaPolizaForm, ModificarClienteForm, ModificarPolizaForm
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

def cartera_cliente(request, cliente_id):
    cliente=Cliente.objects.filter(id = cliente_id)[0]   #Entender si es la mejor manera indexar con 0
    polizas=Poliza.objects.filter(cliente_id = cliente_id)
    context = {'cliente': cliente, 'polizas': polizas}
    return render(request, 'gestion_seguros/cartera_cliente.html', context)

def detalle_cliente(request, cliente_id):
    cliente=Cliente.objects.get(id = cliente_id) 
    if request.method == "POST":
        form = ModificarClienteForm(request.POST)
        if form.is_valid():
            Cliente.objects.filter(id = cliente_id).update(
                nombre=form.cleaned_data["nombre"],
                documento=form.cleaned_data["documento"],
                email=form.cleaned_data["email"],
                domicilio_provincia= form.cleaned_data["domicilio_provincia"],
                domicilio_ciudad= form.cleaned_data["domicilio_ciudad"],
                domicilio_calle= form.cleaned_data["domicilio_calle"],
                domicilio_numero= form.cleaned_data["domicilio_numero"],
                domicilio_depto= form.cleaned_data["domicilio_depto"],
                telefono= form.cleaned_data["telefono"],
                tipo_persona= form.cleaned_data["tipo_persona"]
            )
            messages.add_message(request, messages.SUCCESS, 'Cliente modificado con éxito')
        else:
            pass
    else:
        form = ModificarClienteForm(initial = model_to_dict(cliente))
    context = {'cliente': cliente, 'form': form}
    return render(request, 'gestion_seguros/detalle_cliente.html', context)

def detalle_poliza(request, poliza_id):
    poliza=Poliza.objects.get(id = poliza_id) 
    if request.method == "POST":
        form = ModificarPolizaForm(request.POST)
        if form.is_valid():
            Poliza.objects.filter(id = poliza_id).update(
                cliente=form.cleaned_data["cliente"],
                numero=form.cleaned_data["numero"],
                tomador=form.cleaned_data["tomador"],
                limite_asegurados= form.cleaned_data["limite_asegurados"],
                fecha_inicio= form.cleaned_data["fecha_inicio"],
                fecha_fin= form.cleaned_data["fecha_fin"],
                fecha_limite_carga= form.cleaned_data["fecha_limite_carga"],
                condiciones= form.cleaned_data["condiciones"],
            )
            messages.add_message(request, messages.SUCCESS, 'Póliza modificado con éxito')
        else:
            pass
    else:
        form = ModificarPolizaForm(initial = model_to_dict(poliza))
    context = {'poliza': poliza, 'form': form}
    return render(request, 'gestion_seguros/detalle_poliza.html', context)