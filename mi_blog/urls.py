# proyectoapp/mi_blog/urls.py (Archivo URL principal del proyecto)

"""
URL configuration for mi_blog project.

The `urlpatterns` list routes URLs to views.
"""
from django.contrib import admin
from django.urls import path, include # <--- Asegúrate de que 'include' esté aquí

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')), # <--- ¡SOLO ESTA LÍNEA DEBE IR AQUÍ PARA TU BLOG!
]
