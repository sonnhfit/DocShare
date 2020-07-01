from django.shortcuts import render
from django.views import View
from posts.models import BaiViet
# Create your views here.


class BaiVietDetail(View):
    def get(self,request, slugg):
        s = BaiViet.objects.get(slug=slugg)
        return render(request,'postcontent.html',{'s': s})


class ListBaiViet(View):
    def get(self,request):
        lp = BaiViet.objects.all()
        context = {
            'bv' : lp
        }
        return render(request,'blog.html',context)
