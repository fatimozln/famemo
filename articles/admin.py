from django.contrib import admin
from . import models
from .models import Article

# Register your models here.


class Blogadmin(admin.ModelAdmin):
    fieldsets = [
        ('title',                {'fields': ['title']}),
        ('content information',                {'fields': ['body', 'author']}),
        ('image',                {'fields': ['image']}),
        ('like',                {'fields': ['likes']}),
    ]
    list_display = ['title', 'date']
    serch_fields = ['title', 'content']


admin.site.register(Article, Blogadmin)
