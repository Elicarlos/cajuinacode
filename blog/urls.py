
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('contato/', views.contato, name='contato'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('<slug:slug>/', views.post_detail, name='post_detail')
]