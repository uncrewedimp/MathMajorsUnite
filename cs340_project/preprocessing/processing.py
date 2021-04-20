# Contains functions for calling processing code in views.py
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

from .forms import ImagesForm, TextForm
from .models import Images, Text

import pandas as pd
import matplotlib.pyplot as plt

def merge(request):

    if request.method == 'POST':
        merge_fname = request.POST.getlist('merge_fname')
        pk_to_merge = request.POST.getlist('merge_files', default = ['BUG'])

        pk_to_merge = [int(pk) for pk in pk_to_merge]

        print('Printing to Test until merge functions implemented')
        print(merge_fname)
        print(pk_to_merge)

        # Collect the files
        df_list = []
        for pk in pk_to_merge:
           # Retrieves the requested file:
            f = Text.objects.get(pk=pk)

            #Computes report for dataframe:
            df = pd.read_csv(f.filename())
            df_list.append(df)

        # Merge files on backend:
        #merge(df_list, merge_fname)

        # Register saved with a model instance

    return redirect('process_text')

def rename(request):

    if request.method == 'POST':
        new_name = request.POST.getlist('new_name')

    # Actually renaming the columns

    return redirect('edit_file')

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

