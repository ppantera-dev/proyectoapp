"""
URL configuration for mi_blog project.

The `urlpatterns` list routes URLs to views.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]
