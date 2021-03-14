from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

from .forms import ImagesForm
from .models import Images

def index(request):
  return render(request, 'preprocessing/index.html')

def about(request):
  return render(request, 'preprocessing/about.html')

def image(request):

  # Allows us to send data back to the page
  context = {}

  # Image loading code:
  if request.method == "POST":
    form = ImagesForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      
  else: # If not a post request, instantiate empty form
    form = ImagesForm()

  #  uploaded_file = request.FILES['img_data']
  #  fs = FileSystemStorage()
  #  name = fs.save(uploaded_file.name, uploaded_file)
  #  context['url'] = fs.url(name)

  imgs = Images.objects.all()
  context['images'] = imgs

  # Get form
  context['form'] = form

  return render(request, 'preprocessing/image.html', context)

def delete_image(request, pk):
  if request.method == 'POST':
    img = Images.objects.get(pk=pk)
    img.delete()
  return redirect('preprocessing-image')

def text(request):
  return render(request, 'preprocessing/text.html')