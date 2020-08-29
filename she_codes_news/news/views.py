from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import NewsStory
from .forms import StoryForm
from .forms import SelectAuthorForm
from users.models import CustomUser
from django.http import HttpResponseNotFound



class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.order_by('-pub_date').all()[:3]
        context['all_stories'] = NewsStory.objects.order_by('-pub_date').all()
        context['author_choices'] = CustomUser.objects.all()
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

class StoryByView(generic.ListView, generic.edit.FormMixin):
    model = NewsStory
    template_name = 'news/storyby.html'
    context_object_name = 'story'
    form_class = SelectAuthorForm

    def get_queryset(self):
        '''Return that authors news stories.'''
        return NewsStory.objects.filter(author=self.kwargs['author_username'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_stories'] = NewsStory.objects.filter(author=self.kwargs['author_username']).order_by('-pub_date')
        context['form'] = SelectAuthorForm
        try:
            context['author_username'] = CustomUser.objects.get(pk=self.kwargs['author_username']).full_name
        except CustomUser.DoesNotExist:
            return None
        return context

    def select_author(request):
        #the job of this function is to process the form when POSTed
        if request.method == "POST":
            form = SelectAuthorForm(request.POST)

            if form.is_valid():
                return redirect("{% url news:authorStory author_username=form.cleaned_data['author'] %}")
