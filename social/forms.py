from django import forms
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
        }