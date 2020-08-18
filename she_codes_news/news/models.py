from django.db import models
from django.utils import timezone

class NewsStory(models.Model):
    # created_at = models.DateTimeField(auto_now_add=True, story_name="Created at")
    # updated_at = models.DateTimeField(auto_now=True, story_name="Updated at")
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    category = models.CharField(max_length=50)
    content = models.TextField()


class Image(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')

