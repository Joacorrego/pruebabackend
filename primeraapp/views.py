from django.shortcuts import render
from django.http import HttpResponse
from primeraapp.models import Productos
from . import forms
from primeraapp.forms import FormProyecto
from primeraapp.models import Productos
from django.shortcuts import redirect
from evaApp.views import index
from primeraapp.models import Area
from primeraapp.forms import formArea
# Create your views here.

def productosData(request):
    productos = Productos.objects.all()
    data = {'productos' : productos}
    return render(request, 'templatesapp/productos.html',data)


def userRegistrationView(request):
    form = forms.UserRegistrationForm()

    if request.method == 'POST':
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            print("form es valido")
            print("nombre: ", form.cleaned_data['nombre'])
            print("email: ", form.cleaned_data['email'])
            print("fono: ", form.cleaned_data['fono'])
            

    data = {'form' : form}
    return render(request, 'templatesapp/userRegistration.html', data)

def ListadoProducto(request):
    productos = Productos.objects.all()
    data = {'productos' : productos}
    return render(request, 'templatesapp/productos.html', data)

def agregarProducto(request):
    form = FormProyecto()
    if request.method == 'POST' :
        form = FormProyecto(request.POST)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'templatesapp/agregarProductos.html', data)


def eliminarProducto(request, id):
    producto = Productos.objects.get(id = id)
    producto.delete()
    return redirect('/productos')


def actualizarProducto(request, id):
    producto = Productos.objects.get(id = id)
    form = FormProyecto(instance=producto)
    if request.method =='POST' :
        form = FormProyecto(request.POST, instance=producto)
        if form.is_valid() :
            form.save()
            return index(request)
    data = {'form' : form}
    return render(request, 'templatesapp/agregarProductos.html', data)


def listadoarea(request):
    areas = Area.objects.all()
    data = {'areas' : areas}
    return render(request, 'templatesapp/areas.html',data)


def agregararea(request):
    form = formArea()
    if request.method == 'POST' :
        form = formArea(request.POST)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'templatesapp/agregararea.html', data)

def eliminarArea(request, id):
    area = Area.objects.get(id = id)
    area.delete()
    return redirect('/areas')

def modificarArea(request, id):
    area = Area.objects.get(id = id)
    form = formArea(instance=area)
    if request.method == 'POST':
        form = formArea(request.POST, instance=area)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'templatesapp/agregararea.html', data)