from django.urls import path
from . import views

app_name = 'first_app'

urlpatterns = [
    path('index/', views.index, name='index'), 
    path('calculadora/', views.calculadora, name='calculadora'),
    path('parana/', views.parana, name='parana'),
    path('formulario/', views.formulario_simples, name= 'formsimples'),
    path('Movel/', views.formulario_movel, name = 'movel')
]
