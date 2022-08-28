from django.contrib import admin
from django.urls import path

from main.views import mainpage, shop
from product.views import product

urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('shop/', shop, name='shop'),
    path('product/', product, name='product'),


    path('admin/', admin.site.urls),
]
