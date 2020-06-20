from django.contrib import admin
from .models import DocumentCategory, SubCategory, Tag, Document
# Register your models here.

admin.site.register(DocumentCategory)
admin.site.register(SubCategory)
admin.site.register(Tag)
admin.site.register(Document)