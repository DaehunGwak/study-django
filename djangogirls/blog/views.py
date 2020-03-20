
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


def post_list(request):
    logger.info(f"request: {request}")
    return render(request, 'blog/post_list.html', {})
