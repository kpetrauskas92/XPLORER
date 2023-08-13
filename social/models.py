import os
from datetime import date, timedelta
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from cloudinary.uploader import destroy
from django.core.files import File
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError


class Post(models.Model):
    """Represents a user's post with text content, an optional image,
    creation date, author, and likes from other users."""
    body = models.CharField(max_length=80)
    image = CloudinaryField('post_image', null=True, blank=True)
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='post_author')
    likes = models.ManyToManyField(User, blank=True, related_name='likes')

    def delete(self, *args, **kwargs):
        """Ensure image associated with post is deleted from Cloudinary."""
        if self.image:
            public_id = self.image.public_id
            destroy(public_id)
        super(Post, self).delete(*args, **kwargs)

    def __str__(self):
        return f"Post by {self.author.username} on {self.created_on.date()}"


class Comment(models.Model):
    """Represents a comment on a post. Each comment has text content,
    creation date, author, associated post, likes, and may be
    a reply to another comment."""
    comment = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    likes = models.ManyToManyField(
        User, blank=True, related_name='comment_likes'
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='+'
    )

    @property
    def children(self):
        """Returns all child comments for the current comment."""
        return (Comment.objects.filter(parent=self)
                .order_by('-created_on')
                .all())

    @property
    def is_parent(self):
        """Check if the current comment is a top-level comment."""
        return self.parent is None

    def __str__(self):
        return f"Comment by {self.author.username} on {self.created_on.date()}"


def validate_age(value):
    """Validate age based on provided date of birth."""
    today = date.today()
    age = (today.year - value.year -
           ((today.month, today.day) < (value.month, value.day)))
    if age < 16 or value > today:
        raise ValidationError('Users must be 16 years old or older.')


class UserProfile(models.Model):
    """Represents additional profile data for a user."""
    user = models.OneToOneField(
        User,
        primary_key=True,
        verbose_name='user',
        related_name='profile',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=10, blank=True, null=True)
    bio = models.TextField(max_length=40, blank=True, null=True)
    date_of_birth = models.DateField(
        null=True, blank=True, validators=[validate_age]
    )
    location = models.CharField(max_length=50, blank=True, null=True)
    picture = CloudinaryField('profile_image', default='user-default_zft92h')
    followers = models.ManyToManyField(
        User, blank=True, related_name='followers'
    )

    def __str__(self):
        return f"Profile of {self.user.username}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create a user profile when a new user is created."""
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Save the user profile whenever the user is saved."""
    instance.profile.save()
