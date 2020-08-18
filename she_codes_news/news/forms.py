from django import forms
from django.forms import ModelForm
from .models import NewsStory
from .models import Image

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'author', 'pub_date', 'content', 'category']
        widgets = {
            'pub_date': forms.DateInput(format=('%m/%d/%Y'), 
            attrs={'class':'form-control', 'placeholder':'Select a date', 
            'type':'date'}),
        }

class ImageForm(ModelForm):
    # form for the image model
    class Meta:
        model = Image
        fields = ['title', 'image']