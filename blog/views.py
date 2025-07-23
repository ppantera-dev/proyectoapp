# proyectoapp/blog/views.py
from django.shortcuts import render
# from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.contrib.auth.decorators import login_required
# from django.contrib import messages

from .models import Article # Necesitamos importar el modelo Article para 'home'
# from .forms import ArticleForm

# --- Vistas Generales ---

def home(request):
    """Vista de inicio/home. Muestra los 5 artículos más recientes."""
    recent_articles = Article.objects.all().order_by('-published_date')[:5]
    return render(request, 'blog/home.html', {'recent_articles': recent_articles})

def about(request):
    """Vista 'Acerca de mí'."""
    return render(request, 'blog/about.html')

# --- (Las vistas para los Articles y la Zona Restringida se agregarán más adelante) ---
