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

    context_object_name = 'sub_category'
    template_name = 'list_doc.html'

    def get_queryset(self):
        self.category = get_object_or_404(DocumentCategory, slug=self.kwargs['category'])
        # DocumentCategory
        sub_list = SubCategory.objects.filter(parent_cate=self.category)
        self.doc = Document.objects.filter(cate__in=sub_list)
        return sub_list
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['doc_category'] = self.category
        context['docs'] = self.doc
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
        cate = SubCategory.objects.get(slug=slug)
        tags = Tag.objects.all()
        doc = Document.objects.filter(cate=cate)
        cart = Cart(request)
        context = {
            "docs": doc,
            "cart": cart,
            "tags": tags,
            "cate": cate,
        }
        return render(request, 'single-blog.html', context)



