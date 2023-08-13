from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, Max
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib.auth import logout
from django.contrib import messages
from django.views import View
from django.core.paginator import Paginator
from .models import Post, Comment, UserProfile
from .forms import PostForm, CommentForm, UserProfileForm
from django.views.generic.edit import UpdateView, DeleteView


class PostListView(LoginRequiredMixin, View):
    """
    PostListView:
    - Displays a list of posts from users that the current user follows.
    - Allows the current user to create a new post.
    """

    def get_newsfeed_posts(self, user):
        followed_profiles = UserProfile.objects.filter(followers__in=[user])
        followed_users = [profile.user for profile in followed_profiles]

        # Include posts from the user as well
        followed_users.append(user)

        # Get latest posts from followed users and the user themselves
        posts = Post.objects.filter(author__in=followed_users).order_by('-created_on')

        return posts

    def get(self, request, *args, **kwargs):
        posts = self.get_newsfeed_posts(request.user)
        paginator = Paginator(posts, 3)  # 3 posts per page

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        form = PostForm()
        context = {
            'page_obj': page_obj,
            'form': form,
        }
        return render(request, 'post_list.html', context)

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            messages.success(
                request,
                'Your post has been created! 🎉'
            )
            return redirect('post-list')

        posts = self.get_newsfeed_posts(request.user)
        paginator = Paginator(posts, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'page_obj': page_obj,
            'form': form,
        }
        return render(request, 'post_list.html', context)


class PostDetailView(LoginRequiredMixin, View):
    """
    PostDetailView:
    - Displays the details of a specific post.
    - Allows users to view comments and add new ones to the post.
    """
    def get(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm()
        comments = Comment.objects.filter(post=post, parent=None).order_by('-created_on')
        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'post_detail.html', context)
    
    def post(self, request, pk, *args, **kwargs):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()
            messages.success(request, 'Your comment has been added!')

        comments = Comment.objects.filter(post=post, parent=None)\
                          .order_by('-created_on')
        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'post_detail.html', context)


class CommentReplyView(LoginRequiredMixin, View):
    """
    CommentReplyView:
    - Allows users to reply to specific comments on a post.
    - Associates the new comment with the parent comment, post, and the user.
    """
    def post(self, request, post_pk, pk, *args, **kwargs):
        post = Post.objects.get(pk=post_pk)
        parent_comment = Comment.objects.get(pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.parent = parent_comment
            new_comment.save()

        return redirect('post-detail', pk=post.pk)


class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    PostEditView:
    - Allows post authors to edit their own posts.
    - Uses the UpdateView to provide form handling for editing the post's body.
    - Tests if the user trying to edit the post is indeed its author.
    """
    model = Post
    fields = ['body']
    template_name = 'post_edit.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('post-detail', kwargs={'pk': pk})

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    def form_valid(self, form):
        messages.success(self.request, 'Your post has been updated!')
        return super().form_valid(form)

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    PostDeleteView:
    - Allows post authors to delete their own posts.
    - Uses the DeleteView for deleting posts and redirects
    - to the post list after deletion.
    - Tests if the user trying to delete the post is indeed its author.
    """
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post-list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Your post has been deleted.')
        return super().delete(request, *args, **kwargs)


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    CommentDeleteView:
    - Allows comment authors to delete their own comments.
    - Uses the DeleteView for deleting comments and redirects
    - to the post detail after deletion.
    - Tests if the user trying to delete the comment is indeed its author.
    """
    model = Comment
    template_name = 'comment_delete.html'

    def get_success_url(self):
        pk = self.kwargs['post_pk']
        return reverse_lazy('post-detail', kwargs={'pk': pk})

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, 'Comment deleted successfully.')
        return super().delete(request, *args, **kwargs)


class ProfileView(View):
    """
    ProfileView:
    - Displays details of a specific user's profile.
    - Shows the user's posts, followers, and checks
    - if the current user is following the profile.
    - Calculates and displays the age of the user if the
    - date of birth is provided.
    """
    def get(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(user=pk)
        user = profile.user
        posts = Post.objects.filter(author=user).order_by('-created_on')
        followers = profile.followers.all()

        if len(followers) == 0:
            is_following = False

        for follower in followers:
            if follower == request.user:
               is_following = True
               break
            else:
                is_following = False

        number_of_followers = len(followers)

        if profile.date_of_birth:
            age = date.today().year - profile.date_of_birth.year - ((date.today().month, date.today().day) < (profile.date_of_birth.month, profile.date_of_birth.day))
        else:
            age = None

        context = {
            'user': user,
            'profile': profile,
            'posts': posts,
            'number_of_followers': number_of_followers,
            'is_following': is_following,
            'age': age,
        }

        return render(request, 'profile.html', context)


class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    ProfileEditView:
    - Allows users to edit their own profiles.
    - Uses the UpdateView to provide form handling for editing the profile.
    - Tests if the user trying to edit the profile is indeed its owner.
    """
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'profile_edit.html'

    def get_success_url(self):
        pk= self.kwargs['pk']
        return reverse_lazy('profile', kwargs={'pk': pk})

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user
    
    def form_valid(self, form):
        messages.success(self.request, 'Your profile has been updated!')
        return super().form_valid(form)


class ProfileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    ProfileDeleteView:
    - Allows users to delete their own profiles.
    - Upon profile deletion, logs out the user and deletes the user account.
    - Uses the DeleteView for deleting profiles.
    """
    model = UserProfile
    template_name = 'profile_delete.html'
    success_url = reverse_lazy('index')

    def test_func(self):
        profile = self.get_object()
        return self.request.user == profile.user

    def delete(self, request, *args, **kwargs):
        user = self.request.user
        response = super().delete(request, *args, **kwargs)
        logout(request)
        user.delete()
        messages.success(request, 'Your profile has been deleted!')
        return response


class AddFollower(LoginRequiredMixin, View):
    """
    AddFollower:
    - Allows users to follow another user's profile.
    """
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        profile.followers.add(request.user)

        return redirect('profile', pk=profile.pk)

class RemoveFollower(LoginRequiredMixin, View):
    """
    RemoveFollower:
    - Allows users to unfollow a profile they are currently following.
    """
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        profile.followers.remove(request.user)

        return redirect('profile', pk=profile.pk)


class AddLike(LoginRequiredMixin, View):
    """
    AddLike:
    - Allows users to like or unlike a post.
    - Toggles the like status and returns the current number of
    - likes and the like status.
    """
    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        user = request.user
        liked = False
        
        if user in post.likes.all():
            post.likes.remove(user)
        else:
            post.likes.add(user)
            liked = True

        return JsonResponse({
            'likes_count': post.likes.count(),
            'liked': liked
        })

class AddCommentLike(LoginRequiredMixin, View):
    """
    AddCommentLike:
    - Allows users to like or unlike a comment.
    - Toggles the like status and returns the current number of
    - likes and the like status.
    """
    def post(self, request, comment_pk, *args, **kwargs):
        comment = Comment.objects.get(pk=comment_pk)
        user = request.user
        liked = False
        
        if user in comment.likes.all():
            comment.likes.remove(user)
        else:
            comment.likes.add(user)
            liked = True

        return JsonResponse({
            'likes_count': comment.likes.count(),
            'liked': liked
        })


class UserSearch(View):
    """
    UserSearch:
    - Enables users to search for other users based on their username.
    - Returns a list of profiles that match the search query.
    """
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        profile_list = UserProfile.objects.filter(
            Q(user__username__icontains=query)
        )

        context = {
            'profile_list': profile_list,
        }
        return render(request, 'search.html', context)