from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import PostForm
from .models import Post
import logging

logger = logging.getLogger(__name__)


def post_list(request):
    logger.debug(f"request: {request}")
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    logger.debug(f"posts: {posts}")
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    logger.debug(f"request: {request}")
    post = get_object_or_404(Post, pk=pk)
    logger.debug(f"post: {post}")
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    logger.debug(f"request: {request}")
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    logger.debug(f"request:{request}, pk:{pk}")
    post = get_object_or_404(Post, pk=pk)
    logger.debug(f"post: {post}")
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})

