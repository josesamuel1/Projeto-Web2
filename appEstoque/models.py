from django.db import models
from django.utils import timezone
from datetime import date

class BaseModelQuerySet(models.QuerySet):
    def delete(self):
        self.update(delete_at = timezone.now(), is_active = False)

class BaseManager(models.Manager):
    def get_queryset(self):
        return BaseModelQuerySet(self.model, using = self._db).filter(deleted_at__isnull = True, is_active = True)

class BaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    deleted_at = models.DateTimeField(editable = False, blank = True, null = True)
    is_active = models.BooleanField(editable = False, default = True)
    objects = BaseManager()

    def delete(self, **kwargs):
        self.is_active = False
        self.delete_at = timezone.now()
        self.save()

    def hard_delete(self, **kwargs):
        super(BaseModel, self).delete(**kwargs)


class Produto(models.Model):

    TAMANHOS_DISPONIVEIS = {
        ("P", "p"),
        ("PP", "pp"),
        ("M", "m"),
        ("G", "g"),
        ("GG", "gg"),
        ("XG", "xg"),
    }

    nome = models.CharField(max_length=100, null=False, blank=False)
    quantidade = models.IntegerField(null=False, blank=False, default=0)
    tamanho = models.CharField(max_length=2, null=False, blank=False, choices=TAMANHOS_DISPONIVEIS, default='')
    data = models.DateField(default=date.today, blank=False)
    descricao = models.TextField(null=True, blank=True)


    def __str__(self):
        return f"Produto={self.nome}]"
    

class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False)
    telefone = models.CharField(max_length=11)


    def __str__(self):
        return f"Nome: {self.nome}"
    

class ProdutosInventario(models.Model):
    produtos_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.produtos_count}'

    