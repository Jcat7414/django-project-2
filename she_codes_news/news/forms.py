from django import forms
from django.forms import ModelForm
from .models import NewsStory
from users.models import CustomUser


class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'content', 'category', 'type', 'linkedin_url', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'pub_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-input', 'placeholder':'Select a date', 'type':'date'}),
            'content': forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'Write the story here'}),
            'category': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Type of Story'}),
            'type': forms.Select(attrs={'class': 'form-imput', 'default': 'Founder'}),
            'linkedin_url': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Paste your LinkedIn URL here'}),
        }

#Creating a form to change an existing article.
# story = NewsStory.objects.get(pk=1)
# form = StoryForm(instance=story)

class SelectAuthorForm(forms.Form):
    authors = forms.ModelChoiceField(queryset=CustomUser.objects.all())
