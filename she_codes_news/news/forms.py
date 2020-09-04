from django import forms
from django.forms import ModelForm
from .models import NewsStory, Category
from users.models import CustomUser

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)


class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'content', 'category', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'pub_date': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-input', 'placeholder':'Select a date', 'type':'date'}),
            'content': forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'Write the story here'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-input'}),
        }

class SelectAuthorForm(forms.Form):
    class Meta:
        author = forms.ModelChoiceField(queryset=CustomUser.objects.all())

