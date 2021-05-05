from django.contrib import admin

# Register your models here.

from .models import *   #Llama a las base de datos

admin.site.register(Estudiante)
admin.site.register(Tag)
admin.site.register(Estado)
admin.site.register(Trabajo)
admin.site.register(Empresa)