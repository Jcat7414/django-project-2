from django.urls import path, include
from . import views
from .views import CreateAccountView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('user-profile/', views.ProfileView.as_view(), name='userProfile'),
    path('upload', views.ImageView.as_view(), name='userImage'),
]