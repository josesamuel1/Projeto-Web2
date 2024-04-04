from django.db import models
from django.utils import timezone

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

class Post(models.Model):
    titulo = models.CharField(max_length = 200)
    descricao = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.titulo

class Categoria(models.Model):
    nome = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length = 100)
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    preco = models.DecimalField(max_digits = 5, decimal_places = 2)
    descricao = models.TextField(null = True)

    def __str__(self):
        return self.nome
