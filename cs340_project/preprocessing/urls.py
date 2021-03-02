from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='preprocessing_home'),
    path('about/', views.about, name='preprocessing_about'),
]