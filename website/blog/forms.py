from django.forms import ModelForm
from .models import Post, Blogger, PostImages



class PostForm(ModelForm):
    class Meta:
        model = Post

        fields = ['title', 'content', 'author']



class PostImagesForm(ModelForm):
    class Meta:
        model = PostImages
        fields = ["image"]
