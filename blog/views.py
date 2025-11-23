from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpRequest
from django.utils import timezone
from blog.models import Post
from blog.forms import NewsletterForm
from datetime import timedelta
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage


def blog_home(request,**kwargs):
    posts = Post.objects.filter(status=True)
    if kwargs.get('cat_name') != None :
        posts = posts.filter(category__name = kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts= posts.filter(author__username=kwargs['author_username'])
       
    page_all  =  Paginator(posts,1)
    page = request.GET.get("page")
    try: 
        
        posts = page_all.page(page)
    except PageNotAnInteger:
        posts = page_all.page(1)
    except EmptyPage:
        posts = page_all.page(1)
        
    context = {'posts': posts,'page_range':page_all.page_range}
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

def blog_search(request:HttpRequest):
    posts = Post.objects.filter(status=True)
    
    if request.method == 'GET':
        posts = posts.filter(content__contains=request.GET.get('search'))
        
    context = {'posts': posts}
    return render(request, 'blog/blog_home.html', context)
    
def save_newsletter(request:HttpRequest):
    if request.method == "POST":
        print("salaa,m")
        form = NewsletterForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            print("save")
            return redirect('blog:blog_home')
    
    return redirect('blog:blog_home')    
            