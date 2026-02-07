from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts_view, name = 'allPosts'),
    path('<int:pk>/', views.single_view, name = "single")
]