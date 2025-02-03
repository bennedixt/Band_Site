
"""
ASGI configuration for the band_site project.

This file exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see:
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

# Setting the default Django settings module for ASGI
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "band_site.settings")

application = get_asgi_application()

