from django.apps import AppConfig

class appEstoqueConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appEstoque'

    def ready(self):
        import appEstoque.signals

    