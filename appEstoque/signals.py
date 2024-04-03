from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post

@receiver(post_save, sender = Post)
def update_pub_date (sender, instance, created, **kwargs):
    if created:
        instance.pub_date = instance.created_at
    
    instance.save(update_fields = ['pub_date'])