from django.urls import path
from .views import CreateAccountView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    # path('user-profile/', ChangeAccountView.as_view(), name='userProfile'),
]