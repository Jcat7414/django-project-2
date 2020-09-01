from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import NewsStory
from .forms import StoryForm
from .forms import SelectAuthorForm
from users.models import CustomUser
from django.http import HttpResponseNotFound

# class FormListView(generic.edit.FormMixin, generic.ListView):
#     def get(self, request, *args, **kwargs):
#         # From ProcessFormMixin
#         form_class = self.get_form_class()
#         self.form = self.get_form(form_class)

#         # From BaseListView??
#         self.object_list = self.get_queryset()
#         allow_empty = self.get_allow_empty()
#         if not allow_empty and len(self.object_list) == 0:
#             raise Http404(_(u"Empty list and '%(class_name)s.allow_empty' is False.") % {'class_name': self.__class__.__name__})

#         context = self.get_context_data(object_list=self.object_list, form=self.form)
#         return self.render_to_response(context)

#     def post(self, request, *args, **kwargs):
#         return self.get(request, *args, **kwargs)

class IndexView(generic.ListView):
    form_class = SelectAuthorForm
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SelectAuthorForm()
        context['latest_stories'] = NewsStory.objects.order_by('-pub_date').all()[:3]
        context['all_stories'] = NewsStory.objects.order_by('-pub_date').all()
        return context

    def select_author(request):
        #the job of this function is to process the form when POSTed
        if request.method == "POST":
            form = SelectAuthorForm(request.POST)
            if form.is_valid():

                return redirect("{% url 'news:authorStory' author_username=form.cleaned_data['author'] %}")

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

class StoryByView(generic.ListView):
    model = NewsStory
    template_name = 'news/storyby.html'
    context_object_name = 'storyby'

    def get_queryset(self):
        '''Return that author's news stories.'''
        return NewsStory.objects.filter(author=self.kwargs['author_username'])

class EditStoryView(generic.UpdateView):
    model = NewsStory
    form_class = StoryForm
    template_name = 'news/editStory.html'
    success_url = reverse_lazy('news:index')

class DeleteStoryView(generic.DeleteView):
    model = NewsStory
    template_name = 'news/deleteStory.html'
    success_url = reverse_lazy('news:index')
    
# class AuthorView(generic.ListView):
#     model = NewsStory
#     template_name = 'news.index.html'
#     fields = ['author']
#     success_url = reverse_lazy('news:authorStory user.pk')