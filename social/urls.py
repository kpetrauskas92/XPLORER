from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostEditView,
    PostDeleteView,
    CommentDeleteView,
    CommentReplyView,
    ProfileView,
    ProfileEditView,
    AddFollower,
    RemoveFollower,
    AddLike,
    AddCommentLike,
    UserSearch
)

urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/edit/<int:pk>', PostEditView.as_view(), name='post-edit'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_pk>/comment/delete/<int:pk>/', CommentDeleteView.as_view(), name='comment-delete'),
    path('post/<int:post_pk>/comment/<int:pk>/reply/', CommentReplyView.as_view(), name='comment_reply'),
    path('post/<int:pk>/like', AddLike.as_view(), name='like'),
    path('post/<int:post_pk>/comment/<int:comment_pk>/like', AddCommentLike.as_view(), name='comment-like'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', ProfileEditView.as_view(), name='profile-edit'),
    path('profile/<int:pk>/followers/add', AddFollower.as_view(), name='add-follower'),
    path('profile/<int:pk>/followers/remove', RemoveFollower.as_view(), name='remove-follower'),
    path('search/', UserSearch.as_view(), name='profile-search'),
]