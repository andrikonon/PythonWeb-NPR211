from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from posts.models import Post


def posts_list(request) -> HttpResponse:
    posts = Post.objects.all().order_by('-date')
    return render(request, 'posts/posts_list.html', { 'posts': posts })

def posts_read(request, slug) -> HttpResponse:
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'posts/posts_read.html', { 'post': post })