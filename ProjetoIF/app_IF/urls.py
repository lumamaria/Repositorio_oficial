from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('detalhes_aluno/<int:id>', views.detalhes_aluno, name='detalhes_aluno'),
    path('detalhes_project/<int:id>/', views.detalhes_projeto, name='detalhes_projeto'),
    path('listagem_prog', views.listagem_projetos, name='listagem_projetos'),
]


