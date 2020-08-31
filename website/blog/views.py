from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Blogger, Post
from .forms import PostForm, UserForm, BloggerForm
from .decorators import unauthenticated_user
# from .filters import BloggerFilter


def homePage(request):
    context = { }
    return render(request, 'blog/home.html', context)


@login_required(login_url='/login/')
def bloggerPage(request):
    blogger = request.user.blogger
    posts = blogger.post_set.all()[:5]

    context = {
        'blogger': blogger,
        'posts': posts,
    }
    return render(request, 'blog/blogger.html', context)


@login_required(login_url='/login/')
def postPage(request, post_id):
    post = request.user.blogger.post_set.get(id=post_id)

    context = {
        'post': post,
    }
    return render(request, 'blog/post.html', context)


@login_required(login_url='/login/')
def createPost(request):
    blogger = request.user.blogger

    if request.method == "POST":
        form = PostForm(request.POST, initial={'author': blogger})
        if form.is_valid():
            form.save()
            return redirect(f"/blogger")

    context = {
        'form': form,
    }
    return render(request, 'blog/create_post.html', context)


@login_required(login_url='/login/')
def updatePage(request, post_id):
    post = request.user.blogger.post_set.get(id=post_id)

    form = PostForm(instance=post)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(f"/blogger")

    context = {
        'form': form,
    }
    return render(request, 'blog/update.html', context)


@login_required(login_url='/login/')
def deletePage(request, post_id):
    post = request.user.blogger.post_set.get(id=post_id)

    if request.method == "POST":
        post.delete()
        return redirect(f"/blogger")

    context = {
        'post': post,
    }
    return render(request, 'blog/delete.html', context)

@unauthenticated_user
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


def userPage(request):
    context = {
        "user": request.user,
    }
    return render(request, 'blog/user.html', context)


@login_required(login_url='/login/')
def createBlogPage(request):

    data = {
        'user': request.user,
        'email': request.user.email,
    }

    bloggerForm = BloggerForm(initial=data)

    if request.method == "POST":
        bloggerForm = BloggerForm(request.POST, request.FILES)
        if bloggerForm.is_valid():
            bloggerForm.save()
            return redirect("home")

    context = {
        "bloggerForm": bloggerForm,
    }

    return render(request, "blog/create_blog.html", context)


def aboutPage(request):
    context = {

    }
    return render(request, "blog/about.html", context)


""" Perform a search based on a given Blogger's name """
def searchResultsPage(request):
    bloggerName = request.GET.get("search_blogger")
    bloggers = Blogger.objects.all().filter(name__icontains=bloggerName)

    context = {
            "bloggers": bloggers,
        }
    return render(request, "blog/search_results.html", context)

