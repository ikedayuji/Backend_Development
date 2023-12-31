from django.urls import path
from . import views
from  django.conf import settings
from first_app import views
from .views import card_list


app_name = 'first_app'

urlpatterns = [
    path('index/', views.index, name='index'), 
    path('calculadora/', views.calculadora, name='calculadora'),
    path('parana/', views.parana, name='parana'),
    path('formulario/', views.formulario_simples, name= 'formsimples'),
    path('movel/', views.formulario_movel, name = 'movel'),
    path('escola/list', views.EscolaListView.as_view(), name='escola-list'),
    path('escolas/<int:pk>/', views.EscolaDetailView.as_view(), name='escola-detail'),
    path('escola/create', views.EscolaCreateView.as_view(), name='escola-create'),
    path('escola/update/int:pk/', views.EscolaUpdateView.as_view(), name='escola-update'),
    path('escola/delete/<int:pk>/', views.EscolaDeleteView.as_view(), name='escola-delete'),
    path('cadastrar/', views.cadastrar_usuario, name='cadastrar'),
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
    path('jornada/', views.home, name='jornadahome'),
    path('card-list/', card_list, name='card_list'),
    path('graficos/', views.home, name="home"),
    path('retorna_total_vendido', views.retorna_total_vendido, name="retorna_total_vendido"),
    path('relatorio_faturamento', views.relatorio_faturamento, name="relatorio_faturamento"),
    path('relatorio_produtos', views.relatorio_produtos, name="relatorio_produtos"),
    path('relatorio_funcionario', views.relatorio_funcionario, name="relatorio_funcionario"),
]
