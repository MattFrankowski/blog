from django.shortcuts import render, redirect
from .models import Blogger, Post
from .forms import PostForm


def homePage(request):
    context = {

    }
    return render(request, 'blog/home.html', context)


def bloggerPage(request, pk):
    blogger = Blogger.objects.get(id=pk)
    posts = blogger.post_set.all()[:5]

    context = {
        'blogger': blogger,
        'posts': posts,
    }
    return render(request, 'blog/blogger.html', context)


def postPage(request, pk, post_id):
    post = Post.objects.get(id=post_id)

    context = {
        'post': post,
    }
    return render(request, 'blog/post.html', context)


def createPost(request, pk):
    blogger = Blogger.objects.get(id=pk)
    form = PostForm(initial={'author': blogger})

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f"/blogger/{pk}")

    context = {
        'form': form,
    }
    return render(request, 'blog/create_post.html', context)


def updatePage(request, pk, post_id):
    post = Post.objects.get(id=post_id)
    form = PostForm(instance=post)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(f"/blogger/{pk}")

    context = {
        'form': form,
    }
    return render(request, 'blog/create_post.html', context)


def deletePage(request, pk, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        post.delete()
        return redirect(f"/blogger/{pk}")

    context = {
        'post': post,
    }
    return render(request, 'blog/delete.html', context)

