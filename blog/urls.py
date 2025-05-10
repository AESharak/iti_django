from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('author/<int:pk>/', views.author_detail, name='author_detail'),
    path('<slug:slug>/delete/', views.delete_post, name='delete_post'),
    path('author/<int:pk>/delete/', views.delete_author, name='delete_author'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
]