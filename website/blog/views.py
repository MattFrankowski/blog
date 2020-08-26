from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Blogger, Post
from .forms import PostForm, UserForm


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


@login_required(login_url='/login/')
def postPage(request, pk, post_id):
    post = Post.objects.get(id=post_id)

    context = {
        'post': post,
    }
    return render(request, 'blog/post.html', context)


@login_required(login_url='/login/')
def createPost(request, pk):
    blogger = Blogger.objects.get(id=pk)
    form = PostForm(initial={'author': blogger})

    if request.method == "POST":
        form = PostForm(request.POST, initial={'author': blogger})
        if form.is_valid():
            form.save()
            return redirect(f"/blogger/{pk}")

    context = {
        'form': form,
    }
    return render(request, 'blog/create_post.html', context)


@login_required(login_url='/login/')
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
    return render(request, 'blog/update.html', context)


@login_required(login_url='/login/')
def deletePage(request, pk, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == "POST":
        post.delete()
        return redirect(f"/blogger/{pk}")

    context = {
        'post': post,
    }
    return render(request, 'blog/delete.html', context)


def registerPage(request):
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(request, "Account created for " + user)
            return redirect('login')

    context = {
        'form': form,
    }
    # template stored in website/templates/registration directory
    return render(request, 'registration/register.html', context)


def userPage(request, pk):
    user = User.objects.get(id=pk)
    context = {
        "user": user,
    }
    return render(request, 'blog/user.html', context)


def createBlogPage(request, pk):
    user = User.objects.get(id=pk)
    context = {
        "user": user,
    }
    return render(request, 'blog/create_blog.html', context)


def aboutPage(request):
    context = {

    }
    return render(request, "blog/about.html", context)


