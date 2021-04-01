# Contains functions for calling processing code in views.py
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

from .forms import ImagesForm, TextForm
from .models import Images, Text

import matplotlib.pyplot as plt

def redirect_text_process(request, fn_code = 0):
    '''Idea: pass a function code (int) to fn_code, call the function based off its code'''
    #print(fn_code)
    if request.method == "POST":
        content = {}
        content['code'] = True
        content['fn_code'] = str(fn_code)
    # Does nothing with content for now
    #return render(request, 'preprocessing/process_text.html', content)
    return redirect('process_text')

def redirect_img_process(request, fn_code):

    return render(request, 'preprocessing/process_image.html')

