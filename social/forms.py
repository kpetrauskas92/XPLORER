import json
from django import forms
from django.conf import settings
from .models import Post, Comment, UserProfile

class PostForm(forms.ModelForm):
    body = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows': '2',
            'placeholder': 'Post your adventure...'
        })
    )

    
    class Meta:
        model = Post
        fields = ['body', 'image']

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


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'bio', 'date_of_birth', 'location', 'picture']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'bio': forms.Textarea(attrs={'rows': 4, 'cols': 15}),
        }

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        
        # Load countries from JSON
        with open(settings.BASE_DIR / "static/data/countries.json", "r") as file:
            countries = json.load(file)
            country_choices = [(country["name"], country["name"]) for country in countries]

        # Set choices for the location field
        self.fields['location'].widget = forms.Select(choices=country_choices)