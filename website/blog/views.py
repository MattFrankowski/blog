from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.contrib import messages

from .models import Blogger, Post, PostImages
from .forms import PostForm, PostImagesForm


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

    postForm = PostForm(initial={'author': blogger})

    if request.method == "POST":
        postForm = PostForm(request.POST)
        if postForm.is_valid():
            postForm.save()
            return redirect(f"/blogger/{pk}")

    ImageFormSet = modelformset_factory(PostImages, form=PostImagesForm, extra=3)

    formset = ImageFormSet(queryset=PostImages.objects.none())
    postForm = PostForm(initial={'author': blogger})

    if request.method == "POST":
        postForm = PostForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES, queryset=PostImages.objects.none())
        if postForm.is_valid() and formset.is_valid():
            postForm.save()
            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    photo = PostImages(post=postForm, image=image)
                    photo.save()
                messages.success(request, "Photos added")
                return redirect(f"/blogger/{pk}")
            else:
                print(postForm.errors, formset.errors)
        else:
            postForm = PostForm()
            formset = ImageFormSet(queryset=PostImages.objects.none())

    context = {
        'postForm': postForm,
        'formset': formset,
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

