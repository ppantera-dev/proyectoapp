# proyectoapp/blog/urls.py
# (Este es el archivo urls.py de tu aplicación 'blog')

from django.urls import path
from . import views # Importa las vistas de tu app blog

urlpatterns = [
    path('', views.vista_inicio_blog, name='blog_de_inicio'),
    # Puedes añadir más rutas aquí para tu blog, por ejemplo:
    path('post/<int:pk>/', views.detalle_post, name='detalle_post'),
    path('acerca-de/', views.acerca_acerca, name='acerca'), # Corrección: usa un nombre de vista claro
]
