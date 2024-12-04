from django.urls import path
from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.home, name='home'),
    path('members/', views.band_members, name='band_members'),
    path('concerts/', views.concerts, name='concerts'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('auth/', include('user_authentication.urls')),
    
]
