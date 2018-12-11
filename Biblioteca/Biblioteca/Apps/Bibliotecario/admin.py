from django.contrib import admin
from Biblioteca.Apps.Bibliotecario.models import *

# Register your models here.

admin.site.register(Persona)
admin.site.register(Categorias)
admin.site.register(Libro)
admin.site.register(Prestamo)
admin.site.register(Registro)
