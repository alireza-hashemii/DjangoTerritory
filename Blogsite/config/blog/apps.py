from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"
    verbose_name = 'مقاله'
    verbose_name_plural = "مقالات"
