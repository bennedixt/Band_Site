"""
URL configuration for the Blog application.

Defines routes for blog-related views.
"""

from django.urls import path
from . import views

app_name = 'blog'  # Namespace for app-specific URL names

urlpatterns = [
    path('tour/', views.tour, name='tour'),  # Tour page
    path('grammys/', views.grammys, name='grammys'),  # Grammys page
]


