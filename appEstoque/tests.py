import json

from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken
from .models import Post
from datetime import date
from .models import Produto

class ClienteTest(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(
            nome="João",
            cpf="12345678900",
            telefone="123456789",
         )

class ProdutoTest(TestCase):
    def setUp(self):
        self.produto = Produto.objects.create(
            nome="Camiseta",
            quantidade=10,
            tamanho="M",
            data=date(2024, 4, 5),
            descricao="Camisa amarela",
        )

class PostAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    # def test_delete_post(self):

    #     post = Post.objects.create(title='Teste', content='Conteúdo do teste')

    #     response = self.client.delete(f'/api/produtos/{post.id}/')
    #     self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)
    #     self.assertEqual(Post.objects.count(), 0)
