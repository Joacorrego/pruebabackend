from django.contrib import admin
from evaApp.models import Empleados

class EmpleadosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'rut', 'cargo', 'fono', 'area']

# Register your models here.
admin.site.register(Empleados, EmpleadosAdmin)
