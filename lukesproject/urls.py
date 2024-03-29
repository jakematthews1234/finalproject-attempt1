"""lukesproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts.views import index
from cart.views import view_cart
from checkout.views import checkout
import blog.views


#  all main url's used on the website, linked to their respective url folders
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('products/', include('products.urls')),
    url('accounts/', include('accounts.urls')),
    url(r'^$', index, name='index'),
    url(r'blog/', include('blog.urls')),
    url(r'cart/', include('cart.urls')),
    url(r'checkout/', include('checkout.urls')),
    # url(r'testimonials/', include('testimonials.urls')),

]


