from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog/detail/', views.blog_detail, name='blog_detail'),
    path('reservation/', views.reservation, name='reservation'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('reservation/success/', views.reservation_success, name='reservation_success'),
]