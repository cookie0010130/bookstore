from django.contrib import admin
from django.urls import path, include, re_path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls', namespace='main')),
    path('account/', include('account.urls', namespace='account')),
   path('order/', include('order.urls', namespace='order')),
    re_path('.*', views.main),
]