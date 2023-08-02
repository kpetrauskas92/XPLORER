from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.files import File
from django.conf import settings
import os

class Post(models.Model):
    body = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, verbose_name='user', related_name='profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=20, blank=True, null=True)
    bio = models.TextField(max_length=200, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    picture = CloudinaryField('profile_image', blank=True)

    def save(self, *args, **kwargs):
        if self.picture == '':
            self.picture.save(
                'blank-profile-picture.png', 
                File(open(os.path.join(settings.MEDIA_ROOT, 'blank-profile-picture.png'), 'rb'))
            )
        super().save(*args, **kwargs)