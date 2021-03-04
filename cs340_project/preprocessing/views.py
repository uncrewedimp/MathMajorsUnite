from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return render(request, 'preprocessing/index.html')

def about(request):
  return render(request, 'preprocessing/about.html')

def image(request):
  return render(request, 'preprocessing/image.html')

def text(request):
  return render(request, 'preprocessing/text.html')