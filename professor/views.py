from django.shortcuts import render
from rest_framework import viewsets
from professor.serializers import ProfessorSerializer
from professor.models import Professor

from rest_framework.filters import SearchFilter

# Create your views here.

class ProfessorViewSets(viewsets.ModelViewSet):
    filter_backends = [SearchFilter]
    search_fields = ['^nome', '=idade']
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
