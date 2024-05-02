from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from appEstoque.models import Produto, ProdutosInventario


def produtos_inventario_update():
    produtos_count = Produto.objects.all().count()
    ProdutosInventario.objects.create(produtos_count=produtos_count)

    
@receiver(post_save, sender=Produto)
def produtos_post_save(sender, instance, **kwargs):
    produtos_inventario_update()


@receiver(post_delete, sender=Produto)
def produtos_post_delete(sender, instance, **kwargs):
    produtos_inventario_update()
