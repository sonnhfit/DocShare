"""mydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from myapp.views import HomeView, LionDocList, DetailDocument, SearchLionDocList
from users.views import SignInView, SignUpView
from blog.views import BlogView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', HomeView.as_view(), name='home'),
    path('docs/<category>/', LionDocList.as_view(), name='doc_cate'),
    path('detail/<slug>/', DetailDocument.as_view(), name='detail_doc'),
    #Sign up
    path('sign-in/', SignInView.as_view(), name='sign_in'),
    path('sign-up/', SignUpView.as_view(), name='sign_up'),
    #search
    path('search/', SearchLionDocList.as_view(), name='search'),
    #cart
    path('cart/', include('cart.urls')),
    path('blog/', BlogView.as_view(), name='blog')
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
