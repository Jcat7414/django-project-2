from django import forms
from django.forms import ModelForm
from .models import NewsStory

# FAMILY_TYPE = [
#         ('FOUNDER', "Founder"), 
#         ('PARTNER', "Partner"), 
#         ('MENTOR', "Mentor"),
#         ('TEAM', "Flair Team"), 
#         ('ADVOCATE', "Advocate")
#     ]


class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'author', 'pub_date', 'content', 'category', 'linkedin_url', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'author': forms.TextInput(attrs={'class': 'form-input'}),
            'pub_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-input', 'placeholder':'Select a date', 'type':'date'}),
            'content': forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'Write the story here'}),
            'category': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Type of Story'}),
            # 'family_member_type': forms.Select(attrs={'class': 'form-imput', 'default': 'Founder'}),
            'linkedin_url': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Paste your LinkedIn URL here'}),
        }

#Creating a form to change an existing article.
story = NewsStory.objects.get(pk=1)
form = StoryForm(instance=story)