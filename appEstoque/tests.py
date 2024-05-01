import json

from django.test import TestCase
from .models import Cliente, Produto
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