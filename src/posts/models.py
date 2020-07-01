from django.db import models
from ckeditor.fields import RichTextField
from users.models import User
# Create your models here.


class BaiViet(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    keyword = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    content = RichTextField()

