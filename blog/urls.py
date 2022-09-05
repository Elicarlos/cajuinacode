from pkgutil import ImpImporter
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('contato/', views.contato, name='contato')
]