from django.urls import path
from AppEntrega import views

urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('formulario/', views.formulario, name="Formulario"),
    path('form_api/', views.jugador_formulario, name="Form-api"),
    path('form_entrenador/', views.entrenador_Formulario, name="Form-entrenador"),
    path('form_socio/', views.socio_formulario, name="Form-socio"),
]