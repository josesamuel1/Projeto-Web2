from rest_framework import routers
from appEstoque.api import viewsets

post_router = routers.DefaultRouter()
post_router.register('post', viewsets.PostViewSet)