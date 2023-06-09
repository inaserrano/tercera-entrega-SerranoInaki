from django.urls import path
from AppEntrega import views

urlpatterns = [
    path('',views.inicio, name='inicio'), 
]