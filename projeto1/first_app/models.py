from django.db import models
from typing import ClassVar
import datetime

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
    sobrenome = models.CharField(max_length=256)
    telefone = models.PositiveIntegerField()
    
class Escola(models.Model):
    nome = models.CharField(max_length=256)
    diretor = models.CharField(max_length=256)
    endereco = models.CharField(max_length=256)
    
    def __str__(self):
        return self.nome

class Estudante(models.Model):
    nome = models.CharField(max_length=256)
    idade = models.PositiveBigIntegerField()
    escola = models.ForeignKey(Escola, related_name='estudantes', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome

class Grafico(models.Model):
    titulo = models.CharField(max_length=255)
    conteudo = models.TextField()

    def __str__(self):
        return self.titulo

class Card(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image_path = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Produto1(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome

class Vendedor(models.Model):
    nome = models.CharField(max_length=50)


    def __str__(self) -> str:
        return self.nome

class Vendas(models.Model):
    nome_produto = models.ForeignKey(Produto1, on_delete=models.DO_NOTHING)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.DO_NOTHING)
    total = models.FloatField()
    data = models.DateTimeField(default=datetime.datetime.now())


    def __str__(self):
        return self.nome_produto.nome