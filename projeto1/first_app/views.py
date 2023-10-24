from django.db import models
from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .forms import MyForm
from .forms import movelform
from .models import Escola
from django.views.generic import View
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from .models import Grafico
from .models import Produto1, Vendas, Vendedor
from datetime import datetime
from django.db.models import Sum




def index(request):
    return render(request, "index.html")

def calculadora(request):
    return render(request, "calculadora.html")

def parana(request):
    return render(request, "parana.html")

def formulario_simples(request):
    form = MyForm()
    
    if request.method == 'POST':
        
        form = MyForm(request.POST)
        
        if form.is_valid():
            
            print("Form Validation Sucess. Prints in console")
            print("Name"+form.cleaned_data['name'])
            print("Email"+form.cleaned_data['email'])
            print("Text"+form.cleaned_data['text'])
    return render(request,'movel.html',{'form':form})

def formulario_movel(request):
    form = movelform()
    
    if request.method == 'POST':
        
        form = movelform(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Deu erro")
            
    return render(request,'movel.html',{'form':form})

def hello(request):
    info = {"info": "Olá Mundo vindo do servidor"}
    return render(request, 'index.html', info)

class Helpp(View):
    def get(self, request):
        return HttpResponse("Class-based views em funcionamento!")
        
class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        contexto['info'] = "Olá Mundo vindo do servidor"
        return contexto
    
class EscolaListView(ListView):
    model = Escola
    template_name = 'app1/escola_list.html'

class EscolaCreateView(CreateView):
    model = Escola
    fields = ("nome", "diretor", "endereco")
    
class EscolaDetailView(DetailView):
    model = Escola
    context_object_name = 'escola_details'
    
class EscolaUpdateView(UpdateView):
    model = Escola
    fields = ("nome", "diretor")
    
class EscolaDeleteView(DeleteView):
    model = Escola
    sucess_url = reverse_lazy("app1:escola-list")
    
class UsuarioInfoPerfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    site_portfolio = models.URLField(blank=True)
    foto_perfil = models.ImageField(upload_to='fotos_perfil')
    
    def __str__(self):
        return self.user.username
    
class UsuarioInfoPerfilForm(forms.ModelForm):
    class Meta():
        model = UsuarioInfoPerfil
        fields = ('site_portfolio','foto_perfil')
        
class UserForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ('username', 'email','password')    

def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('app1/castrar_usuario.html')
    else:
        form = UserCreationForm()
    return render(request, 'app1/cadastrar_usuario.html', {'form': form})

def login_usuario(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('app1/login_usuario.html')
    else:
        form = AuthenticationForm()
    return render(request, 'app1/login_usuario.html', {'form': form})

def logout_usuario(request):
    logout(request)
    return redirect('app1/logout_usuario.html')

def home(request):
    exibirCartoes = True  
    graficosData = Grafico.objects.all() 

    context = {
        'exibirCartoes': exibirCartoes,
        'graficosData': graficosData,
    }
    
    return render(request, 'jornadahome.html')

def card_list(request):
    cards = Card.objects.all()
    return render(request, 'card-list.html', {'cards': cards})

def home(request):
    return render(request, 'home.html')

def retorna_total_vendido(request):
    total = Vendas.objects.all().aggregate(Sum('total'))['total__sum']
    if request.method == "GET":
        return JsonResponse({'total': total})

def relatorio_faturamento(request):
    x = Vendas.objects.all()
    
    meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    data = []
    labels = []
    cont = 0
    mes = datetime.now().month + 1
    ano = datetime.now().year
    for i in range(12): 
        mes -= 1
        if mes == 0:
            mes = 12
            ano -= 1
        
        y = sum([i.total for i in x if i.data.month == mes and i.data.year == ano])
        labels.append(meses[mes-1])
        data.append(y)
        cont += 1

    data_json = {'data': data[::-1], 'labels': labels[::-1]}
     
    return JsonResponse(data_json)

def relatorio_produtos(request):
    produtos = Produto1.objects.all()
    label = []
    data = []
    for produto1 in produtos:
        vendas = Vendas.objects.filter(nome_produto=produto1).aggregate(Sum('total'))
        if not vendas['total__sum']:
            vendas['total__sum'] = 0
        label.append(produto.nome)
        data.append(vendas['total__sum'])

    x = list(zip(label, data))

    x.sort(key=lambda x: x[1], reverse=True)
    x = list(zip(*x))
    
    return JsonResponse({'labels': x[0][:3], 'data': x[1][:3]})

def relatorio_funcionario(request):
    vendedores = Vendedor.objects.all()
    label = []
    data = []
    for vendedor in vendedores:
        vendas = Vendas.objects.filter(vendedor=vendedor).aggregate(Sum('total'))
        if not vendas['total__sum']:
            vendas['total__sum'] = 0
        label.append(vendedor.nome)
        data.append(vendas['total__sum'])

    x = list(zip(label, data))

    x.sort(key=lambda x: x[1], reverse=True)
    x = list(zip(*x))
    
    return JsonResponse({'labels': x[0][:3], 'data': x[1][:3]})