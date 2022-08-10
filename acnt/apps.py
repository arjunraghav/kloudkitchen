from django.apps import AppConfig


class AcntConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'acnt'

    def ready(self):
        import acnt.signals
