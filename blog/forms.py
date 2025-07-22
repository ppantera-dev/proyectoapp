# proyectoapp/blog/forms.py
from django import forms
from .models import Article
from ckeditor.widgets import CKEditorWidget

class ArticleForm(forms.ModelForm):
    # Asegúrate de que el widget de CKEditor se aplique al campo de contenido
    content = forms.CharField(widget=CKEditorWidget(), label="Contenido del Artículo")

    class Meta:
        model = Article
        fields = ['title', 'subtitle', 'content', 'image', 'band_name', 'genre', 'release_year']
        # Los campos 'author' y 'published_date' se asignan automáticamente en la vista o el modelo.
