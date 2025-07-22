# proyectoapp/mi_blog/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings # ¡IMPORTAR ESTA LÍNEA!
from django.conf.urls.static import static # ¡IMPORTAR ESTA OTRA LÍNEA!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')), # Esta línea ya la tienes
    path('ckeditor/', include('ckeditor_uploader.urls')), # ¡AGREGAR ESTA LÍNEA!
    path('', include('blog.urls')), # ¡AGREGAR ESTA LÍNEA! Esto hará que la URL "/" sea manejada por blog.urls
    # Las URLs para las apps 'accounts' y 'messages_app' las agregaremos más adelante cuando las creemos.
    # path('accounts/', include('accounts.urls')),
    # path('messages/', include('messages_app.urls')),
]

# ¡AGREGAR ESTE BLOQUE COMPLETO AL FINAL DEL ARCHIVO!
# Configuración para servir archivos de MEDIA en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
