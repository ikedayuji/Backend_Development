import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

import random
from first_app.models import Topic, Webpage, AccessRecord
from faker import Faker

fakegen = Faker()
topics = ['Pesquisa', 'Social', 'Marketplace', 'Noticias', 'Jogos']

def add_topics():
    nome = random.choice(topics)
    t, created = Topic.objects.get_or_create(nome=nome)
    if created:
        t.save()
    return t

if __name__ == '__main__':
    for _ in range(10):
        topic = add_topics()
        print(f'Tópico criado: {topic.nome}')

def populate(n=5):
    for entry in range(n):
        top = add_topics()
        
        url = fakegen.url()
        data = fakegen.date()
        nome = fakegen.company()
        
        pagina, _ = Webpage.objects.get_or_create(topico=top, url=url, nome=nome)
        
        registro, _ = AccessRecord.objects.get_or_create(pagina=pagina, data=data)
        
    print("Populando o BD... Por favor aguarde.")

populate(20)
