# proyectoapp/blog/admin.py
from django.contrib import admin
from .models import Article # Importa tu modelo Article

# Opcional: Personaliza cómo se muestra tu modelo en el admin
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'genre', 'release_year')
    list_filter = ('published_date', 'genre', 'author')
    search_fields = ('title', 'content', 'band_name')
    date_hierarchy = 'published_date' # Permite navegar por fecha

# Registra tu modelo con tu configuración personalizada (si la tienes)
admin.site.register(Article, ArticleAdmin)

# Si no quieres personalización, solo:
# admin.site.register(Article)
