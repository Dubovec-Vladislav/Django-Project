from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='blog_home'),
    path('category/<str:slug>/', PostsByCategory.as_view(), name='category'),
    path('tag/<str:slug>/', PostsByTag.as_view(), name='tag'),
    path('post/<str:slug>/', GetPost.as_view(), name='post'),
    path('search/', Search.as_view(), name='search'),

    path('like/<str:slug>/', LikeView, name='like_news'),
    path('remove-like/<str:slug>/', RemoveLikeView, name='remove_like_news'),

    path('post/<int:pk>/add-comment/', CreateComment.as_view(), name='add_comment'),
    path('comment-like/<str:slug>/', CommentLikeView, name='like_comments'),

    path('post/<int:pk>/add-reply-comment/', CreateReplyComment.as_view(), name='add_reply_comment'),
    path('reply-comment-like/<str:slug>/', ReplyCommentLikeView, name='like_reply_comments'),
]
