"""
URL configuration for the band_site project.

Defines the main URL patterns that map views and applications to different routes.

Examples:
    - Function views: 
        1. Import a view: from my_app import views
        2. Add a URL pattern: path('', views.home, name='home')

    - Class-based views:
        1. Import a view: from other_app.views import Home
        2. Add a URL pattern: path('', Home.as_view(), name='home')

    - Including another URL configuration:
        1. Import `include`: from django.urls import include, path
        2. Add a URL pattern: path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin interface
    path('', include('band.urls')),  # Root URL maps to the band app
    path('accounts/', include('django.contrib.auth.urls')),  # Authentication URLs
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),  # Blog app URLs
]



