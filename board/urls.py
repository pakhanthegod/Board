from django.urls import path

from . import views

app_name = 'board'
urlpatterns = [
    path('', views.index, name='index'),
    path('posts/<int:post_id>/', views.detail, name='detail'),
    path('posts/new/', views.post_new, name='post_new'),
]