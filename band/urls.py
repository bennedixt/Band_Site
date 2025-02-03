from django.urls import path, include
from . import views

"""
URL configuration for the band application.

Defines URL patterns that map to view functions in the `views.py` file.

Routes:
    - '': Homepage view.
    - 'members/': List of band members.
    - 'concerts/': List of concerts.
    - 'accounts/': Includes Django's built-in authentication URLs.
    - 'auth/': Includes custom user authentication URLs.
"""

urlpatterns = [
    path('', views.home, name='home'),  # Homepage
    path('members/', views.band_members, name='band_members'),  # Band members list
    path('concerts/', views.concerts, name='concerts'),  # Concerts list
    path('accounts/', include('django.contrib.auth.urls')),  # Built-in Django authentication
    path('auth/', include('user_authentication.urls')),  # Custom authentication system
]

