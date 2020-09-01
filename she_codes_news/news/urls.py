from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('story/<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('upload', views.ImageView.as_view(), name='image'),
    path('author/<int:author_username>/', views.StoryByView.as_view(), name='authorStory'),
    path('edit-story/<int:pk>/', views.EditStoryView.as_view(), name='editStory'),
    path('delete-story/<int:pk>/', views.DeleteStoryView.as_view(), name='deleteStory'),
]
