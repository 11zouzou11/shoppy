from re import template
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path

from cart.views import add_to_cart, cart, checkout, hx_menu_cart, update_cart, hx_cart_total, success
from order.views import start_order
from main.views import mainpage, shop, signup, account, edit_account
from product.views import product

urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('account/', account, name='account'),
    path('account/edit/', edit_account, name='edit_account'),
    path('shop/', shop, name='shop'),
    path('shop/<slug:slug>', product, name='product'),
    path('cart/', cart, name='cart'),
    path('success/', success, name="success"),
    path('cart/checkout/', checkout, name='checkout'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('hx_menu_cart/', hx_menu_cart, name="hx_menu_cart"),
    path('update_cart/<int:product_id>/<str:action>/', update_cart, name='update_cart'),
    path('hx_cart_total/', hx_cart_total, name='hx_cart_total'),
    path('start_order/', start_order, name='start_order'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
