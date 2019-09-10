from django.shortcuts import render
from landing.models import Aluno
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication

from landing.serializers import AlunoSerializer

from rest_framework.filters import SearchFilter


# Create your views here.
class AlunoViewSets(viewsets.ModelViewSet): 
    filter_backends = [SearchFilter]
    search_fields = ['^nome', '=idade']
    queryset = Aluno.objects.all()
    #permission_classes = (IsAuthenticatedOrReadOnly,)
    #authentication_classes = (TokenAuthentication,)
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
