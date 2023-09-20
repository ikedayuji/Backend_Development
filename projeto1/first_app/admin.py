#from django.contrib import admin
#from django.urls import path, include

#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('', include('first_app.urls')), 
#]

from django.contrib import admin
from .models import Topic, Webpage, AccessRecord, Movel, Cliente, Filme

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(Movel)

class FilmeAdmin(admin.ModelAdmin):

    fields = ['ano_lancamento', 'titulo', 'duracao']

    search_fields = ['ano_lancamento','titulo', 'duracao']
    list_filter = ['ano_lancamento', 'titulo', 'duracao']
    list_display = ['ano_lancamento', 'titulo', 'duracao']

admin.site.register(Cliente)
admin.site.register(Filme, FilmeAdmin)