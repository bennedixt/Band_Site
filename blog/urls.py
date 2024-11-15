from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('tour/', views.tour, name='tour'),
    path('grammys/', views.grammys, name='grammys'),
]
# blog/urls.py
from django.urls import path
from . import views


