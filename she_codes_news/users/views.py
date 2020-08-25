from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
# from .forms import CustomUserChangeForm

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

# not sure this should be CreateView, perhaps ChangeView?
# class ChangeAccountView(CreateView):
#     form_class = CustomUserChangeForm
#     success_url = reverse_lazy('profile')
#     template_name = 'users.userProfile.html'
