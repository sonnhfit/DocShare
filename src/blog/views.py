from django.shortcuts import render
from django import views

# Create your views here.

class BlogView(views.View):
    def get(self, request):
        return render(request, 'blog.html')