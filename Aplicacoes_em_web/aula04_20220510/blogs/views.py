from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):

    latest_post_list = Post.objects.all()

    context = {
        'latest_post_list':latest_post_list
    }

    return render(request, 'blogs/index_post.html', context = context)

def detail(request, blogs_id):

    blogs = get_object_or_404(Post, pk=blogs_id)

    context = {
        'blogs':blogs
    }

    return render(request, 'blogs/index_post.html',context=context)
