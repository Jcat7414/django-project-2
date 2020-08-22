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
    image = models.ImageField(upload_to='static/news/images', default="placeholder-1.jpg")
    @property
    def better_date(self):
        if self.pub_date:
            return self.pub_date.strftime("%d %b %Y")
        else:
            return "no_date"

# class Image(models.Model):
#     title = models.CharField(max_length=50)
#     image = models.ImageField(upload_to='images')

