from django.shortcuts import render
from rest_framework import viewsets,permissions

from .serializers import LivreListeSerializers, LivreSerializers

from .models import Livre, LivreListe

class Livre_ViewSet(viewsets.ModelViewSet):
    queryset=Livre.objects.all()
    serializer_class=LivreSerializers
    """permission_classes=(permissions.IsAuthenticated,)"""
    filterset_fields=['id','titre']
    search_fields=['titre']

class livreLIste_ViewSet(viewsets.ModelViewSet):
    queryset=LivreListe.objects.all()
    serializer_class=LivreListeSerializers

