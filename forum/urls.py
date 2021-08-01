from django.urls import path
from .views import (
    PostListView, 
    PostDetailView, 
    PostUpdateView, 
    PostCreateView,
    PostDeleteView
)
from . import views

urlpatterns = [
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='about-home'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('', PostListView.as_view(), name='forum-home'),
]