from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255)
    image = models.ImageField(
        default='default_profile.jpg', upload_to='%Y/%m/%d')

    def __str__(self):
        return str(self.name)
