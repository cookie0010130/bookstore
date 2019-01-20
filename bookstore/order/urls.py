from django.urls import path
from order import views


app_name = 'order'
urlpatterns = [
    path('order/', views.order, name='order'),
    path('order/check/', views.ordercheck, name='ordercheck'),
]