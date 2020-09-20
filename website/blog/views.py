from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Blogger
from .forms import PostForm, UserForm, BloggerForm, CommentForm
from .decorators import unauthenticated_user


def homePage(request):
    """
    Home Page view
    """
    bloggers = Blogger.objects.all().order_by("-date_created")[:3]
    context = {
        "bloggers": bloggers,
    }
    return render(request, 'blog/home.html', context)


@login_required(login_url='/login/')
def bloggerPage(request):
    """
    Blogger Page view. Get logged Blogger and retrieve Posts
    """
    blogger = request.user.blogger
    posts = blogger.post_set.all()
    paginator = Paginator(posts, 6)  # Show 6 posts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'blogger': blogger,
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, 'blog/blogger.html', context)


@login_required(login_url='/login/')
def postPage(request, post_id):
    """
    Post Page view. Get certain Post object.
    """
    post = request.user.blogger.post_set.get(id=post_id)
    comments = post.comment_set.all()
    context = {
        'post': post,
        'comments': comments,
    }
    return render(request, 'blog/post.html', context)


@login_required(login_url='/login/')
def createPost(request):
    """
    Create Post object. Author field is already filled in a form.
    """
    blogger = request.user.blogger
    form = PostForm(initial={'author': blogger})
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(f"/blogger")

    context = {
        'form': form,
    }
    return render(request, 'blog/create_post.html', context)


@login_required(login_url='/login/')
def updatePage(request, post_id):
    """
    Update Post object.
    """
    post = request.user.blogger.post_set.get(id=post_id)
    form = PostForm(instance=post)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect(f"/blogger/post/{post_id}")

    context = {
        'form': form,
    }
    return render(request, 'blog/update_post.html', context)


@login_required(login_url='/login/')
def deletePage(request, post_id):
    """
    Delete Post object
    """
    post = request.user.blogger.post_set.get(id=post_id)

    if request.method == "POST":
        post.delete()
        return redirect(f"/blogger")

    context = {
        'post': post,
    }
    return render(request, 'blog/delete_post.html', context)

@unauthenticated_user
def registerPage(request):
    """
    Register User view. Uses UserForm
    """
    form = UserForm()

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, "Account created for " + username)
            return redirect('login')

    context = {
        'form': form,
    }
    # template stored in website/templates/registration directory
    return render(request, 'registration/register.html', context)


@login_required(login_url='/login/')
def userPage(request):
    """
    View displays User information
    """
    context = {
        "user": request.user,
    }
    return render(request, 'blog/user.html', context)


@login_required(login_url='/login/')
def createBlogPage(request):
    """
    Create Blog view. Uses BloggerForm
    """
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
    """
    About Page view.
    """
    context = {

    }
    return render(request, "blog/about.html", context)


def searchResultsPage(request):
    """
    Perform a Blogger search based on a given name
    """
    bloggerName = request.GET.get("search_blogger")
    bloggers = Blogger.objects.all().filter(name__icontains=bloggerName)

    context = {
            "bloggers": bloggers,
        }
    return render(request, "blog/search_results.html", context)


def bloggerVisitPage(request, pk):
    """
    Blogger Visit view. User cannot edit an object as a visitor.
    """
    blogger = Blogger.objects.get(id=pk)
    posts = blogger.post_set.all()
    paginator = Paginator(posts, 6)  # Show 6 posts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "blogger": blogger,
        "posts": posts,
        "page_obj": page_obj,
    }
    return render(request, "blog/blogger_visit.html", context)


def postVisitPage(request, pk, post_id):
    """
    Post Visit view. User cannot edit an object as a visitor.
    """
    post = Blogger.objects.get(id=pk).post_set.get(id=post_id)
    comments = post.comment_set.all().order_by("-date_created")

    data = {
        "user": request.user,
        "post": post,
    }

    form = CommentForm(initial=data)

    if request.method == "POST":
        form = CommentForm(request.POST, initial=data)
        if form.is_valid():
            form.save()
            return redirect(f"/blogger/{pk}/post/{post_id}")

    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blog/post_visit.html", context)
