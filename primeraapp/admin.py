from django.contrib import admin
from primeraapp.models import Productos
# Register your models here.
class ProductosAdmin(admin.ModelAdmin):
    list_display = ['nombre','marca','fecha_expiracion','peso','area']




admin.site.register(Productos)