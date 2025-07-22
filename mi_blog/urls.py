# proyectoapp/mi_blog/urls.py
"""
URL configuration for mi_blog project.

The `urlpatterns` list routes URLs to views.
"""
from django.contrib import admin
from django.urls import path, include # <--- Asegúrate de importar 'include' aquí

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')), # <--- ¡Esta es la línea que debes agregar!
]
