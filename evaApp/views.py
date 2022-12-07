from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from evaApp.models import Empleados
from . import forms
from evaApp.forms import registroEmpleadoForm


# Create your views here.

def index(request):
    return render(request, 'evaApp/index.html')

def empleadosData(request):
    empleados = Empleados.objects.all()
    data = {'empleados' : empleados}
    return render(request, 'evaApp/empleados.html', data)

def registroEmpleadoView(request):
    form = registroEmpleadoForm()
    
    if request.method == "POST":
        form = registroEmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'evaApp/registroEmpleado.html', data)

def eliminarEmpleado(request, id):
    empleado = Empleados.objects.get(id = id)
    empleado.delete()
    return redirect('/empleados')

def modificarEmpleado(request, id):
    empleado = Empleados.objects.get(id = id)
    form = registroEmpleadoForm(instance=empleado)
    if request.method == 'POST':
        form = registroEmpleadoForm(request.POST, instance=empleado)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'evaApp/registroEmpleado.html', data)
    
