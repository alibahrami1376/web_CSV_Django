# لیست مشکلات پروژه Web_CSV_Django

این فایل شامل تمام مشکلات شناسایی شده در پروژه است که باید برطرف شوند.

---

## 🔴 مشکلات بحرانی (Critical)

### 1. مشکل Type Hint اشتباه در Views
**فایل‌های مشکل‌دار:**
- `home/views.py` خط 25: `def save_contact(request:request):`
- `blog/views.py` خط 47: `def blog_search(request:request):`
- `blog/views.py` خط 56: `def save_newsletter(request:request):`

**مشکل:** `request:request` اشتباه است. باید `request` باشد یا از `HttpRequest` استفاده شود.

**راه حل:**
```python
# اشتباه:
def save_contact(request:request):

# درست:
def save_contact(request: HttpRequest):
# یا
def save_contact(request):
```

---

### 2. مشکل Import اشتباه در blog/views.py
**فایل:** `blog/views.py` خط 2

**مشکل:** 
```python
from django.http import request
```
این import اشتباه است. `request` یک ماژول نیست، بلکه یک پارامتر است.

**راه حل:** این خط را حذف کنید.

---

### 3. مشکل امنیتی: SECRET_KEY در settings.py
**فایل:** `website/settings.py` خط 23

**مشکل:** 
```python
SECRET_KEY = 'django-insecure-@i57f*3nduso2gldjq7-sm9tsdh0bqc5sa$^-!a7ngax(k8w2g'
```

**مشکل:** SECRET_KEY در کد قرار دارد و برای production مناسب نیست.

**راه حل:** از متغیرهای محیطی استفاده کنید:
```python
import os
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-...')
```

---

### 4. مشکل DEBUG = True در Production
**فایل:** `website/settings.py` خط 26

**مشکل:** 
```python
DEBUG = True
```

**راه حل:** برای production باید `DEBUG = False` باشد و از متغیر محیطی استفاده کنید:
```python
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
```

---

### 5. مشکل ALLOWED_HOSTS خالی
**فایل:** `website/settings.py` خط 28

**مشکل:** 
```python
ALLOWED_HOSTS = []
```

**راه حل:** برای production باید host های مجاز را اضافه کنید:
```python
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
```

---

## 🟡 مشکلات مهم (Important)

### 6. مشکل مدیریت Profile در base.html
**فایل:** `templates/base.html` خط 16

**مشکل:** اگر `user.profile` وجود نداشته باشد خطا می‌دهد.

**راه حل:** 
```django
{% if user.is_authenticated %}
  {% if user.profile %}
    <portfolio-header
      data-is-auth="true"
      data-avatar="{% if user.profile.avatar %}{{ user.profile.avatar.url }}{% endif %}"
      data-profile-url="{% url 'home:profile' %}"
    ></portfolio-header>
  {% else %}
    <portfolio-header data-is-auth="true"></portfolio-header>
  {% endif %}
{% else %}
  <portfolio-header data-is-auth="false"></portfolio-header>
{% endif %}
```

---

### 7. مشکل Signal در models.py - احتمال Infinite Loop
**فایل:** `home/models.py` خط 43-48

**مشکل:** 
```python
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()  # این می‌تواند باعث loop شود
```

**راه حل:** از `update_fields` استفاده کنید یا `created` را چک کنید:
```python
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    if not created:
        if hasattr(instance, 'profile'):
            instance.profile.save(update_fields=[])
```

---

### 8. مشکل Pagination در blog_home
**فایل:** `blog/views.py` خط 17

**مشکل:** 
```python
page_all = Paginator(posts, 1)  # فقط 1 پست در هر صفحه!
```

**راه حل:** تعداد مناسب را تنظیم کنید:
```python
page_all = Paginator(posts, 6)  # یا هر تعداد مناسب
```

---

### 9. مشکل URL Pattern در blog/urls.py
**فایل:** `blog/urls.py` خط 10

**مشکل:** 
```python
path('author/<str:author_username>',blog_home,name='author')
```

**مشکل:** `/` در انتها نیست که می‌تواند باعث مشکل شود.

**راه حل:**
```python
path('author/<str:author_username>/',blog_home,name='author')
```

---

### 10. مشکل Search در blog_search
**فایل:** `blog/views.py` خط 51

**مشکل:** 
```python
posts = posts.filter(content__contains=request.GET.get('search'))
```

**مشکلات:**
- اگر `search` خالی باشد، همه پست‌ها را برمی‌گرداند
- `__contains` case-sensitive است
- باید از `__icontains` استفاده شود

**راه حل:**
```python
search_query = request.GET.get('search', '').strip()
if search_query:
    posts = posts.filter(
        Q(title__icontains=search_query) | 
        Q(content__icontains=search_query)
    )
```

---

### 11. مشکل Print Statements در Production
**فایل:** `blog/views.py` خط 58, 60, 63

**مشکل:** 
```python
print("salaa,m")
print(form.is_valid())
print("save")
```

**راه حل:** این print ها را حذف کنید یا از logging استفاده کنید:
```python
import logging
logger = logging.getLogger(__name__)
logger.debug("Newsletter form submitted")
```

---

### 12. مشکل Default Avatar در Profile Model
**فایل:** `home/models.py` خط 20

**مشکل:** 
```python
avatar = models.ImageField(upload_to='profiles/', default='profiles/default.png', blank=True, null=True)
```

**مشکل:** فایل `profiles/default.png` ممکن است وجود نداشته باشد.

**راه حل:** از `blank=True, null=True` استفاده کنید و در template چک کنید.

---

## 🟢 مشکلات جزئی (Minor)

### 13. مشکل نام فیلد در Post Model
**فایل:** `blog/models.py` خط 20

**مشکل:** 
```python
creat_date = models.DateTimeField(auto_now_add=True)
```

**مشکل:** نام فیلد `creat_date` است که باید `created_date` باشد.

**راه حل:** نام را تغییر دهید (نیاز به migration دارد).

---

### 14. مشکل Ordering در Post Model
**فایل:** `blog/models.py` خط 24

**مشکل:** 
```python
ordering = ['creat_date']  # قدیمی‌ترین اول
```

**راه حل:** معمولاً باید جدیدترین اول باشد:
```python
ordering = ['-creat_date']
```

---

### 15. مشکل Static Files در Production
**فایل:** `website/urls.py` خط 27-28

**مشکل:** 
```python
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

**مشکل:** این فقط برای development است. در production باید از web server استفاده شود.

**راه حل:** 
```python
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

---

### 16. مشکل TIME_ZONE در settings.py
**فایل:** `website/settings.py` خط 112

**مشکل:** 
```python
TIME_ZONE = 'UTC'
```

**راه حل:** برای ایران:
```python
TIME_ZONE = 'Asia/Tehran'
```

---

### 17. مشکل LANGUAGE_CODE در settings.py
**فایل:** `website/settings.py` خط 110

**مشکل:** 
```python
LANGUAGE_CODE = 'en-us'
```

**راه حل:** برای فارسی:
```python
LANGUAGE_CODE = 'fa'
```

---

### 18. مشکل Missing Middleware Closing
**فایل:** `website/settings.py` خط 51

**مشکل:** 
```python
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


ROOT_URLCONF = 'website.urls'
```

**مشکل:** یک خط خالی اضافی وجود دارد.

**راه حل:** خط خالی را حذف کنید.

---

### 19. مشکل Namespace در blog URLs
**فایل:** `website/urls.py` خط 25

**مشکل:** 
```python
path('blog/',include('blog.urls'),name='blog'),
```

**مشکل:** `name='blog'` در اینجا استفاده نمی‌شود. باید namespace باشد:
```python
path('blog/',include('blog.urls', namespace='blog')),
```

---

### 20. مشکل Missing Error Handling در signup_view
**فایل:** `home/views.py` خط 102

**مشکل:** Exception handling خیلی عمومی است.

**راه حل:** Exception های خاص را handle کنید:
```python
except IntegrityError as e:
    messages.error(request, 'خطا در ایجاد حساب کاربری. لطفاً دوباره تلاش کنید.')
except Exception as e:
    logger.error(f"Error creating user: {e}")
    messages.error(request, 'خطای غیرمنتظره رخ داد. لطفاً دوباره تلاش کنید.')
```

---

## 📝 مشکلات کد نویسی (Code Quality)

### 21. مشکل Comment در Post Model
**فایل:** `blog/models.py` خط 16

**مشکل:** 
```python
#tag
```

**راه حل:** یا کامنت را کامل کنید یا حذف کنید.

---

### 22. مشکل Whitespace در URLs
**فایل:** `home/urls.py` خط 8

**مشکل:** 
```python
path('', home_page ,name= "home"),
```

**راه حل:** فاصله‌های اضافی را حذف کنید:
```python
path('', home_page, name="home"),
```

---

### 23. مشکل Missing CSRF Protection Check
**مشکل:** در برخی از فرم‌ها CSRF token وجود دارد اما باید مطمئن شوید که همه فرم‌ها آن را دارند.

---

### 24. مشکل Missing Validation در Forms
**مشکل:** برخی از فرم‌ها validation کافی ندارند.

**راه حل:** از Django forms استفاده کنید و validation اضافه کنید.

---

## 🔧 مشکلات Migration

### 25. نیاز به Migration برای Profile Model
**مشکل:** مدل Profile اضافه شده اما migration ممکن است اجرا نشده باشد.

**راه حل:**
```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 📦 مشکلات Dependencies

### 26. Missing requirements.txt
**مشکل:** فایل `requirements.txt` وجود ندارد.

**راه حل:** ایجاد کنید:
```bash
pip freeze > requirements.txt
```

---

## 🎨 مشکلات Frontend

### 27. مشکل Feather Icons Loading
**مشکل:** Feather Icons از CDN لود می‌شود که ممکن است در offline کار نکند.

**راه حل:** فایل‌های Feather Icons را به صورت local اضافه کنید.

---

### 28. مشکل Missing Error Pages
**مشکل:** صفحات 404 و 500 وجود ندارند.

**راه حل:** ایجاد کنید:
- `templates/404.html`
- `templates/500.html`

---

## 📊 خلاصه مشکلات

- **مشکلات بحرانی:** 5 مورد
- **مشکلات مهم:** 7 مورد
- **مشکلات جزئی:** 8 مورد
- **مشکلات کد نویسی:** 4 مورد
- **مشکلات Migration:** 1 مورد
- **مشکلات Dependencies:** 1 مورد
- **مشکلات Frontend:** 2 مورد

**جمع کل:** 28 مشکل

---

## ✅ اولویت‌بندی برای رفع

### اولویت 1 (فوری):
1. رفع Type Hint اشتباه
2. رفع Import اشتباه
3. رفع مشکل Profile در base.html
4. رفع مشکل Signal

### اولویت 2 (مهم):
5. رفع مشکلات امنیتی (SECRET_KEY, DEBUG, ALLOWED_HOSTS)
6. رفع مشکل Search
7. رفع مشکل Pagination
8. حذف Print Statements

### اولویت 3 (بهبود):
9. رفع مشکلات جزئی
10. بهبود کد نویسی
11. اضافه کردن Error Pages

---

**تاریخ ایجاد:** 2025-01-27  
**آخرین به‌روزرسانی:** 2025-01-27
