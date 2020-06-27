from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from users.models import User
# Create your models here.


class DocumentCategory(models.Model):
    cate_title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.cate_title)
        super(DocumentCategory, self).save(*args, **kwargs)    

    def __str__(self):
        return self.cate_title


class SubCategory(models.Model):
    sub_title = models.CharField(max_length=255, verbose_name = "Tiêu Đề Nhỏ")
    slug = models.SlugField(max_length=100, unique=True, verbose_name = "Hạng Mục")
    parent_cate = models.ForeignKey(DocumentCategory, on_delete=models.CASCADE, verbose_name = "Nhóm Tài Liệu")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.sub_title)
        super(SubCategory, self).save(*args, **kwargs)    

    def __str__(self):
        return self.sub_title

    class Meta:
        verbose_name_plural = 'Danh Mục Nhỏ'


class Tag(models.Model):
    word        = models.CharField(max_length=35, verbose_name = "Từ Khóa Thẻ")
    slug        = models.CharField(max_length=250, verbose_name = "Hạng Mục")
    created_at  = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.word)
        super(Tag, self).save(*args, **kwargs)    

    def __str__(self):
        return self.word

    class Meta:
        verbose_name_plural = 'Thẻ'


class Document(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200, unique=True, primary_key=True, auto_created=False)
    number_of_page = models.IntegerField(default=0)
    number_of_view = models.IntegerField(default=0)
    number_of_download = models.IntegerField(default=0)
    size_of_file = models.FloatField(default=0.0)
    doc_file = models.FileField(upload_to='doc/%Y/%m/%d/', null=True)
    description = RichTextUploadingField(default='', blank=True, null=True)
    tags = models.ManyToManyField(Tag)
    cate = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="demo_images")
    video_url = models.CharField(max_length=255)
    file_field = models.FileField(upload_to='documents/%Y/%m/%d/')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Document, self).save(*args, **kwargs)

    @property
    def get_text_price(self):
        return f"{self.price:,}"