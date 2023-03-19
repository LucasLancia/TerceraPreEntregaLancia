from django import forms

class CursoForms(forms.Form):
    nombre=forms.CharField(min_length=3,max_length=20)
    camada=forms.CharField(max_length=30)


class AlumnoFormulario(forms.Form):
    nombre=forms.CharField(max_length=15)
    apellido=forms.CharField(max_length=15)
    telefono=forms.CharField(max_length=15)
    email=forms.CharField(max_length=40)
    direccion=forms.CharField(max_length=40)

class BusquedaCursoForms(forms.Form):
    nombre=forms.CharField(min_length=3,max_length=20)
