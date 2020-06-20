from django.views.generic import TemplateView, ListView
from .tasks import show_hello_world
# from .models import DemoModelư
from documents.models import DocumentCategory, SubCategory, Document, Tag
from django.views import View
from django.shortcuts import render, get_object_or_404
from cart.cart import Cart
# Create your views here.


class HomeView(TemplateView):
    
    template_name = 'index.html'

    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorys'] = DocumentCategory.objects.all()
        list_sub_cate = SubCategory.objects.all()
        context['sub_cate'] = list_sub_cate
        list_dict = []
        for item in list_sub_cate:
            sid = {}
            sid['docl'] = Document.objects.filter(cate=item)
            sid['su_cate'] = item
            list_dict.append(sid)
        
        context['list_im'] = list_dict

        return context


class LionDocList(ListView):

    context_object_name = 'doc_list'
    template_name = 'list_doc.html'

    def get_queryset(self):
        self.category = get_object_or_404(SubCategory, slug=self.kwargs['category'])
        # DocumentCategory

        return Document.objects.filter(cate=self.category)
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['category'] = self.category
        print(   context['category'])
        return context


class SearchLionDocList(View):
    def post(self, request):
        doc = request.POST.get('search')
        try:
            status = Document.objects.filter(title__icontains=doc)
        except Document.DoesNotExist:
            status = None
        return render(request, 'search.html', {"doc": status})


class DetailDocument(View):

    def get(self, request, slug):
        doc = Document.objects.get(slug=slug)
        tags = Tag.objects.all()
        cate = SubCategory.objects.all()
        cart = Cart(request)
        context = {
            "doc": doc,
            "cart": cart,
            "tags": tags,
            "cate": cate,
        }
        return render(request, 'single-blog.html', context)



