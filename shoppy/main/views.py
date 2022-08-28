from django.shortcuts import render

from product.models import Product

def mainpage(request):
    products = Product.objects.all()[0:8]

    return render(request, 'main/mainpage.html', {'products': products})

def shop(request):
    products = Product.objects.all()[0:8]

    return render(request, 'main/shop.html', {'products': products})
