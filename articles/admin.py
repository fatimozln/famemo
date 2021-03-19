from django.contrib import admin
from . import models
from .models import Article, Like, Comment


# Register your models here.


class Blogadmin(admin.ModelAdmin):
    fieldsets = [
        ('title',                {'fields': ['title']}),
        ('content information',                {'fields': ['body', 'author']}),
        ('slug',                {'fields': ['slug']}),
        ('image',                {'fields': ['image']}),
        ('like',                {'fields': ['likes']}),


    ]
    list_display = ['title', 'date']
    serch_fields = ['title', 'content']


admin.site.register(Article, Blogadmin)
admin.site.register(Like)
admin.site.register(Comment)
