from django.apps import AppConfig

class Testeapp1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appEstoque'

class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
    
    def ready(self):
        import posts.signals