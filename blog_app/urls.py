from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('post/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('post/new/', views.blog_create, name='blog_create'),
    path('post/<int:pk>/edit/', views.blog_edit, name='blog_edit'),
    path('post/<int:pk>/delete/', views.blog_delete, name='blog_delete'),
    path('post/<int:pk>/rate/', views.rate_post, name='rate_post'),
    path('contact/', views.contact, name='contact'),
    path('profile/', views.profile, name='profile'),
] 