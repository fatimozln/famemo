from django.shortcuts import render, HttpResponse, redirect
from . import models
from django.contrib.auth.decorators import login_required
from . import forms


def articles_list(request):
    articles = models.Article.objects.all().order_by('-date')
    return render(request, 'articles/articles_list.html', {'articles': articles})


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
