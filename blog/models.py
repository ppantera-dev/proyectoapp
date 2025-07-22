# proyectoapp/blog/models.py
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name="Título del Artículo")
    subtitle = models.CharField(max_length=255, blank=True, null=True, verbose_name="Subtítulo")
    content = RichTextField(verbose_name="Contenido")
    image = models.ImageField(upload_to='articles_images/', null=True, blank=True, verbose_name="Imagen Principal")
    published_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Publicación")

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles', verbose_name="Autor")

    band_name = models.CharField(max_length=100, blank=True, null=True, verbose_name="Nombre de la Banda")
    genre = models.CharField(max_length=50, blank=True, null=True, verbose_name="Género (Ej: Thrash Metal)")
    release_year = models.IntegerField(blank=True, null=True, verbose_name="Año de Lanzamiento (Si es un álbum)")

    class Meta:
        verbose_name = "Artículo de Metal"
        verbose_name_plural = "Artículos de Metal"
        ordering = ['-published_date']

    def __str__(self):
        return self.title
