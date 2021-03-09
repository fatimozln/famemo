from django.shortcuts import render, HttpResponse
from . import models
# Create your views here.


def articles_list(request):
    articles = models.Article.objects.all().order_by('date')
    return render(request, 'articles/articles_list.html', {'articles': articles})


def articles_details(request, slug):
    return HttpResponse(slug)
