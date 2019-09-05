from django.shortcuts import render
from rest_framework import viewsets
from professor.serializers import ProfessorSerializer
from professor.models import Professor

# Create your views here.

class ProfessorViewSets(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
