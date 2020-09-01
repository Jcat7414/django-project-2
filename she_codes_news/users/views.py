from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import CustomUser
from .forms import CustomUserCreationForm
from .forms import CustomUserChangeForm

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

class ProfileView(generic.DetailView):
    model = CustomUser
    template_name = 'users/userProfile.html'
    context_object_name = 'profile'

    def get_object(self):
        return CustomUser.objects.all()

class ImageView(generic.CreateView):
    template_name = 'users/createAccount.html'

    def image_upload_view(request):
        """Process images uploaded by users"""
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                # Get the current instance object to display in the template
                img_obj = profile.image
                return render(request, 'userProfile.html', {'form': form, 'img_obj': img_obj})
        else:
            form = CustomUserCreationForm()
        return render(request, 'createAccount.html', {'form': form})

class ChangeAccountView(CreateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('userProfile')
    template_name = 'users/editProfile.html'
