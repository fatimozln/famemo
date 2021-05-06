from django.db import models
from accounts.models import MyUser
# Create your models here.


STATUS_CHOICES = [
    ('active', 'active'),
    ('deactive', 'deactive'),
]


class Profile(models.Model):
    name = models.CharField(max_length=50)
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255)
    image = models.ImageField(
        default='default_profile.jpg', upload_to='%Y/%m/%d')
    status = models.CharField(choices=STATUS_CHOICES,
                              default='active', max_length=10)

    def __str__(self):
        return str(self.name)
