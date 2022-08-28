from django.contrib import admin
from django.urls import path

from main.views import mainpage

urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('admin/', admin.site.urls),
]
