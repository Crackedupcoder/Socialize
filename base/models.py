from django.db import models
from users.models import CustomUser
from django.utils import timezone


class Post(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='users_post')
    text = models.TextField(blank=True)
    image = models.ImageField(upload_to='images',blank=True)
    users_like = models.ManyToManyField(CustomUser,
                                        related_name='images_liked',
                                        blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.user.username


