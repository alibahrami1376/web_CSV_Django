# مستندات کامل App: BLOG

## 📁 ساختار App
```
blog/
├── __init__.py
├── models.py            # مدل‌های Post, Category, Newsletter
├── views.py             # View functions
├── urls.py              # URL routing
├── forms.py             # فرم Newsletter
├── admin.py             # تنظیمات Django Admin
├── templatetags/        # Custom template tags
│   └── blog_tags.py
└── migrations/          # فایل‌های migration
```

---

## 📄 فایل: models.py

### خط 1-3: Import ها
```python
from django.db import models
from django.contrib.auth.models import User
```

**توضیح:**
- `models`: برای تعریف مدل‌های دیتابیس
- `User`: مدل کاربر Django

---

### خط 4-8: مدل Category
```python
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
```

**توضیح خط به خط:**

**خط 4:** `class Category(models.Model):`
- تعریف مدل Category برای دسته‌بندی پست‌ها

**خط 5:** `name = models.CharField(max_length=255)`
- فیلد نام دسته‌بندی
- حداکثر 255 کاراکتر

**خط 7-8:** `def __str__(self): return self.name`
- نمایش نام دسته‌بندی در admin و shell

---

### خط 10-27: مدل Post
```python
class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    image = models.ImageField(upload_to='blog/',default='blog/default.png')
    title = models.CharField(max_length=255)
    content = models.TextField(null=True)
    url = models.URLField(max_length=500, null=True, blank=True)   
    category =models.ManyToManyField(Category)
    counted_view = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    creat_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-creat_date']
        
    def __str__(self):
        return f"{self.title}"
```

**توضیح خط به خط:**

**خط 11:** `author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)`
- رابطه چند به یک با User
- `on_delete=models.SET_NULL`: اگر User حذف شود، author = NULL می‌شود
- `null=True`: می‌تواند NULL باشد

**خط 12:** `image = models.ImageField(upload_to='blog/',default='blog/default.png')`
- فیلد تصویر پست
- `upload_to='blog/'`: ذخیره در media/blog/
- `default='blog/default.png'`: تصویر پیش‌فرض

**خط 13:** `title = models.CharField(max_length=255)`
- عنوان پست

**خط 14:** `content = models.TextField(null=True)`
- محتوای کامل پست
- `null=True`: می‌تواند خالی باشد

**خط 15:** `url = models.URLField(max_length=500, null=True, blank=True)`
- لینک خارجی (اختیاری)
- `max_length=500`: حداکثر طول URL
- `blank=True`: در فرم می‌توان خالی گذاشت

**خط 16:** `category =models.ManyToManyField(Category)`
- رابطه چند به چند با Category
- یک پست می‌تواند چند دسته‌بندی داشته باشد

**خط 17:** `counted_view = models.IntegerField(default=0)`
- شمارنده بازدید
- `default=0`: مقدار پیش‌فرض صفر

**خط 18:** `status = models.BooleanField(default=False)`
- وضعیت انتشار
- `False`: پیش‌نویس (draft)
- `True`: منتشر شده (published)

**خط 19:** `published_date = models.DateTimeField(null=True)`
- تاریخ انتشار
- `null=True`: می‌تواند خالی باشد

**خط 20-21:** فیلدهای تاریخ (مشابه home app)

**خط 23-24:** `class Meta: ordering = ['-creat_date']`
- مرتب‌سازی بر اساس تاریخ ایجاد (جدیدترین اول)
- `-` یعنی نزولی

**خط 26-27:** `def __str__(self): return f"{self.title}"`
- نمایش عنوان در admin

---

### خط 29-37: مدل Newsletter
```python
class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.email
```

**توضیح خط به خط:**

**خط 30:** `email = models.EmailField(unique=True)`
- فیلد ایمیل
- `unique=True`: هر ایمیل فقط یکبار می‌تواند ثبت شود

**خط 31:** `created_date = models.DateTimeField(auto_now_add=True)`
- تاریخ ثبت

**خط 33-34:** `class Meta: ordering = ['-created_date']`
- جدیدترین اول

**خط 36-37:** `def __str__(self): return self.email`
- نمایش ایمیل

---

## 📄 فایل: views.py

### خط 1-8: Import ها
```python
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpRequest
from django.utils import timezone
from django.db.models import Q
from blog.models import Post
from blog.forms import NewsletterForm
from datetime import timedelta
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage
```

**توضیح:**
- `get_object_or_404`: اگر object پیدا نشد، 404 برمی‌گرداند
- `Q`: برای query های پیچیده (OR, AND)
- `Paginator`: برای pagination (صفحه‌بندی)

---

### خط 11-29: View صفحه اصلی وبلاگ
```python
def blog_home(request,**kwargs):
    posts = Post.objects.filter(status=True)
    if kwargs.get('cat_name') != None :
        posts = posts.filter(category__name = kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts= posts.filter(author__username=kwargs['author_username'])
       
    page_all  =  Paginator(posts, 6)
    page = request.GET.get("page")
    try: 
        
        posts = page_all.page(page)
    except PageNotAnInteger:
        posts = page_all.page(1)
    except EmptyPage:
        posts = page_all.page(1)
        
    context = {'posts': posts,'page_range':page_all.page_range}
    return render(request, 'blog/blog_home.html', context)
```

**توضیح خط به خط:**

**خط 11:** `def blog_home(request,**kwargs):`
- `**kwargs`: دریافت پارامترهای اضافی از URL (مثل cat_name, author_username)

**خط 12:** `posts = Post.objects.filter(status=True)`
- فقط پست‌های منتشر شده (`status=True`)

**خط 13-14:** فیلتر بر اساس دسته‌بندی
- `kwargs.get('cat_name')`: بررسی وجود cat_name در kwargs
- `category__name`: دسترسی به فیلد name از Category (double underscore)

**خط 15-16:** فیلتر بر اساس نویسنده
- `author__username`: دسترسی به username از User

**خط 18:** `page_all = Paginator(posts, 6)`
- ایجاد Paginator
- `posts`: queryset
- `6`: تعداد پست در هر صفحه

**خط 19:** `page = request.GET.get("page")`
- دریافت شماره صفحه از URL (?page=2)

**خط 20-26:** مدیریت pagination
- `try-except`: مدیریت خطاها
- `PageNotAnInteger`: اگر page عدد نباشد، صفحه 1
- `EmptyPage`: اگر صفحه خالی باشد، صفحه 1

**خط 28:** `context = {'posts': posts,'page_range':page_all.page_range}`
- `posts`: پست‌های صفحه فعلی
- `page_range`: محدوده صفحات برای نمایش (مثلاً [1,2,3,4,5])

**خط 29:** `return render(request, 'blog/blog_home.html', context)`
- render template

---

### خط 31-46: View جزئیات پست
```python
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
```

**توضیح خط به خط:**

**خط 33:** `post = get_object_or_404(Post, id=post_id, status=True)`
- دریافت پست با id مشخص
- فقط پست‌های منتشر شده
- اگر پیدا نشد، 404

**خط 35-36:** افزایش بازدید
- `counted_view += 1`: افزایش شمارنده
- `save(update_fields=['counted_view'])`: فقط این فیلد را به‌روز می‌کند (performance بهتر)

**خط 38-39:** پست‌های مرتبط
- `filter(status=True)`: فقط منتشر شده
- `exclude(id=post.id)`: غیر از پست فعلی
- `order_by('-published_date', '-creat_date')`: جدیدترین اول
- `[:3]`: فقط 3 پست

**خط 41-44:** context و render

---

### خط 48-60: View جستجو
```python
def blog_search(request:HttpRequest):
    posts = Post.objects.filter(status=True)
    
    if request.method == 'GET':
        search_query = request.GET.get('search', '').strip()
        if search_query:
            posts = posts.filter(
                Q(title__icontains=search_query) | 
                Q(content__icontains=search_query)
            )
        
    context = {'posts': posts}
    return render(request, 'blog/blog_home.html', context)
```

**توضیح خط به خط:**

**خط 49:** `posts = Post.objects.filter(status=True)`
- شروع با همه پست‌های منتشر شده

**خط 51-52:** دریافت query جستجو
- `request.GET.get('search', '')`: دریافت از URL (?search=python)
- `strip()`: حذف فاصله‌های اضافی

**خط 53-56:** فیلتر بر اساس جستجو
- `Q(title__icontains=...)`: جستجو در عنوان (case-insensitive)
- `Q(content__icontains=...)`: جستجو در محتوا
- `|`: OR (یا)
- `icontains`: شامل باشد (بدون توجه به حروف بزرگ/کوچک)

**خط 58-59:** context و render

---

### خط 62-69: View ثبت Newsletter
```python
def save_newsletter(request:HttpRequest):
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:blog_home')
    
    return redirect('blog:blog_home')
```

**توضیح:**
- دریافت فرم POST
- validation
- ذخیره در دیتابیس
- redirect به صفحه اصلی وبلاگ

---

## 📄 فایل: urls.py

```python
from django.urls import path
from blog.views import blog_home, blog_detail,blog_search,save_newsletter

app_name = 'blog'

urlpatterns = [
    path('', blog_home, name='blog_home'),
    path('<int:post_id>/', blog_detail, name='blog_detail'),
    path('category/<str:cat_name>/',blog_home,name='category'),
    path('author/<str:author_username>/',blog_home,name='author'),
    path('search/',blog_search,name='search'),
    path('newsletter/',save_newsletter,name="save_newsletter")
]
```

**توضیح خط به خط:**

**خط 4:** `app_name = 'blog'`
- namespace برای این app

**خط 7:** `path('', blog_home, name='blog_home')`
- URL: `/blog/`
- View: `blog_home`

**خط 8:** `path('<int:post_id>/', blog_detail, name='blog_detail')`
- URL: `/blog/1/` (1 = post_id)
- `<int:post_id>`: دریافت post_id به صورت integer

**خط 9:** `path('category/<str:cat_name>/',blog_home,name='category')`
- URL: `/blog/category/python/`
- `<str:cat_name>`: دریافت نام دسته‌بندی
- همان view `blog_home` استفاده می‌شود (با kwargs)

**خط 10:** `path('author/<str:author_username>/',blog_home,name='author')`
- URL: `/blog/author/admin/`
- فیلتر بر اساس نویسنده

**خط 11:** `path('search/',blog_search,name='search')`
- URL: `/blog/search/?search=python`

**خط 12:** `path('newsletter/',save_newsletter,name="save_newsletter")`
- URL: `/blog/newsletter/`
- برای ثبت ایمیل در newsletter

---

## 📄 فایل: forms.py

```python
from django.forms import ModelForm
from django import forms
from blog.models import Newsletter


class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'ایمیل خود را وارد کنید',
                'required': True
            })
        }
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Newsletter.objects.filter(email=email).exists():
            raise forms.ValidationError('این ایمیل قبلاً ثبت شده است.')
        return email
```

**توضیح خط به خط:**

**خط 6-15:** تعریف فرم
- `ModelForm`: فرم بر اساس مدل Newsletter
- `fields = ['email']`: فقط فیلد email
- `widgets`: تنظیمات HTML input
  - `placeholder`: متن راهنما
  - `required`: اجباری

**خط 17-21:** `clean_email()`
- Custom validation
- `cleaned_data`: داده‌های تمیز شده
- بررسی تکراری نبودن ایمیل
- `ValidationError`: خطای validation

---

## 📄 فایل: admin.py

```python
from django.contrib import admin
from blog.models import Post,Category,Newsletter

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'creat_date'
    empty_value_display="-empty"
    list_display = ('title' ,'counted_view','status','published_date','creat_date')
    list_filter = ('status',)
    search_fields = ['title','content'] 
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    
   
@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'created_date')
    search_fields = ('email',)
    list_filter = ('created_date',)
```

**توضیح:**

**خط 5-10:** PostAdmin
- `date_hierarchy`: فیلتر تاریخ در بالای صفحه
- `empty_value_display`: نمایش برای فیلدهای خالی
- `list_display`: ستون‌های لیست
- `list_filter`: فیلتر در سایدبار
- `search_fields`: فیلدهای قابل جستجو

**خط 12-15:** CategoryAdmin
- تنظیمات ساده برای Category

**خط 17-21:** NewsletterAdmin
- تنظیمات برای Newsletter

---

## 📄 فایل: templatetags/blog_tags.py

```python
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
```

**توضیح خط به خط:**

**خط 1-3:** Import و register
- `template.Library()`: ثبت template tags

**خط 6-9:** `pupolarposts` tag
- `@register.inclusion_tag(...)`: inclusion tag (render یک template)
- `arg=3`: پارامتر پیش‌فرض (3 پست)
- دریافت پست‌های منتشر شده
- مرتب‌سازی بر اساس تاریخ انتشار
- `[:arg]`: محدود کردن تعداد

**خط 11-18:** `postcategories` tag
- دریافت همه دسته‌بندی‌ها
- شمارش پست‌های هر دسته‌بندی
- `cat_dict`: دیکشنری {category: count}
- بازگرداندن برای استفاده در template

**استفاده در template:**
```django
{% load blog_tags %}
{% pupolarposts 5 %}
{% postcategories %}
```

---

## 📄 Templates

### blog_home.html
- لیست پست‌ها
- Pagination
- فیلتر دسته‌بندی
- جستجو

### blog_detail.html
- نمایش کامل پست
- پست‌های مرتبط
- افزایش بازدید

### blog_category_sidebar.html
- لیست دسته‌بندی‌ها با تعداد پست

### latest_posts.html
- نمایش آخرین پست‌ها

---

## 🔄 جریان کار (Flow)

### 1. صفحه اصلی وبلاگ
```
User → /blog/ → blog_home() → blog_home.html
```

### 2. فیلتر دسته‌بندی
```
User → /blog/category/python/ → blog_home(cat_name='python') → فیلتر → نمایش
```

### 3. جزئیات پست
```
User → /blog/1/ → blog_detail(post_id=1) → افزایش بازدید → blog_detail.html
```

### 4. جستجو
```
User → /blog/search/?search=python → blog_search() → فیلتر → نمایش
```

### 5. ثبت Newsletter
```
User → POST /blog/newsletter/ → save_newsletter() → ذخیره → redirect
```

---

## 📝 نکات مهم

1. **Pagination**: استفاده از Paginator برای صفحه‌بندی
2. **Query Optimization**: استفاده از `update_fields` برای به‌روزرسانی سریع‌تر
3. **Q Objects**: برای query های پیچیده (OR, AND)
4. **Template Tags**: برای کدهای قابل استفاده مجدد
5. **Status Field**: کنترل انتشار پست‌ها
6. **View Counter**: شمارش بازدید هر پست

---

## 🎯 خلاصه

این app شامل:
- ✅ سیستم وبلاگ کامل
- ✅ دسته‌بندی پست‌ها
- ✅ جستجو
- ✅ Pagination
- ✅ Newsletter
- ✅ شمارش بازدید
- ✅ پست‌های مرتبط
- ✅ Custom template tags

