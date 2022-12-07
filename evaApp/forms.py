from pyexpat import model
from django import forms
from django.core import validators
from evaApp.models import Empleados


class registroEmpleadoForm(forms.ModelForm):
   
   
   nombre = forms.CharField(validators=[
   validators.MinLengthValidator(5),
   validators.MaxLengthValidator(20)
  ])

   rut = forms.CharField(validators=[
   validators.MinLengthValidator(5),
   validators.MaxLengthValidator(13)
  ])

   cargo = forms.CharField(validators=[
   validators.MinLengthValidator(5),
   validators.MaxLengthValidator(25)
  ])

   fono = forms.CharField(validators=[
   validators.MinLengthValidator(5),
   validators.MaxLengthValidator(9)
  ])


   class Meta:
        model = Empleados
        fields = '__all__'

