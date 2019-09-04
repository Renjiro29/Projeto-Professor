from django.shortcuts import render
from landing.models import Aluno

# Create your views here.

def index(request):

    if request.method == 'POST':
        aluno = Aluno()
        aluno.nome = request.POST.get('nome')
        aluno.idade = request.POST.get('sobrenome')
        aluno.email = request.POST.get('email')
        aluno.save()

         contexto = {
            'nome': pessoa.nome,
        }
        return render(request, 'login.html', contexto)
