from django.contrib.auth.models import AbstractUser
from django.db import models
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


class CustomUser(AbstractUser):
    # this is where I can put custom fields for a user - such as a profile image
    # the basics are included due to the 'AbstractUser' command
    first_name = models.CharField(max_length=30, verbose_name="first name")
    last_name = models.CharField(max_length=150, verbose_name="last name")
    business_name = models.CharField(max_length=100, verbose_name="business name", blank=True)
    type = models.CharField(max_length=20, verbose_name="family member type", choices=FAMILY_TYPE, default=FOUNDER)
    bio = models.TextField(verbose_name="tell us about yourself", blank=True)
    linkedin_url = models.CharField(max_length=200, verbose_name="linkedIn profile URL", default="Paste your LinkedIn URL here", blank=True)
    profile_photo = models.ImageField(upload_to='profile_photo/', verbose_name="profile photo", default="placeholder-1.jpg")

    @property
    def full_name(self):
        # "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)

    # def __str__(self):
    #         return self.username


  


