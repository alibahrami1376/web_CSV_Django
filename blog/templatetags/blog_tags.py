from django import template
from blog.models import Post,Category
register = template.Library()


@register.inclusion_tag('blog/latest_posts.html')
def pupolarposts(arg=3):
    posts = Post.objects.filter(status=1).order_by("published_date")[:arg]
    return {'posts':posts}

@register.inclusion_tag('blog/blog_category_sidebar.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {'categories':cat_dict}

@register.filter
def safe_quill_html(quill_field):
    """Safely get HTML from QuillField, returns empty string if invalid"""
    if not quill_field:
        return ""
    try:
        return quill_field.html
    except Exception:
        return ""
    
    