from django.shortcuts import render
from django.views import View
from Posts.models import baiviet
# Create your views here.


class ViewBaiSlug(View):
    def get(self,request, slugg):
        s = baiviet.objects.get(slug=slugg)
        return render(request,'post2.html',{'s': s})


class ListBaiViet(View):
    def get(self,request):
        lp = baiviet.objects.all()
        context = {
            'bv' : lp
        }
        return render(request,'blog.html',context)
