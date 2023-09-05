#from django.contrib import admin
#from django.urls import path, include

#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('', include('first_app.urls')), 
#]

from django.contrib import admin
from .models import Topic, Webpage, AccessRecord

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)