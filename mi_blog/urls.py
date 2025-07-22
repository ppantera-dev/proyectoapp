# proyectoapp/blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_blog, name='home_blog'),
    # Puedes añadir más rutas aquí para tu blog, por ejemplo:
    # path('post/<int:pk>/', views.detalle_post, name='detalle_post'),
    # path('acerca-de/', views.about, name='about'),
]
