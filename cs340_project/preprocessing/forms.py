from django import forms
from .models import Images, Text

class ImagesForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ('title', 'img_zip')

class TextForm(forms.ModelForm):
    class Meta:
        model = Text
        fields = ('title', 'txt')

