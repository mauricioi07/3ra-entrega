from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import Cliente
from home.forms import FormularioCreacionCliente

# Create your views here.
def home(request):
    return render(request, 'home/home.html')
    #return HttpResponse('Home')

def crear_cliente(request):

    #cliente = Cliente(nombre=nombre,apellido=apellido,email=email)
    #cliente.save()

    #request.POST()
    if request.method == "POST":
        formulario = FormularioCreacionCliente()
        if formulario.is_valid():
            nuevo_nombre=formulario.cleaned_data.get("nombre")
            nuevo_apellido=formulario.cleaned_data.get("apellido")
            nuevo_email=formulario.cleaned_data.get("email")

            cliente=Cliente(nombre=nuevo_nombre, apellido=nuevo_apellido, email=nuevo_email)
            cliente.save()

            return redirect("listado_autos")
    else:
        formulario = FormularioCreacionCliente()

    return render(request, 'home/crear_cliente.html', {'formulario' : formulario})

def listado_clientes(request):
    clientes=Cliente.objects.all()
    return render(request, 'home/listado_clientes.html',{'listado_clientes' : clientes})