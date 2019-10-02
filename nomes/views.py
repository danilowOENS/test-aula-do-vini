from django.shortcuts import render
from rest_framework import viewsets
from nomes.models import Nome
from nomes.serializers import NomeSerializer


class NomeViewSet(viewsets.ModelViewSet):
    queryset = Nome.objects.all()
    serializer_class = NomeSerializer