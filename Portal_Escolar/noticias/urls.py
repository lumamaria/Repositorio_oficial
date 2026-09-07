from django.urls import path
from . import views


urlpatterns = [
    path('', views.lista_noticias, name='inicio'),

    path('categorias/', views.lista_categorias, name='lista_categorias'),
    path('categorias/<int:id>/', views.detalhe_categorias, name='detalhe_categorias'),

    path('tags/', views.lista_tags, name='lista_tags'),
    path('tags/<int:id>/', views.detalhe_tags, name='detalhe_tags'),

    path('noticias/', views.lista_noticias, name='lista_noticias'),
    path('noticias/<int:id>/', views.detalhe_noticias, name='detalhe_noticias'),
]