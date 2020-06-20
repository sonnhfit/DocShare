from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    coin = models.IntegerField(default=0)
    facebook_id = models.CharField(max_length=150, blank=True, null=True, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    def __str__(self):
        return '{}-{}'.format(self.id, self.username)