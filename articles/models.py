from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='%Y/%m/%d', blank=True, null=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='bloglikes', blank=True)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50]+'...'
