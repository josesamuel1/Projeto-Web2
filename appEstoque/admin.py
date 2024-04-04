from django.contrib import admin
from .models import Post, Produto, Cliente

@admin.register(Produto)
class ProdutosEstoque(admin.ModelAdmin):
    list_display = ('nome', 'quantidade')
    search_fields = ('tamanho',)

@admin.register(Cliente)
class ClientesEstoque(admin.ModelAdmin):
    list_display = ('nome', 'cpf')
    search_fields = ('nome', 'cpf')

admin.site.register(Post)

