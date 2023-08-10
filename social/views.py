from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q, Max
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib import messages
from django.views import View
from .models import Post, Comment, UserProfile
from .forms import PostForm, CommentForm, UserProfileForm
from django.views.generic.edit import UpdateView, DeleteView


class PostListView(LoginRequiredMixin, View):

    def get_followed_users_posts(self, user):
        followed_profiles = UserProfile.objects.filter(followers__in=[user])
        followed_users = [profile.user for profile in followed_profiles]

        # get the latest post from each followed user
        posts = []
        for user in followed_users:
            latest_post = Post.objects.filter(author=user).order_by('-created_on').first()
            if latest_post is not None:
                posts.append(latest_post)

        # sort the posts by creation time
        posts.sort(key=lambda post: post.created_on, reverse=True)
        return posts

    def get(self, request, *args, **kwargs):
        posts = self.get_followed_users_posts(request.user)
        form = PostForm()
        context = {
            'post_list': posts,
            'form': form,
        }
        return render(request, 'post_list.html', context)

    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            messages.success(request, 'Your post has been created! See it in your Profile 🎉')
            return redirect('post-list')

        posts = self.get_followed_users_posts(request.user)
        context = {
            'post_list': posts,
            'form': form,
        }
        return render(request, 'post_list.html', context)


class PostDetailView(LoginRequiredMixin, View):
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

        comments = Comment.objects.filter(post=post, parent=None).order_by('-created_on')
        context = {
            'post': post,
            'form': form,
            'comments': comments,
        }

        return render(request, 'post_detail.html', context)


class CommentReplyView(LoginRequiredMixin, View):
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


class AddFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        profile.followers.add(request.user)

        return redirect('profile', pk=profile.pk)

class RemoveFollower(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        profile = UserProfile.objects.get(pk=pk)
        profile.followers.remove(request.user)

        return redirect('profile', pk=profile.pk)


class AddLike(LoginRequiredMixin, View):
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
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        profile_list = UserProfile.objects.filter(
            Q(user__username__icontains=query)
        )

        context = {
            'profile_list': profile_list,
        }
        return render(request, 'search.html', context)