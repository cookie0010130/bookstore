from django.urls import path
from main import views


app_name = 'main'
urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.login, name='login'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('aboutbookstore/', views.aboutbookstore, name='aboutbookstore'),
    path('personal/', views.personal, name='personal'),
    path('new/', views.new, name='new'),
    path('hot/', views.hot, name='hot'),
    path('34off/', views.saleoff, name='34off'),
    path('title1/', views.title1, name='title1'),
    path('title2/', views.title2, name='title2'),
    path('title3/', views.title3, name='title3'),
    path('title4/', views.title4, name='title4'),
    path('book1/', views.book1, name='book1'),
    path('book2/', views.book2, name='book2'),
    path('book3/', views.book3, name='book3'),
    path('book4/', views.book4, name='book4'),
]