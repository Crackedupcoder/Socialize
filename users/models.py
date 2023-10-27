from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    name = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(upload_to='avatars', default='avatar.svg')
    bio = models.TextField(blank=True)
    location = models.CharField(blank=True, max_length=255)
    profession = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.username

