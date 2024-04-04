import logging

from rest_framework import viewsets, permissions
from appEstoque import models    
from appEstoque.api import serializers
from .permissions import IsInSpecificGroup

logger = logging.getLogger('custom')


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = models.Produto.objects.all()
    serializer_class = serializers.ProdutoSerializer
    permission_classes = [permissions.IsAuthenticated, IsInSpecificGroup]

    def perform_create(self, serializer):
        logger.info(f'Novo post criado: {self.request.data["nome"]}')
        serializer.save()
