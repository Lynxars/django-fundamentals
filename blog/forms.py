# blog/forms.py
from django import forms
from blog.models import Post

# Define a form linked directly to our Post model
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'category', 'author']