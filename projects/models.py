from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_quill.fields import QuillField

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

class Projects(models.Model):
    STATUS_CHOICES = [
        ('completed', 'تکمیل شده'),
        ('in_progress', 'در حال توسعه'),
        ('on_hold', 'متوقف شده'),
    ]
    
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, allow_unicode=True)
    description = models.TextField()
    content = QuillField()
    image = models.ImageField(upload_to='projects/', default='projects/default.jpg', blank=True, null=True)
    category = models.ManyToManyField(Category, related_name='projects', verbose_name='دسته‌بندی')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    github_url = models.URLField(blank=True, null=True, verbose_name='لینک GitHub')
    demo_url = models.URLField(blank=True, null=True, verbose_name='لینک دمو')
    website_url = models.URLField(blank=True, null=True, verbose_name='لینک وب‌سایت')
    featured = models.BooleanField(default=False, verbose_name='پروژه ویژه')
    view_count = models.IntegerField(default=0, verbose_name='تعداد بازدید')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='تاریخ به‌روزرسانی')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='تاریخ انتشار')
    
    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.title
    
    def get_status_display_class(self):
        status_classes = {
            'completed': 'status-completed',
            'in_progress': 'status-in-progress',
            'on_hold': 'status-on-hold',
        }
        return status_classes.get(self.status, '')
    
    def get_absolute_url(self):
        return reverse('projects:project_detail', kwargs={'project_slug': self.slug})
    
    def get_categories_list(self):
        return ', '.join([cat.name for cat in self.category.all()])      