from django.contrib import admin
from .models import Categoria, Tag, Noticia, Perfil


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('titulo',)
    search_fields = ('titulo',)

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria')
    search_fields = ('titulo', 'texto')
    list_filter = ('categoria',)

class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'bio')
    search_fields = ('usuario__username',)


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Perfil, PerfilAdmin)