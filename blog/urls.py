from django.urls import path
from . import views
from .feeds import LatestPostsFeed

app_name = 'blog'



urlpatterns = [
    path('<int:post_id>/', views.single_view, name='single'),
    path('search/', views.search_view, name = 'search'),
    path('category/<int:category_id>/', views.category_view, name='category'),
    path('tag/<int:tag_id>/', views.tag_view, name='tag'),
    path('author/<int:author_id>/', views.author_view, name='author'),

    path('rss/', LatestPostsFeed(), name='post_feed'),


]