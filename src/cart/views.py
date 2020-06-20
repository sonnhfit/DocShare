from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST

from documents.models import Document, SubCategory
from .models import Enroll
from .cart import Cart


@require_POST
def cart_add(request, slug):
    cart = Cart(request)  # create a new cart object passing it the request object
    document = get_object_or_404(Document, slug=slug)
    cart.add(document=document, quantity=1, update_quantity=False)
    return redirect('cart:cart_detail')


def cart_remove(request, slug):
    cart = Cart(request)
    document = get_object_or_404(Document, slug=slug)
    cart.remove(document)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html',  {'cart': cart,})


# def cart_checkout(request):
#     carts = Cart(request)
#     price = 0
#     for cart in carts:
#         document = cart['document']
#         document = get_object_or_404(Document, slug=document.slug)
#         price += document.price
        
    
#         Enroll.objects.create(document=document, user_id=request.user.id)

    # url = test_get(str(price))
    # messages.success(request, 'Successfully checked out!')
    # carts.clear()

    # return redirect(url)
    #return redirect(reverse_lazy('cart:cart_detail'))

