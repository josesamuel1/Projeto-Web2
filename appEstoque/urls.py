from django.urls import path
from appEstoque.views import index

urlpatterns = [
    path('', index, name='index'),

]