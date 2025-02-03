"""
App configuration for the Blog application.
"""

from django.apps import AppConfig

class BlogConfig(AppConfig):
    """
    Configuration class for the Blog application.

    Attributes:
        default_auto_field (str): Specifies the default auto field type for models.
        name (str): The name of the application.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "blog"