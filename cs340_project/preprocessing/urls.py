from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='preprocessing-index'),
    path('about/', views.about, name='preprocessing-about')
]