from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='preprocessing_index'),
    path('about/', views.about, name='preprocessing_about')
]