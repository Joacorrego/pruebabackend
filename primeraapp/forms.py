from django import forms
from primeraapp.models import Productos
from primeraapp.models import Area
from django.core import validators


class FormProyecto(forms.ModelForm):

  nombre = forms.CharField(validators=[
   validators.MinLengthValidator(5),
   validators.MaxLengthValidator(15)
   
  ])

  marca = forms.CharField(validators=[
   validators.MinLengthValidator(5),
   validators.MaxLengthValidator(15)
  ])

  fecha_expiracion = forms.CharField(validators=[
   validators.MinLengthValidator(5),
   validators.MaxLengthValidator(15)
  ])

  peso = forms.CharField(validators=[
   validators.MinLengthValidator(5),
   validators.MaxLengthValidator(11)
  ])

     
     
  class Meta:
        model = Productos
        fields = '__all__'


class formArea(forms.ModelForm):
  
   nombre = forms.CharField(validators=[
   validators.MinLengthValidator(5),
   validators.MaxLengthValidator(15)
   
  ])

   tamanio = forms.CharField(validators=[
   validators.MinLengthValidator(5),
   validators.MaxLengthValidator(15)
  ])

   ubicacion = forms.CharField(validators=[
   validators.MinLengthValidator(5),
   validators.MaxLengthValidator(15)
  ])

   maxi_person = forms.CharField(validators=[
   validators.MinLengthValidator(5),
   validators.MaxLengthValidator(11)
  ])

   estado = forms.CharField(validators=[
   validators.MinLengthValidator(5),
   validators.MaxLengthValidator(11)
  ])
     
     
     
     
   class Meta:
        model = Area
        fields = '__all__'    

