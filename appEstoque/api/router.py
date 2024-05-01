from rest_framework import routers
from appEstoque.api import viewsets

produto_router = routers.DefaultRouter()
produto_router.register('produto', viewsets.ProdutoViewSet)
produto_router.register('cliente', viewsets.ClienteViewSet)