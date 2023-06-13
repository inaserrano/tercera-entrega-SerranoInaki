from django.urls import path
from AppEntrega import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('formulario/', views.formulario, name="Formulario"),
    path('form_entrenador/', views.entrenador_Formulario, name="Form-entrenador"),
    path('form_socio/', views.socio_formulario, name="Form-socio"),
    path('buscar_jugador/',views.buscar_jugador, name="Buscar-jugador"),
    path('buscar_jugador/',views.buscar_jugador, name="Buscar-jugador"),
    path('buscar_socio/',views.buscar_socio, name="Buscar-socio"),
    path('buscar_entrenador/',views.buscar_entrenador, name="Buscar-entrenador")
]