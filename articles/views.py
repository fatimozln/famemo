from django.shortcuts import render, HttpResponse
from . import models
# Create your views here.


def articles_list(request):
    articles = models.Article.objects.all().order_by('-date')
    return render(request, 'articles/articles_list.html', {'articles': articles})


def articles_details(request, slug):
    # return HttpResponse(slug)
    article = models.Article.objects.get(slug=slug)
    return render(request, 'articles/articles_detail.html', {'article': article})


def add_post(request):
    return render(request, 'articles/add_post.html')
