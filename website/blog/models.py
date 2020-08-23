from django.db import models


class Blogger(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    photo = models.ImageField(default="unnamed.png", blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=10000)
    author = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    # images = models.ImageField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PostImages(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="", blank=True, null=True)
