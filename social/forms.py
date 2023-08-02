from django import forms
from .models import Post

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
        fields = ['body']