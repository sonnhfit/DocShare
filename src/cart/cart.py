from decimal import Decimal
from django.conf import settings

from documents.models import Document


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_SLUG)
        if not cart:
            cart = self.session[settings.CART_SESSION_SLUG] = {}
        self.cart = cart

    def add(self, document, quantity=1, update_quantity=False):
        document_slug = str(document.slug)
        if document_slug not in self.cart:
            self.cart[document_slug] = {'quantity': 0, 'price': str(document.price)}
        if update_quantity:
            self.cart[document_slug]['quantity'] = quantity
        else:
            self.cart[document_slug]['quantity'] += quantity
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_SLUG] = self.cart
        self.session.modified = True

    def remove(self, document):
        document_slug = str(document.slug)
        if document_slug in self.cart:
            del self.cart[document_slug]
            self.save()

    def __iter__(self):
        document_slugs = self.cart.keys()
        documents = Document.objects.filter(slug__in=document_slugs)
        for document in documents:
            self.cart[str(document.slug)]['document'] = document

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def has_document(self, document):
        document_slug = str(document.slug)
        return document_slug in self.cart

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
    
    def get_total_price_text(self):
        sub_total = sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
        return f"{sub_total:,}"

    def clear(self):
        del self.session[settings.CART_SESSION_SLUG]
        self.session.modified = True
