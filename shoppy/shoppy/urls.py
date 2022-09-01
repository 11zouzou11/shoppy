from django.contrib import admin
from django.urls import path

from cart.views import add_to_cart
from main.views import mainpage, shop
from product.views import product

urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>', product, name='product'),
    path('add_to_cart/int:product_id>/', add_to_cart, name='add_to_cart'),
    path('admin/', admin.site.urls),
]
