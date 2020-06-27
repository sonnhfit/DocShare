from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class baiviet(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = RichTextField()