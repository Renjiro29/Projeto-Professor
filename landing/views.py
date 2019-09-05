from django.shortcuts import render
from landing.models import Aluno
from rest_framework import viewsets
from landing.serializers import AlunoSerializer


# Create your views here.
class AlunoViewSets(viewsets.ModelViewSet): 
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


# def index(request):

#     if request.method == 'POST':
#         aluno = Aluno()
#         aluno.nome = request.POST.get('nome')
#         aluno.idade = request.POST.get('sobrenome')
#         aluno.email = request.POST.get('email')
#         aluno.save()

#          contexto = {
#             'nome': pessoa.nome,
#         }
#         return render(request, 'login.html', contexto)
