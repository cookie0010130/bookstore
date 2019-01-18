from django.urls import path
from main import views


app_name = 'main'
urlpatterns = [
    path('', views.main, name='main'),
    path('login/', views.login, name='login'),
    path('about/', views.about, name='about'),
    path('登入/', views.登入, name='登入'),
    path('關於bookstore/', views.關於bookstore, name='關於bookstore'),
    path('隱私政策/', views.隱私政策, name='隱私政策'),
    path('新品推薦/', views.新品推薦, name='新品推薦'),
    path('暢銷書榜/', views.暢銷書榜, name='暢銷書榜'),
    path('今日66折/', views.今日66折, name='今日66折'),
    path('經典文學/', views.經典文學, name='經典文學'),
    path('心理勵志/', views.心理勵志, name='心理勵志'),
    path('推理文學/', views.推理文學, name='推理文學'),
    path('科幻小說/', views.科幻小說, name='科幻小說'),
    path('傲慢與偏見/', views.傲慢與偏見, name='傲慢與偏見'),
    path('被討厭的勇氣/', views.被討厭的勇氣, name='被討厭的勇氣'),
    path('福爾摩斯/', views.福爾摩斯, name='福爾摩斯'),
    path('harrypotter/', views.harrypotter, name='harrypotter'),
]