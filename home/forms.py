from django import forms

class FormularioCreacionCliente(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email= forms.CharField(max_length=50)