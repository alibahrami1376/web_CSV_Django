from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post
from datetime import timedelta


def blog_home(request):
    
    
    posts = Post.objects.filter(status=True)
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog_home.html', context)

def blog_detail(request, post_id):
    """نمایش جزئیات یک پست وبلاگ"""
    post = get_object_or_404(Post, id=post_id, status=True)
    
    # افزایش تعداد بازدید
    post.counted_view += 1
    post.save(update_fields=['counted_view'])
    
    # دریافت پست‌های مرتبط (آخرین پست‌ها)
    related_posts = Post.objects.filter(status=True).exclude(id=post.id).order_by('-published_date', '-creat_date')[:3]
    
    context = {
        'post': post,
        'related_posts': related_posts
    }
    return render(request, 'blog/blog_detail.html', context)

def blog_category(request,cat_name):
    posts= Post.objects.filter(status=1)
    posts= posts.filter(category__name=cat_name)
    context = {
        'posts': posts
    }
    return render(request,'blog/blog_home.html',context)