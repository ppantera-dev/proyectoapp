# proyectoapp/blog/views.py
from django.shortcuts import render, get_object_or_404, redirect # Agregado get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView # Nuevas importaciones
from django.urls import reverse_lazy # Nueva importación
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # Nuevas importaciones
from django.contrib.auth.decorators import login_required # Nueva importación
from django.contrib import messages # Nueva importación

from .models import Article
from .forms import ArticleForm # Nueva importación

# --- Vistas Generales ---

def home(request):
    """Vista de inicio/home. Muestra los 5 artículos más recientes."""
    recent_articles = Article.objects.all().order_by('-published_date')[:5]
    return render(request, 'blog/home.html', {'recent_articles': recent_articles})

def about(request):
    """Vista 'Acerca de mí'."""
    return render(request, 'blog/about.html')

# --- Vistas de Artículos (CRUD) ---

class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html' # El template que crearemos para listar
    context_object_name = 'articles' # Nombre de la variable en el template
    ordering = ['-published_date'] # Ordena por fecha de publicación descendente
    paginate_by = 6 # Muestra 6 artículos por página

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q') # Obtiene el parámetro de búsqueda 'q'
        if query:
            queryset = queryset.filter(
                models.Q(title__icontains=query) |
                models.Q(content__icontains=query) |
                models.Q(author__username__icontains=query) |
                models.Q(band_name__icontains=query) |
                models.Q(genre__icontains=query)
            ).distinct() # Usa Q objects para búsquedas OR
        return queryset

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html' # El template para el detalle del artículo
    context_object_name = 'article'

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/article_form.html' # Usaremos el mismo template para crear y actualizar
    success_url = reverse_lazy('blog:article_list') # Redirige después de crear

    def form_valid(self, form):
        form.instance.author = self.request.user # Asigna el autor actual al artículo
        messages.success(self.request, '¡Artículo creado exitosamente!')
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/article_form.html'
    success_url = reverse_lazy('blog:article_list')

    def test_func(self): # Solo el autor o un superusuario puede editar
        article = self.get_object()
        return self.request.user == article.author or self.request.user.is_superuser

    def form_valid(self, form):
        messages.success(self.request, '¡Artículo actualizado exitosamente!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_update'] = True # Para diferenciar en el template si es creación o actualización
        return context

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'blog/article_confirm_delete.html' # Un template para confirmar la eliminación
    success_url = reverse_lazy('blog:article_list') # Redirige después de eliminar

    def test_func(self): # Solo el autor o un superusuario puede eliminar
        article = self.get_object()
        return self.request.user == article.author or self.request.user.is_superuser

    def form_valid(self, form):
        messages.success(self.request, 'Artículo eliminado exitosamente.')
        return super().form_valid(form)

# --- Vista de Zona Restringida (con decorador) ---
@login_required # Requiere que el usuario esté logueado
def my_restricted_metal_zone(request):
    """Vista de ejemplo para una zona solo para usuarios logueados."""
    return render(request, 'blog/restricted_zone.html')
