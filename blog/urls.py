from django.urls import path
from .views import postListView, postDetailView , postCreateView , postUpdateView
from . import views

urlpatterns = [
    path('', postListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', postDetailView.as_view(), name='post-detail'),
    path('post/new/', postCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', postUpdateView.as_view(), name='post-update'),
    path('about/' , views.about , name='blog-about')
]
