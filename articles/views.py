from django.shortcuts import render, HttpResponse, redirect
from . import models
from django.contrib.auth.decorators import login_required
from . import forms
from django.contrib.auth.models import AnonymousUser, AbstractBaseUser


def articles_list(request):
    articles = models.Article.objects.all().order_by('-date')
    return render(request, 'articles/home.html', {'articles': articles})


def articles_details(request, slug):
    # return HttpResponse(slug)
    article = models.Article.objects.get(slug=slug)
    return render(request, 'articles/articles_detail.html', {'article': article})


@login_required(login_url='/accounts/login')
def add_post(request):
    if request.method == 'POST':
        form = forms.Addpost(request.POST, request.FILES)
        if form.is_valid():
            sample = form.save(commit=False)
            sample.author = request.user
            sample.save()
            return redirect('articles:list')
    else:
        form = forms.Addpost()
    return render(request, 'articles/add_post.html', {'form': form})


@login_required(login_url='/accounts/login')
def like(request, postid):
    post = models.Article.objects.get(id=postid)
    user = request.user
    if user.is_authenticated:
        if user in post.likes.all():
            return HttpResponse("you liked this post")
        else:
            post.likes.add(user)
            return HttpResponse('you liked this post', postid)
    else:
        return HttpResponse("you are not allow to liked this post...plz login or signup")


""" def like(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_obj = models.Article.objects.get(id=post_id)

        if user in post_obj.likes.all():
            post_obj.likes.remove(user)
        else:
            post_obj.likes.add(user)

        like, created = models.Like.objects.get_or_create(
            user=user, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value == 'UnLike'
            else:
                like.value = 'Like'
        like.save()
        return redirect('articles:list') """


def unlike(request, postid):
    post = models.Article.objects.get(id=postid)
    user = request.user
    if user.is_authenticated:
        if user in post.likes.all():
            post.likes.remove(user)
            return redirect('articles:slug', postid)
        else:
            return HttpResponse("you dont liked this post")
    else:
        return HttpResponse("you are not allow to liked this post...plz login or signup")


@login_required(login_url='/accounts/login')
def add_comment(request, slug):
    post = models.Article.objects.get(slug=slug)
    user = request.user
    if request.method == 'POST':
        form = forms.Addcomments(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.name = request.user
            comment.save()
            return redirect('articles:slug', slug=post.slug)
    else:
        form = forms.Addcomments()
    return render(request, 'articles/add_comment.html', {'form': form})


@login_required(login_url='/accounts/login')
def delete_post(request, slug):
    post = models.Article.objects.get(slug=slug)
    user = request.user
    if post.author == request.user:
        post.delete()
    else:
        return HttpResponse("Only the author of this article is allowed to delete this post!!!")

    return redirect('articles:list')
