from django.urls import path
from . import views
from  django.conf import settings
app_name = 'first_app'

urlpatterns = [
    path('index/', views.index, name='index'), 
    path('calculadora/', views.calculadora, name='calculadora'),
    path('parana/', views.parana, name='parana'),
    path('formulario/', views.formulario_simples, name= 'formsimples'),
    path('Movel/', views.formulario_movel, name = 'movel'),
    path('escola/list', views.EscolaListView.as_view(), name='escola-list'),
    path('escolas/<int:pk>/', views.EscolaDetailView.as_view(), name='escola-detail'),
    path('escola/create', views.EscolaCreateView.as_view(), name='escola-create'),
    path('escola/update/int:pk/', views.EscolaUpdateView.as_view(), name='escola-update'),
    path('escola/delete/<int:pk>/', views.EscolaDeleteView.as_view(), name='escola-delete'),
    ]
