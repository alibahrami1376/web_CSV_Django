import logging
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpRequest
from django.utils import timezone
from django.db.models import Q
from blog.models import Post
from blog.forms import NewsletterForm
from datetime import timedelta
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage

logger = logging.getLogger(__name__)


def blog_home(request,**kwargs):
    logger.info(f'Blog home accessed with kwargs: {kwargs}')
    try:
        posts = Post.objects.filter(status=True)
        logger.info(f'Found {posts.count()} published posts')
        
        if kwargs.get('cat_name') != None :
            logger.info(f'Filtering by category: {kwargs["cat_name"]}')
            posts = posts.filter(category__name = kwargs['cat_name'])
            logger.info(f'Posts after category filter: {posts.count()}')
            
        if kwargs.get('author_username') != None:
            logger.info(f'Filtering by author: {kwargs["author_username"]}')
            posts= posts.filter(author__username=kwargs['author_username'])
            logger.info(f'Posts after author filter: {posts.count()}')
           
        page_all  =  Paginator(posts, 6)
        page = request.GET.get("page")
        try: 
            posts = page_all.page(page)
            logger.info(f'Rendering page {page}')
        except PageNotAnInteger:
            logger.info('Invalid page number, using page 1')
            posts = page_all.page(1)
        except EmptyPage:
            logger.info('Empty page requested, using page 1')
            posts = page_all.page(1)
            
        context = {'posts': posts,'page_range':page_all.page_range}
        logger.info('Blog home rendered successfully!')
        logger.info('Everything is OK!')
        return render(request, 'blog/blog_home.html', context)
    except Exception as e:
        logger.error(f'Error in blog_home view: {e}')
        raise

def blog_detail(request, post_id):
    """نمایش جزئیات یک پست وبلاگ"""
    logger.info(f'Blog detail accessed for post_id: {post_id}')
    try:
        post = get_object_or_404(Post, id=post_id, status=True)
        logger.info(f'Post found: {post.title}')
        
        # افزایش تعداد بازدید
        post.counted_view += 1
        post.save(update_fields=['counted_view'])
        logger.info(f'View count updated for post {post_id}: {post.counted_view}')
        
        # دریافت پست‌های مرتبط (آخرین پست‌ها)
        related_posts = Post.objects.filter(status=True).exclude(id=post.id).order_by('-published_date', '-creat_date')[:3]
        logger.info(f'Found {related_posts.count()} related posts')
        
        context = {
            'post': post,
            'related_posts': related_posts
        }
        logger.info('Blog detail rendered successfully!')
        logger.info('Everything is OK!')
        return render(request, 'blog/blog_detail.html', context)
    except Exception as e:
        logger.error(f'Error in blog_detail view: {e}')
        raise

def blog_search(request:HttpRequest):
    logger.info('Blog search accessed')
    try:
        posts = Post.objects.filter(status=True)
        
        if request.method == 'GET':
            search_query = request.GET.get('search', '').strip()
            if search_query:
                logger.info(f'Searching for: {search_query}')
                posts = posts.filter(
                    Q(title__icontains=search_query) | 
                    Q(content__icontains=search_query)
                )
                logger.info(f'Found {posts.count()} posts matching search query')
            else:
                logger.info('No search query provided')
        
        context = {'posts': posts}
        logger.info('Blog search rendered successfully!')
        logger.info('Everything is OK!')
        return render(request, 'blog/blog_home.html', context)
    except Exception as e:
        logger.error(f'Error in blog_search view: {e}')
        raise
    
def save_newsletter(request:HttpRequest):
    logger.info('save_newsletter view called')
    if request.method == "POST":
        logger.info('Processing newsletter form POST request')
        form = NewsletterForm(request.POST)
        if form.is_valid():
            try:
                newsletter = form.save()
                logger.info(f'Newsletter subscription saved: {newsletter.email}')
                logger.info('Everything is OK!')
                return redirect('blog:blog_home')
            except Exception as e:
                logger.error(f'Error saving newsletter subscription: {e}')
        else:
            logger.warning(f'Newsletter form validation failed: {form.errors}')
    
    return redirect('blog:blog_home')    
            