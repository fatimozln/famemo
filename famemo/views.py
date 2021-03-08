from django.shortcuts import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse('Hi...Welcome To Famemo')
