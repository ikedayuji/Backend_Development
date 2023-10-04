from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import ForName
from .forms import movelform
from .models import Escola
from django.views.generic import View
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView


def index(request):
    return render(request, "index.html")

def calculadora(request):
    return render(request, "calculadora.html")

def parana(request):
    return render(request, "parana.html")

def formulario_simples(request):
    form = ForName()
    
    if request.method == 'POST':
        
        form = form.FormName(request.POST)
        
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

