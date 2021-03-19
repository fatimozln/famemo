from django import forms
from .import models


class Addpost(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'slug', 'body', 'image']


class Addcomments(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['message']
