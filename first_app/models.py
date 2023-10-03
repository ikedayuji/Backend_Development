from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=100)

class Webpage(models.Model):
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name
    
class AccessRecord(models.Model):  
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
    
class Movel(models.Model):
    name = models.CharField(max_length=100)
    preco = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name
    
class Filme(models.Model):
    titulo = models.CharField(max_length=256)
    duracao = models.PositiveIntegerField
    ano_lancamento = models.PositiveIntegerField
    
class Cliente(models.Model):
    nome = models.CharField(max_length=256)
    sobrenome = models.CharField(max_length=10)
    telefone = models.PositiveIntegerField()
    
class Escola(models.Model):
    nome = models.Charfield(max_length=256)
    diretor = models.Charfield(max_length=256)
    endereco = models.Charfield(max_length=256)
    
    def __str__(self) -> str:
        return self.nome

class Estudante(models.Models):
    nome = models.CharField(max_length=256)
    idade = models.PositiveBigIntegerField()
    escola = models.ForeignKey(Escola, related_name=256)
    
    def __str__(self):
        return self.nome
    
class EscolaDetailView(DetailView):
    model = Escola
    context_object_name = 'escola_details'
    
class EscolaCreateView(CreateView):
    model = Escola
    fields = ("nome", "diretor", "endereco")
    
class EscolaUpdateView(UpdateView):
    model = Escola
    fields = ("nome", "diretor")