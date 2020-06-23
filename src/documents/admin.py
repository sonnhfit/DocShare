from django.contrib import admin
from .models import DocumentCategory, SubCategory, Tag, Document
# Register your models here.

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title','number_of_view','number_of_download' ,'price')


admin.site.register(DocumentCategory)
admin.site.register(SubCategory)
admin.site.register(Tag)
admin.site.register(Document, DocumentAdmin)
