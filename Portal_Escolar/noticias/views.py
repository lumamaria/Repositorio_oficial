from django.shortcuts import render
from .models import Categoria, Tag, Noticia

# Create your views here.

def lista_categorias(request):
    categorias = Categoria.objects.all()

    return render(request, 'categorias/lista.html', {'categorias': categorias})

def detalhe_categorias(request, id):
    categoria = Categoria.objects.get(id=id)

    return render(request, 'categorias/detalhe.html', {'categoria': categoria})


def lista_tags(request):
    tags = Tag.objects.all()

    return render(request, 'tags/lista.html', {'tags': tags})

def detalhe_tags(request, id):
    tag = Tag.objects.get(id=id)

    return render(request, 'tags/detalhe.html', {'tag': tag})


def lista_noticias(request):
    noticias = Noticia.objects.all()

    return render(request, 'noticias/lista.html', {'noticias': noticias})

def detalhe_noticias(request, id):
    noticia = Noticia.objects.get(id=id)

    return render(request, 'noticias/detalhe.html', {'noticia': noticia})
