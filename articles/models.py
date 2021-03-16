from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='%Y/%m/%d', blank=True, null=True)
    author = models.ForeignKey(
        User, default=None, on_delete=models.CASCADE, related_name='author')
    likes = models.ManyToManyField(
        User, related_name='bloglikes', blank=True, default=None)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50]+'...'

    @property
    def number_likes(self):
        return self.likes.all().count()


LIKE_CHOICES = [
    ('Like', 'Like'),
    ('UnLike', 'UnLike'),
]


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Article, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,
                             default='Like', max_length=10)

    def __str__(self):
        return str(self.post)
