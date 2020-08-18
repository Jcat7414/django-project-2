from django.db import models


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    content = models.TextField()
    image = models.ImageField(upload_to='images')
# the above image option requires Pillow Library
    # caption = models.CharField(max_length=50)
