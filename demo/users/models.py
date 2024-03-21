from django.contrib.auth.models import AbstractUser
from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class CustomUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pics', null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    is_author = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email