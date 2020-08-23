from django.forms import ModelForm
from django import  forms
from .models import Post, Blogger


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'images', 'author']