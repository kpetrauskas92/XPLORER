import json
from django import forms
from django.conf import settings
from .models import Post, Comment, UserProfile


# PostForm: A form for creating or editing posts
# with a body and optional image.
class PostForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        max_length=100,
        widget=forms.Textarea(attrs={
            'rows': '2',
            'placeholder': 'Post your adventure...'
        })
    )

    class Meta:
        model = Post
        fields = ['body', 'image']


# CommentForm: A form for creating or editing comments.
class CommentForm(forms.ModelForm):
    comment = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '2',
            'placeholder': 'Say something...'
        })
    )

    class Meta:
        model = Comment
        fields = ['comment']


# UserProfileForm: A form for creating or editing user profiles,
# including details like name, bio, DOB, location, and profile picture.
class UserProfileForm(forms.ModelForm):
    picture = forms.ImageField(label='Profile Photo')

    class Meta:
        model = UserProfile
        fields = ['name', 'bio', 'date_of_birth', 'location', 'picture']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'bio': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)

        # Load countries from JSON to populate the location field choices.
        with open(settings.BASE_DIR / "static/data/countries.json", "r") as f:
            countries = json.load(f)
            country_choices = [
                (country["name"], country["name"])
                for country in countries
            ]

        # Set choices for the location field.
        self.fields['location'].widget = forms.Select(choices=country_choices)
