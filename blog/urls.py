from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView
)

my_base_url = 'post'

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path(f'{my_base_url}/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path(f'{my_base_url}/new/', BlogCreateView.as_view(), name='post_new'),
    path(f'{my_base_url}/<int:pk>/edit', BlogUpdateView.as_view(), name='post_edit'),
    path(f'{my_base_url}/<int:pk>/delete', BlogDeleteView.as_view(), name='post_delete'),
]