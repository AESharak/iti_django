from django.urls import path
from . import api_views

urlpatterns = [
    # Post API endpoints
    path('posts/', api_views.PostListCreate.as_view(), name='api-post-list'),
    path('posts/<int:pk>/', api_views.PostRetrieveUpdateDestroy.as_view(), name='api-post-detail'),
    
    # Author API endpoints
    path('authors/', api_views.AuthorListCreate.as_view(), name='api-author-list'),
    path('authors/<int:pk>/', api_views.AuthorRetrieveUpdateDestroy.as_view(), name='api-author-detail'),
] 