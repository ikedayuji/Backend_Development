from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index.html'), 
    path('calculadora/', views.calculadora, name='calculadora'),
    path('parana/', views.parana, name='parana'),
    path('form_simples/', views.formulario_simples, name= 'formsimples'),
]
