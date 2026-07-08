from django.apps import AppConfig


class CMSConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.cms"

    def ready(self):

        from .registry.discovery import discover_modules

        discover_modules()
