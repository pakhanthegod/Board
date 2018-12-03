from django.urls import path, include
from django.views.decorators.http import require_POST

from . import views

app_name = 'board'
urlpatterns = [
    path('', views.ThreadList.as_view(), name='thread_list'),
    path('<str:thread>/', include([
        path('', views.PostList.as_view(), name='thread_posts'),
        path('create_post/', views.PostCreateView.as_view(), name='post_create'),
        path('<int:pk>/', views.PostDetail.as_view(), name='post'),
        path('<int:pk>/create_comment/', require_POST(views.CommentCreateView.as_view()), name='comment_create'),
    ])),
]