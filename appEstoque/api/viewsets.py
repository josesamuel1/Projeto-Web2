import logging

from rest_framework import viewsets, permissions
from appEstoque import models    
from appEstoque.api import serializers
from .permissions import IsInSpecificGroup

logger = logging.getLogger('custom')


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = models.Produto.objects.all()
    serializer_class = serializers.ProdutoSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        logger.info(f'Novo produto adicionado: {self.request.data["nome"]}')
        serializer.save()


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = models.Cliente.objects.all()
    serializer_class = serializers.ClienteSerializer

    def perform_create(self, serializer):
        logger.info(f'Novo cliente adicionado: {self.request.data["nome"]}')
        serializer.save()
