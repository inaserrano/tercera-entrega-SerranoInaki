from django import forms

class CursoFormulario(forms.Form):
    jugador = forms.CharField()
    categoria = forms.IntegerField()
    
class entrenadorFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class socioFormulario(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()
    dni = forms.IntegerField()
    num_socio = forms.IntegerField()