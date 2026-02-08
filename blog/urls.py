from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('<int:post_id>/', views.single_view, name='single'),
]