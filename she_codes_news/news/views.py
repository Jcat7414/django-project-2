from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import NewsStory, Category
from .forms import StoryForm
from .forms import SelectAuthorForm
from users.models import CustomUser
from django.http import HttpResponseNotFound

class IndexView(generic.ListView):
    form_class = SelectAuthorForm
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.order_by('-pub_date').all()[:3]
        context['all_stories'] = NewsStory.objects.order_by('-pub_date').all()
        return context

class ImageView(generic.CreateView):
    template_name = 'news/createStory.html'

    def image_upload_view(request):
        """Process images uploaded by users"""
        if request.method == 'POST':
            form = StoryForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                # Get the current instance object to display in the template
                img_obj = story.image
                return render(request, 'story.html', {'form': form, 'img_obj': img_obj})
        else:
            form = StoryForm()
        return render(request, 'createStory.html', {'form': form})

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class EditStoryView(generic.UpdateView):
    model = NewsStory
    form_class = StoryForm
    template_name = 'news/editStory.html'
    success_url = reverse_lazy('news:index')

class DeleteStoryView(generic.DeleteView):
    model = NewsStory
    template_name = 'news/deleteStory.html'
    success_url = reverse_lazy('news:index')
    
def AuthorView(request, auth):
    # auth = request.user
    auth_story = NewsStory.objects.filter(author=auth)
    return render(request, 'news/storyby.html', {'auth':auth, 'auth_story':auth_story})

class AddCategoryView(generic.CreateView):
    model = Category
    template_name = 'news/addCategory.html'
    fields = '__all__'
    success_url = reverse_lazy('news:index')

def CategoryView(request, cats):
    category_story = NewsStory.objects.filter(category=cats)
    return render(request, 'news/category.html', {'cats': cats, 'category_story':category_story})