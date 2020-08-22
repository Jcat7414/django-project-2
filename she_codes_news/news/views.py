from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import NewsStory
from .forms import StoryForm
# from .forms import ImageForm


class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        # this line does not impact the display order
        return NewsStory.objects.order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.order_by('-pub_date').all()[:4]
        context['all_stories'] = NewsStory.objects.order_by('-pub_date').all()
        return context

# class ImageView(generic.CreateView):
#     template_name = 'news/createStory.html'

#     def image_upload_view(request):
#         """Process images uploaded by users"""
#         if request.method == 'POST':
#             form = ImageForm(request.POST, request.FILES)
#             if form.is_valid():
#                 form.save()
#                 # Get the current instance object to display in the template
#                 img_obj = form.instance
#                 return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
#         else:
#             form = ImageForm()
#         return render(request, 'index.html', {'form': form})

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

