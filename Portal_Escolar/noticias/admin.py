from django.contrib import admin
from .models import Categoria, Tag, Noticia, Perfil
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Tag)
admin.site.register(Noticia)
admin.site.register(Perfil)
