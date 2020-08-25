from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # this is where I can put custom fields for a user - such as a profile image
    # the basics are included due to the 'AbstractUser' command
    pass

    def __str__(self):
        return self.username


