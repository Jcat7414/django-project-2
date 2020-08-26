from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from django.forms import ModelForm

FOUNDER = "Founder" 
PARTNER = "Partner"
MENTOR = "Mentor"
TEAM = "Team"
ADVOCATE = "Advocate"
FAMILY_TYPE = [
    (FOUNDER, "Founder"), 
    (PARTNER, "Partner"), 
    (MENTOR, "Mentor"),
    (TEAM, "Flair Team"), 
    (ADVOCATE, "Advocate")
]

class NewsStory(models.Model):
    # created_at = models.DateTimeField(auto_now_add=True, story_name="Created at")
    # updated_at = models.DateTimeField(auto_now=True, story_name="Updated at")
    title = models.CharField(max_length=100, verbose_name="story title")
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    pub_date = models.DateTimeField(verbose_name="date published")
    category = models.CharField(max_length=20, verbose_name="story category", default='Type of Story')
    type = models.CharField(max_length=20, verbose_name="family member type", choices=FAMILY_TYPE, default=FOUNDER)
    content = models.TextField(verbose_name="")
    linkedin_url = models.CharField(max_length=200, verbose_name="linkedIn profile URL", default="Paste your LinkedIn URL here", blank=True)
    image = models.ImageField(upload_to='story_image/', verbose_name="story photo", default="placeholder-1.jpg")
    @property
    def better_date(self):
        if self.pub_date:
            return self.pub_date.strftime("%d %b %Y")
        else:
            return "no_date"
    

