from django.shortcuts import render
from .models import Aluno, Projeto
# Create your views here.

def detalhes_aluno(request, id):
    aluno = Aluno.objects.get(id=id)

    return render(request, 'app_IF/detalhes_aluno.html', {'aluno': aluno})


def detalhes_projeto(request, id):
    projeto = Projeto.objects.get(id=id)

    return render(request, 'app_IF/detalhes_projeto.html', {'projeto': projeto})


def listagem_projetos(request):
    projetos = Projeto.objects.all()

    return render(request, 'projeto/listagem_projetos.html', {'projetos': projetos})





