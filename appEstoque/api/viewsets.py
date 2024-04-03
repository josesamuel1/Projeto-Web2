import logging

from rest_framework import viewsets, permissions
from appEstoque import models    
from appEstoque.api import serializers
from .permissions import IsInSpecificGroup

logger = logging.getLogger('custom')

class PostViewSet(viewsets.ModelViewSet):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsInSpecificGroup]

    def perform_create(self, serializer):
        logger.info(f'Novo post criado: {self.request.data["nome"]}')
        serializer.save()

class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        logger.info('O middleware foi executado: Obtendo requisição...')

        if 'X-Meu_Header' in request.headers:
            request.session['meu_header'] = request.headers['X-Meu-Header']
            logger.info('Valor do cabeçalho armazenado na sessão: %s', request.session['meu_header'])
        
        response = self.get_response(request)

        logger.info('O middleware foi executado: Obtendo resposta...')

        return response