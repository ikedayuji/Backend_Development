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
    
