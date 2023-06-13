
from django.shortcuts import render
from django.http import HttpResponse 
from .models import Curso,Entrenador,Socio
from AppEntrega.forms import CursoFormulario,entrenadorFormulario,socioFormulario,BuscaJugador,BuscaSocioForm,BuscaEntrenadorForm

def inicio(request):
    return render(request,"AppEntrega/index.html")
# ---------------------------------------------------------------------------------------------------------
def cursos(request):
    return render(request, "AppEntrega/guardar_curso.html")
# ---------------------------------------------------------------------------------------------------------
def formulario(request):
    if request.method == 'POST':
        print(f"\n\n{request.POST}\n\n")
        curso = Curso(nombre=request.POST['curso'], camada=request.POST['camada'])
        curso.save()
        return render(request, "AppEntrega/index.html")        
    return render(request, "AppEntrega/formulario.html")
# ---------------------------------------------------------------------------------------------------------
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
# ---------------------------------------------------------------------------------------------------------
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
# ---------------------------------------------------------------------------------------------------------
def socio_formulario(request):
    if request.method == 'POST':
        miFormulario = socioFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            sociof = Socio(nombre=informacion['nombre'],email=informacion['email'],dni=informacion['dni'],num_socio=informacion['num_socio'])
            sociof.save()
            return render(request,"AppEntrega/index.html")
    else:
        miFormulario = socioFormulario()
    return render(request,"AppEntrega/form_socio.html",{"miFormulario":miFormulario})
# ---------------------------------------------------------------------------------------------------------
def buscar_jugador (request):
    if request.method == "POST":
        busca_jugador = BuscaJugador(request.POST)
        if busca_jugador.is_valid():
            informacion = busca_jugador.cleaned_data
            nombres = Curso.objects.filter(nombre=informacion["nombre"])
            return render(request, "AppEntrega/jugador_lista.html",{"nombres":nombres})
    else:
        busca_jugador = BuscaJugador()
        return render(request,"AppEntrega/busc_jugador.html",{"miFormulario":busca_jugador})

# ---------------------------------------------------------------------------------------------------------

def buscar_socio (request):
    if request.method == "POST":
        busca_socio = BuscaSocioForm(request.POST)
        if busca_socio.is_valid():
            informacion = busca_socio.cleaned_data
            nombres = Socio.objects.filter(nombre=informacion['nombre'])
            return render(request,"AppEntrega/socio_lista.html",{"nombres":nombres})
    else:
        busca_socio = BuscaSocioForm()
        return render(request,"AppEntrega/busc_socio.html",{"miFormulario":busca_socio})

# ---------------------------------------------------------------------------------------------------------
def buscar_entrenador (request):
    if request.method == "POST":
        busca_entrenador = BuscaEntrenadorForm(request.POST)
        if busca_entrenador.is_valid():
            informacion = busca_entrenador.cleaned_data
            nombres = Entrenador.objects.filter(nombre=informacion['nombre'])
            return render(request,"AppEntrega/entrenador_lista.html",{"nombres":nombres})
    else:
        busca_entrenador = BuscaEntrenadorForm() 
        return render(request, "AppEntrega/busc_entrenador.html",{"miFormulario":busca_entrenador})

