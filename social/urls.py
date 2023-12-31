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
    ProfileDeleteView,
    AddFollower,
    RemoveFollower,
    AddLike,
    AddCommentLike,
    UserSearch,
)

urlpatterns = [
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/edit/<int:pk>', PostEditView.as_view(), name='post-edit'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='post-delete'),
    path(
        'post/<int:post_pk>/comment/delete/<int:pk>/',
        CommentDeleteView.as_view(),
        name='comment-delete'
    ),
    path(
        'post/<int:post_pk>/comment/<int:pk>/reply/',
        CommentReplyView.as_view(),
        name='comment_reply'
    ),
    path('likepost/<int:pk>/', AddLike.as_view(), name='like'),
    path(
        'likecomment/<int:comment_pk>/',
        AddCommentLike.as_view(),
        name='comment-like'
    ),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path(
        'profile/edit/<int:pk>/',
        ProfileEditView.as_view(),
        name='profile-edit'
    ),
    path(
        'profile/<int:pk>/delete/',
        ProfileDeleteView.as_view(),
        name='delete-profile'
    ),
    path(
        'profile/<int:pk>/followers/add',
        AddFollower.as_view(),
        name='add-follower'
    ),
    path(
        'profile/<int:pk>/followers/remove',
        RemoveFollower.as_view(),
        name='remove-follower'
    ),
    path('search/', UserSearch.as_view(), name='profile-search'),
    path('', PostListView.as_view(), name='post-list'),
]
