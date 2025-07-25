# proyectoapp/blog/urls.py
from django.urls import path
from . import views

app_name = 'blog' # Define un namespace para las URLs de esta app

urlpatterns = [
    # Rutas generales
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # Rutas para el modelo Article (CRUD)
    path('articles/', views.ArticleListView.as_view(), name='article_list'),
    path('articles/new/', views.ArticleCreateView.as_view(), name='article_create'),
    path('articles/<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('articles/<int:pk>/edit/', views.ArticleUpdateView.as_view(), name='article_update'),
    path('articles/<int:pk>/delete/', views.ArticleDeleteView.as_view(), name='article_delete'),

    # Ruta para la vista con decorador
    path('metal-zone/', views.my_restricted_metal_zone, name='restricted_zone'),
]
