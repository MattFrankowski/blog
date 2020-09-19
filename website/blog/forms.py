from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper

from .models import Post, Blogger, Comment


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'author']


class UserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class BloggerForm(ModelForm):

    class Meta:
        model = Blogger
        fields = "__all__"


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = "__all__"

    # hide CommentForm labels
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False



