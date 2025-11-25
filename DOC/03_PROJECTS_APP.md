# مستندات کامل App: PROJECTS

## 📁 ساختار App
```
projects/
├── __init__.py
├── models.py            # مدل‌های Projects, Category
├── views.py             # View functions
├── urls.py              # URL routing
├── forms.py             # فرم جستجو
├── admin.py             # تنظیمات Django Admin
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
- مشابه blog app

---

### خط 4-16: مدل Category
```python
class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='نام دسته‌بندی')
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True, verbose_name='اسلاگ')
    description = models.TextField(blank=True, null=True, verbose_name='توضیحات')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    
    class Meta:
        verbose_name = 'دسته‌بندی پروژه'
        verbose_name_plural = 'دسته‌بندی‌های پروژه'
        ordering = ['name']
    
    def __str__(self):
        return self.name
```

**توضیح خط به خط:**

**خط 5:** `name = models.CharField(max_length=255, verbose_name='نام دسته‌بندی')`
- نام دسته‌بندی
- `verbose_name`: نام فارسی در admin

**خط 6:** `slug = models.SlugField(max_length=255, unique=True, allow_unicode=True, verbose_name='اسلاگ')`
- `SlugField`: برای URL-friendly strings (مثلاً "python-project")
- `unique=True`: یکتا بودن
- `allow_unicode=True`: پشتیبانی از کاراکترهای فارسی

**خط 7:** `description = models.TextField(blank=True, null=True, verbose_name='توضیحات')`
- توضیحات دسته‌بندی (اختیاری)

**خط 8:** `created_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')`
- تاریخ ایجاد

**خط 10-13:** `class Meta:`
- `verbose_name`: نام مفرد فارسی
- `verbose_name_plural`: نام جمع فارسی
- `ordering = ['name']`: مرتب‌سازی بر اساس نام

---

### خط 18-66: مدل Projects
```python
class Projects(models.Model):
    STATUS_CHOICES = [
        ('completed', 'تکمیل شده'),
        ('in_progress', 'در حال توسعه'),
        ('on_hold', 'متوقف شده'),
    ]
    
    title = models.CharField(max_length=255, verbose_name='عنوان')
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True, verbose_name='اسلاگ')
    description = models.TextField(verbose_name='توضیحات کوتاه')
    content = models.TextField(blank=True, null=True, verbose_name='محتوای کامل')
    image = models.ImageField(upload_to='projects/', default='projects/default.jpg', blank=True, null=True, verbose_name='تصویر')
    category = models.ManyToManyField(Category, related_name='projects', verbose_name='دسته‌بندی')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='نویسنده')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress', verbose_name='وضعیت')
    github_url = models.URLField(blank=True, null=True, verbose_name='لینک GitHub')
    demo_url = models.URLField(blank=True, null=True, verbose_name='لینک دمو')
    website_url = models.URLField(blank=True, null=True, verbose_name='لینک وب‌سایت')
    featured = models.BooleanField(default=False, verbose_name='پروژه ویژه')
    view_count = models.IntegerField(default=0, verbose_name='تعداد بازدید')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='تاریخ به‌روزرسانی')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ انتشار')
    
    class Meta:
        verbose_name = 'پروژه'
        verbose_name_plural = 'پروژه‌ها'
        ordering = ['-created_date']
    
    def __str__(self):
        return self.title
    
    def get_status_display_class(self):
        """برگرداندن کلاس CSS برای وضعیت"""
        status_classes = {
            'completed': 'status-completed',
            'in_progress': 'status-in-progress',
            'on_hold': 'status-on-hold',
        }
        return status_classes.get(self.status, '')
    
    def get_absolute_url(self):
        """برگرداندن URL کامل پروژه"""
        from django.urls import reverse
        return reverse('projects:project_detail', kwargs={'project_slug': self.slug})
    
    def get_categories_list(self):
        """برگرداندن لیست دسته‌بندی‌ها به صورت رشته"""
        return ', '.join([cat.name for cat in self.category.all()])
```

**توضیح خط به خط:**

**خط 19-23:** `STATUS_CHOICES`
- لیست انتخاب‌ها برای فیلد status
- `('completed', 'تکمیل شده')`: مقدار در دیتابیس و نمایش فارسی

**خط 25:** `title = models.CharField(max_length=255, verbose_name='عنوان')`
- عنوان پروژه

**خط 26:** `slug = models.SlugField(...)`
- اسلاگ برای URL (مثلاً "python-web-app")

**خط 27:** `description = models.TextField(verbose_name='توضیحات کوتاه')`
- توضیحات کوتاه (اجباری)

**خط 28:** `content = models.TextField(blank=True, null=True, verbose_name='محتوای کامل')`
- محتوای کامل (اختیاری)

**خط 29:** `image = models.ImageField(...)`
- تصویر پروژه
- `upload_to='projects/'`: ذخیره در media/projects/

**خط 30:** `category = models.ManyToManyField(Category, related_name='projects', ...)`
- رابطه چند به چند با Category
- `related_name='projects'`: از Category می‌توان با `category.projects.all()` دسترسی داشت

**خط 31:** `author = models.ForeignKey(User, ...)`
- نویسنده پروژه
- `on_delete=models.SET_NULL`: اگر User حذف شود، author = NULL

**خط 32:** `status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress', ...)`
- وضعیت پروژه
- `choices=STATUS_CHOICES`: استفاده از لیست انتخاب‌ها
- `default='in_progress'`: پیش‌فرض "در حال توسعه"

**خط 33-35:** فیلدهای URL
- `github_url`: لینک GitHub
- `demo_url`: لینک دمو
- `website_url`: لینک وب‌سایت
- همه اختیاری هستند

**خط 36:** `featured = models.BooleanField(default=False, verbose_name='پروژه ویژه')`
- آیا پروژه ویژه است یا نه
- برای نمایش در صفحه اصلی

**خط 37:** `view_count = models.IntegerField(default=0, verbose_name='تعداد بازدید')`
- شمارنده بازدید

**خط 38-40:** فیلدهای تاریخ

**خط 42-45:** `class Meta:`
- تنظیمات مدل

**خط 47-48:** `def __str__(self):`
- نمایش عنوان

**خط 50-58:** `get_status_display_class()`
- متد کمکی برای CSS class
- بر اساس status، کلاس CSS برمی‌گرداند
- برای استایل‌دهی در template

**خط 60-63:** `get_absolute_url()`
- متد استاندارد Django
- URL کامل پروژه را برمی‌گرداند
- `reverse()`: ساخت URL از name
- استفاده: `project.get_absolute_url()`

**خط 65-66:** `get_categories_list()`
- لیست دسته‌بندی‌ها به صورت رشته
- `', '.join(...)`: اتصال با کاما
- `[cat.name for cat in self.category.all()]`: list comprehension

---

## 📄 فایل: views.py

### خط 1-5: Import ها
```python
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q, Count
from projects.models import Projects, Category
from django.http import HttpRequest
```

**توضیح:**
- `Count`: برای شمارش (aggregation)
- بقیه مشابه blog app

---

### خط 7-82: View لیست پروژه‌ها
```python
def projects_list(request: HttpRequest, category_slug=None):
    """نمایش لیست تمام پروژه‌ها"""
    projects = Projects.objects.all()
    
    # فیلتر بر اساس دسته‌بندی (از URL یا GET parameter)
    if category_slug:
        projects = projects.filter(category__slug=category_slug)
    else:
        category_slug = request.GET.get('category')
        if category_slug:
            projects = projects.filter(category__slug=category_slug)
    
    # فیلتر پروژه‌های ویژه
    featured_only = request.GET.get('featured')
    if featured_only == 'true':
        projects = projects.filter(featured=True)
    
    # جستجو
    search_query = request.GET.get('search', '').strip()
    if search_query:
        projects = projects.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(content__icontains=search_query)
        )
    
    # فیلتر بر اساس وضعیت
    status_filter = request.GET.get('status')
    if status_filter:
        projects = projects.filter(status=status_filter)
    
    # مرتب‌سازی
    sort_options = {
        'newest': '-created_date',
        'oldest': 'created_date',
        'most_viewed': '-view_count',
        'title_asc': 'title',
        'title_desc': '-title',
    }
    sort_by = request.GET.get('sort', 'newest')
    sort_field = sort_options.get(sort_by, '-created_date')
    projects = projects.order_by(sort_field)
    
    # Pagination
    paginator = Paginator(projects, 9)  # 9 پروژه در هر صفحه
    page = request.GET.get('page')
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        projects = paginator.page(1)
    except EmptyPage:
        projects = paginator.page(paginator.num_pages)
    
    # دریافت دسته‌بندی‌ها با تعداد پروژه‌ها
    categories = Category.objects.annotate(
        project_count=Count('projects')
    ).order_by('name')
    
    # آمار کلی
    total_projects = Projects.objects.count()
    completed_projects = Projects.objects.filter(status='completed').count()
    in_progress_projects = Projects.objects.filter(status='in_progress').count()
    
    context = {
        'projects': projects,
        'categories': categories,
        'current_category': category_slug,
        'current_status': status_filter,
        'search_query': search_query,
        'sort_by': sort_by,
        'page_range': paginator.page_range,
        'total_projects': total_projects,
        'completed_projects': completed_projects,
        'in_progress_projects': in_progress_projects,
    }
    return render(request, 'projects/projects_list.html', context)
```

**توضیح خط به خط:**

**خط 7:** `def projects_list(request: HttpRequest, category_slug=None):`
- `category_slug=None`: پارامتر اختیاری از URL

**خط 9:** `projects = Projects.objects.all()`
- شروع با همه پروژه‌ها

**خط 11-17:** فیلتر دسته‌بندی
- اگر `category_slug` از URL آمده باشد
- یا از GET parameter (?category=python)
- `category__slug`: دسترسی به slug از Category

**خط 19-22:** فیلتر پروژه‌های ویژه
- `featured_only == 'true'`: فقط پروژه‌های ویژه

**خط 24-31:** جستجو
- جستجو در title، description، content
- `Q(...)`: برای OR query

**خط 33-36:** فیلتر وضعیت
- فیلتر بر اساس status (completed, in_progress, on_hold)

**خط 38-48:** مرتب‌سازی
- `sort_options`: دیکشنری گزینه‌های مرتب‌سازی
- `sort_by`: دریافت از GET parameter
- `sort_field`: فیلد مرتب‌سازی
- `order_by(sort_field)`: اعمال مرتب‌سازی

**خط 50-58:** Pagination
- مشابه blog app
- 9 پروژه در هر صفحه

**خط 60-63:** دسته‌بندی‌ها با تعداد
- `annotate(project_count=Count('projects'))`: شمارش پروژه‌های هر دسته
- `Count('projects')`: استفاده از related_name

**خط 65-68:** آمار کلی
- تعداد کل پروژه‌ها
- تعداد پروژه‌های تکمیل شده
- تعداد پروژه‌های در حال توسعه

**خط 70-82:** context و render

---

### خط 84-119: View جزئیات پروژه
```python
def project_detail(request: HttpRequest, project_slug: str = None, project_id: int = None):
    """نمایش جزئیات یک پروژه"""
    # پشتیبانی از هر دو slug و id
    if project_slug:
        project = get_object_or_404(Projects, slug=project_slug)
    elif project_id:
        project = get_object_or_404(Projects, id=project_id)
    else:
        from django.http import Http404
        raise Http404("Project not found")
    
    # افزایش تعداد بازدید (فقط یک بار در هر session)
    session_key = f'project_viewed_{project.id}'
    if not request.session.get(session_key, False):
        project.view_count += 1
        project.save(update_fields=['view_count'])
        request.session[session_key] = True
    
    # دریافت پروژه‌های مرتبط (از همان دسته‌بندی)
    related_projects = Projects.objects.filter(
        category__in=project.category.all()
    ).exclude(id=project.id).distinct()[:3]
    
    # اگر پروژه مرتبطی نبود، آخرین پروژه‌ها را نشان بده
    if not related_projects.exists():
        related_projects = Projects.objects.exclude(id=project.id).order_by('-created_date')[:3]
    
    # دریافت پروژه‌های ویژه
    featured_projects = Projects.objects.filter(featured=True).exclude(id=project.id)[:3]
    
    context = {
        'project': project,
        'related_projects': related_projects,
        'featured_projects': featured_projects,
    }
    return render(request, 'projects/project_detail.html', context)
```

**توضیح خط به خط:**

**خط 84:** `def project_detail(..., project_slug: str = None, project_id: int = None):`
- پشتیبانی از هر دو slug و id
- برای سازگاری با URL های قدیمی

**خط 86-92:** دریافت پروژه
- اول slug را چک می‌کند
- اگر نبود، id را چک می‌کند
- اگر هیچکدام نبود، 404

**خط 94-99:** افزایش بازدید (یکبار در session)
- `session_key`: کلید session منحصر به فرد
- `request.session.get(session_key, False)`: بررسی دیده شدن
- اگر دیده نشده، بازدید را افزایش می‌دهد
- `request.session[session_key] = True`: علامت‌گذاری

**خط 101-105:** پروژه‌های مرتبط
- از همان دسته‌بندی‌ها
- `category__in=project.category.all()`: فیلتر بر اساس دسته‌بندی‌های پروژه فعلی
- `distinct()`: حذف تکراری‌ها (چون ManyToMany)
- `[:3]`: فقط 3 پروژه

**خط 107-108:** fallback
- اگر پروژه مرتبطی نبود، آخرین پروژه‌ها

**خط 110-111:** پروژه‌های ویژه
- برای نمایش در sidebar

---

## 📄 فایل: urls.py

```python
from django.urls import path
from projects.views import projects_list, project_detail

app_name = 'projects'

urlpatterns = [
    path('', projects_list, name='projects_list'),
    path('category/<str:category_slug>/', projects_list, name='projects_by_category'),
    path('<str:project_slug>/', project_detail, name='project_detail'),
    path('id/<int:project_id>/', project_detail, name='project_detail_by_id'),  # پشتیبانی از id برای سازگاری
]
```

**توضیح:**

**خط 7:** `path('', projects_list, name='projects_list')`
- URL: `/projects/`
- لیست همه پروژه‌ها

**خط 8:** `path('category/<str:category_slug>/', projects_list, name='projects_by_category')`
- URL: `/projects/category/python/`
- فیلتر بر اساس دسته‌بندی

**خط 9:** `path('<str:project_slug>/', project_detail, name='project_detail')`
- URL: `/projects/python-web-app/`
- جزئیات پروژه با slug

**خط 10:** `path('id/<int:project_id>/', project_detail, name='project_detail_by_id')`
- URL: `/projects/id/1/`
- جزئیات پروژه با id (برای سازگاری)

---

## 📄 فایل: forms.py

```python
from django import forms
from projects.models import Projects, Category

class ProjectSearchForm(forms.Form):
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'جستجو در پروژه‌ها...',
            'class': 'form-control'
        })
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        empty_label='همه دسته‌بندی‌ها',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    status = forms.ChoiceField(
        choices=[('', 'همه وضعیت‌ها')] + Projects.STATUS_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
```

**توضیح:**

**خط 4:** `class ProjectSearchForm(forms.Form):`
- فرم معمولی (نه ModelForm)
- برای جستجو و فیلتر

**خط 5-10:** فیلد جستجو
- `required=False`: اختیاری
- `widget`: تنظیمات HTML
- `placeholder`: متن راهنما

**خط 11-17:** فیلد دسته‌بندی
- `ModelChoiceField`: انتخاب از مدل Category
- `queryset=Category.objects.all()`: همه دسته‌بندی‌ها
- `empty_label`: متن برای "همه"

**خط 18-23:** فیلد وضعیت
- `ChoiceField`: انتخاب از لیست
- `[('', 'همه وضعیت‌ها')] + Projects.STATUS_CHOICES`: اضافه کردن گزینه "همه"

---

## 📄 فایل: admin.py

```python
from django.contrib import admin
from projects.models import Projects, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_date')
    list_filter = ('created_date',)
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'featured', 'view_count', 'author', 'created_date')
    list_filter = ('status', 'featured', 'category', 'created_date')
    search_fields = ('title', 'description', 'content')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('category',)
    readonly_fields = ('view_count', 'created_date', 'updated_date')
    date_hierarchy = 'created_date'
    ordering = ('-created_date',)
    
    fieldsets = (
        ('اطلاعات اصلی', {
            'fields': ('title', 'slug', 'description', 'content', 'image')
        }),
        ('دسته‌بندی و وضعیت', {
            'fields': ('category', 'status', 'featured')
        }),
        ('لینک‌ها', {
            'fields': ('github_url', 'demo_url', 'website_url')
        }),
        ('اطلاعات تکمیلی', {
            'fields': ('author', 'published_date')
        }),
        ('آمار', {
            'fields': ('view_count', 'created_date', 'updated_date'),
            'classes': ('collapse',)
        }),
    )
```

**توضیح:**

**خط 5-9:** CategoryAdmin
- `prepopulated_fields = {'slug': ('name',)}`: slug به صورت خودکار از name ساخته می‌شود

**خط 11-40:** ProjectsAdmin
- `prepopulated_fields = {'slug': ('title',)}`: slug از title
- `filter_horizontal = ('category',)`: رابط بهتر برای ManyToMany
- `readonly_fields`: فیلدهای فقط خواندنی
- `fieldsets`: گروه‌بندی فیلدها در فرم admin
  - `'classes': ('collapse',)`: قابل بستن

---

## 🔄 جریان کار (Flow)

### 1. لیست پروژه‌ها
```
User → /projects/ → projects_list() → فیلتر/جستجو/مرتب‌سازی → Pagination → نمایش
```

### 2. فیلتر دسته‌بندی
```
User → /projects/category/python/ → projects_list(category_slug='python') → فیلتر → نمایش
```

### 3. جزئیات پروژه
```
User → /projects/python-app/ → project_detail(project_slug='python-app') → افزایش بازدید → نمایش
```

---

## 📝 نکات مهم

1. **Slug vs ID**: پشتیبانی از هر دو برای سازگاری
2. **Session-based View Counter**: جلوگیری از افزایش مصنوعی بازدید
3. **Advanced Filtering**: فیلتر چندگانه (دسته، وضعیت، جستجو)
4. **Sorting Options**: چند گزینه مرتب‌سازی
5. **Related Projects**: پروژه‌های مرتبط بر اساس دسته‌بندی
6. **Aggregation**: استفاده از Count برای آمار
7. **Prepopulated Fields**: slug خودکار در admin

---

## 🎯 خلاصه

این app شامل:
- ✅ سیستم مدیریت پروژه‌ها
- ✅ دسته‌بندی با slug
- ✅ فیلتر پیشرفته
- ✅ جستجو
- ✅ مرتب‌سازی
- ✅ Pagination
- ✅ شمارش بازدید (session-based)
- ✅ پروژه‌های مرتبط
- ✅ پروژه‌های ویژه
- ✅ لینک‌های GitHub/Demo/Website

