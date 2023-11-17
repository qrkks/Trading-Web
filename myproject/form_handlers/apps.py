from django.apps import AppConfig


class FormHandlersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "form_handlers"
    verbose_name = "form handlers"

    def ready(self):
        import form_handlers.signals