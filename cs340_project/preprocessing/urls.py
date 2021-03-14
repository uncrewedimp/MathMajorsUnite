from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='preprocessing-index'),
    path('about/', views.about, name='preprocessing-about'),
    path('image/', views.image, name='preprocessing-image'),
    path('image/<int:pk>/', views.delete_image, name='delete_image'),
    path('text/', views.text, name='preprocessing-text')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)