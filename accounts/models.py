from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class MyUser(AbstractUser):
    STATUS_CHOICES = [
        ('active', 'active'),
        ('deactive', 'deactive'),
    ]
    status = models.CharField(choices=STATUS_CHOICES,
                              default='active', max_length=10)
