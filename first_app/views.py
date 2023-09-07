from django.shortcuts import render
from django.http import HttpResponse
from .forms import ForName


def index(request):
    return HttpResponse("index.html")

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
    return render(request,'form_simples.html',{'form':form})


        
    
