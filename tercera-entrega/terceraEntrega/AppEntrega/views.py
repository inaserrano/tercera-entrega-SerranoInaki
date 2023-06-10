
from django.shortcuts import render
from .models import Curso,Entrenador,Socio
from AppEntrega.forms import CursoFormulario,entrenadorFormulario,socioFormulario

def inicio(request):
    return render(request,"AppEntrega/index.html")

def cursos(request):
    return render(request, "AppEntrega/guardar_curso.html")

def formulario(request):
    if request.method == 'POST':
        print(f"\n\n{request.POST}\n\n")
        curso = Curso(nombre=request.POST['curso'], camada=request.POST['camada'])
        curso.save()
        return render(request, "AppEntrega/index.html")        
    return render(request, "AppEntrega/formulario.html")

def jugador_formulario(request):
      if request.method == "POST":
            miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  curso = Curso(nombre=informacion["jugador"], camada=informacion["categoria"])
                  curso.save()
                  return render(request, "AppEntrega/index.html")
      else:
            miFormulario = CursoFormulario()
      return render(request, "AppEntrega/form_api.html", {"miFormulario": miFormulario})
  
def entrenador_Formulario(request):
    if request.method == 'POST':
        miFormulario = entrenadorFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            entrenador = Entrenador(nombre=informacion['nombre'],apellido=informacion['apellido'],email=informacion['email'])
            entrenador.save()
            return render(request,"AppEntrega/index.html")
    else:
        miFormulario = entrenadorFormulario()
    return render(request,"AppEntrega/form_entrenador.html",{"miFormulario":miFormulario})

def socio_formulario(request):
    if request.method == 'POST':
        miFormulario = socioFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            socio = Socio(nombre=informacion['nombre'],email=informacion['email'],dni=informacion['dni'],num_socio=informacion['num_socio'])
            socio.save()
            return render(request,"AppEntrega/index.html")
        else:
            miFormulario = socioFormulario()
        return render(request,"AppEntrega/form_socio.html",{"miFormulario":miFormulario})