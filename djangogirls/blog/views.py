
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post
import logging

logger = logging.getLogger(__name__)


def post_list(request):
    logger.info(f"request: {request}")
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    logger.info(f"posts: {posts}")
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    logger.info(f"request: {request}")
    post = get_object_or_404(Post, pk=pk)
    logger.info(f"post: {post}")
    return render(request, 'blog/post_detail.html', {'post': post})

