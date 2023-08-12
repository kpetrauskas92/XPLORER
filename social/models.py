from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.files import File
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date, timedelta
from django.core.exceptions import ValidationError
import os


# Post: Represents a user's post with text content, an optional image,
# creation date, author, and likes from other users.
class Post(models.Model):
    body = models.TextField()
    image = CloudinaryField('post_image', null=True, blank=True)
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='post_author'
    )
    likes = models.ManyToManyField(User, blank=True, related_name='likes')


# Comment: Represents a comment on a post. Each comment has text content,
# creation date, author, associated post, likes,
# and may be a reply to another comment.
class Comment(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    likes = models.ManyToManyField(
        User, blank=True, related_name='comment_likes'
    )
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True,
        null=True, related_name='+'
    )

    @property
    def children(self):
        return Comment.objects.filter(parent=self).order_by('-created_on').all

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False


def validate_age(value):
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))

    if age < 16 or value > today:
        raise ValidationError('Users must be 16 years old or older.')


# UserProfile: Represents additional profile data for a user, including
# name, bio, date of birth, location, profile picture, and followers.
class UserProfile(models.Model):
    user = models.OneToOneField(
        User, primary_key=True, verbose_name='user',
        related_name='profile', on_delete=models.CASCADE
    )
    name = models.CharField(max_length=10, blank=True, null=True)
    bio = models.TextField(max_length=40, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True, validators=[validate_age])
    location = models.CharField(max_length=50, blank=True, null=True)
    picture = CloudinaryField(
        'profile_image', default='user-default_acghod'
    )
    followers = models.ManyToManyField(
        User, blank=True, related_name='followers'
    )


# Signals: Automatically manage the creation and saving of user profiles.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
