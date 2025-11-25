# مستندات کامل App: HOME

## 📁 ساختار App
```
home/
├── __init__.py          # فایل اولیه برای شناسایی app به عنوان Python package
├── models.py            # مدل‌های دیتابیس (Contact, Profile)
├── views.py             # View functions (منطق اصلی برنامه)
├── urls.py              # URL routing
├── forms.py             # فرم‌های Django
├── admin.py             # تنظیمات Django Admin
├── apps.py              # تنظیمات app
├── content.json         # محتوای استاتیک صفحه اصلی
└── migrations/          # فایل‌های migration دیتابیس
```

---

## 📄 فایل: models.py

### توضیح کلی
این فایل شامل دو مدل اصلی است:
1. **Contact**: برای ذخیره پیام‌های تماس کاربران
2. **Profile**: برای اطلاعات تکمیلی کاربران

---

### خط 1-4: Import ها
```python
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
```

**توضیح:**
- `models`: برای تعریف مدل‌های دیتابیس Django
- `User`: مدل کاربر پیش‌فرض Django
- `post_save`: سیگنال Django که بعد از ذخیره یک object اجرا می‌شود
- `receiver`: دکوراتور برای اتصال function به سیگنال

---

### خط 6-16: مدل Contact
```python
class Contact(models.Model):
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)  
    class Meta:
        ordering = ['created_date']
    def __str__(self):
        return self.name
```

**توضیح خط به خط:**

**خط 6:** `class Contact(models.Model):`
- تعریف کلاس Contact که از Model Django ارث‌بری می‌کند
- این کلاس یک جدول در دیتابیس ایجاد می‌کند

**خط 7:** `name = models.CharField(max_length=255)`
- فیلد متنی برای نام کاربر
- حداکثر 255 کاراکتر
- در دیتابیس به صورت VARCHAR ذخیره می‌شود

**خط 8:** `subject = models.CharField(max_length=255)`
- فیلد متنی برای موضوع پیام
- حداکثر 255 کاراکتر

**خط 9:** `email = models.EmailField()`
- فیلد ایمیل با اعتبارسنجی خودکار
- Django بررسی می‌کند که فرمت ایمیل صحیح باشد

**خط 10:** `message = models.TextField()`
- فیلد متنی بزرگ برای پیام
- بدون محدودیت طول (برای متن‌های طولانی)

**خط 11:** `created_date = models.DateTimeField(auto_now_add=True)`
- فیلد تاریخ و زمان
- `auto_now_add=True`: فقط هنگام ایجاد object مقدار می‌گیرد
- قابل تغییر نیست

**خط 12:** `updated_date = models.DateTimeField(auto_now=True)`
- فیلد تاریخ و زمان به‌روزرسانی
- `auto_now=True`: هر بار که object ذخیره می‌شود، به‌روز می‌شود

**خط 13-14:** `class Meta: ordering = ['created_date']`
- کلاس Meta برای تنظیمات اضافی
- `ordering`: ترتیب پیش‌فرض نمایش رکوردها
- `['created_date']`: بر اساس تاریخ ایجاد (قدیمی‌ترین اول)

**خط 15-16:** `def __str__(self): return self.name`
- متد `__str__` برای نمایش object در Django Admin و shell
- وقتی `print(contact)` یا در admin نمایش داده می‌شود، نام را نشان می‌دهد

---

### خط 18-36: مدل Profile
```python
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='profiles/', default='profiles/default.png', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True, verbose_name='بیوگرافی')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name='شماره تماس')
    location = models.CharField(max_length=100, blank=True, null=True, verbose_name='موقعیت')
    website = models.URLField(blank=True, null=True, verbose_name='وب‌سایت')
    github = models.CharField(max_length=100, blank=True, null=True, verbose_name='GitHub')
    linkedin = models.CharField(max_length=100, blank=True, null=True, verbose_name='LinkedIn')
    twitter = models.CharField(max_length=100, blank=True, null=True, verbose_name='Twitter')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'پروفایل'
        verbose_name_plural = 'پروفایل‌ها'
    
    def __str__(self):
        return f'پروفایل {self.user.username}'
```

**توضیح خط به خط:**

**خط 19:** `user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')`
- رابطه یک به یک با مدل User
- `on_delete=models.CASCADE`: اگر User حذف شود، Profile هم حذف می‌شود
- `related_name='profile'`: از User می‌توان با `user.profile` به Profile دسترسی داشت

**خط 20:** `avatar = models.ImageField(upload_to='profiles/', default='profiles/default.png', blank=True, null=True)`
- فیلد تصویر
- `upload_to='profiles/'`: فایل‌ها در پوشه media/profiles/ ذخیره می‌شوند
- `default='profiles/default.png'`: تصویر پیش‌فرض
- `blank=True`: در فرم می‌توان خالی گذاشت
- `null=True`: در دیتابیس می‌تواند NULL باشد

**خط 21:** `bio = models.TextField(max_length=500, blank=True, null=True, verbose_name='بیوگرافی')`
- فیلد متن برای بیوگرافی
- `max_length=500`: حداکثر 500 کاراکتر
- `verbose_name='بیوگرافی'`: نام فارسی در Django Admin

**خط 22-27:** فیلدهای متنی دیگر
- همه با `blank=True, null=True`: اختیاری هستند
- `verbose_name`: نام فارسی برای نمایش

**خط 28-29:** فیلدهای تاریخ (مشابه Contact)

**خط 31-33:** `class Meta:`
- `verbose_name`: نام مفرد فارسی
- `verbose_name_plural`: نام جمع فارسی

**خط 35-36:** `def __str__(self):`
- نمایش "پروفایل username" در admin

---

### خط 38-41: Signal Handler برای ایجاد Profile خودکار
```python
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
```

**توضیح:**
- `@receiver(post_save, sender=User)`: وقتی User ذخیره می‌شود، این function اجرا می‌شود
- `sender`: مدلی که signal را فرستاده (User)
- `instance`: object User که ذخیره شده
- `created`: True اگر object جدید ایجاد شده، False اگر به‌روزرسانی شده
- `if created:`: فقط برای User جدید Profile ایجاد می‌شود

---

### خط 43-47: Signal Handler برای ذخیره Profile
```python
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    if not created:
        if hasattr(instance, 'profile'):
            instance.profile.save(update_fields=[])
```

**توضیح:**
- وقتی User به‌روزرسانی می‌شود (`not created`)
- اگر Profile وجود داشته باشد (`hasattr`)
- Profile را ذخیره می‌کند

---

## 📄 فایل: views.py

### خط 1-12: Import ها
```python
import json
from pathlib import Path
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from home.forms import ContactForm, ProfileForm
from home.models import Contact, Profile
from django.http import HttpRequest
from projects.models import Projects
```

**توضیح:**
- `json`: برای خواندن فایل JSON
- `Path`: برای کار با مسیر فایل‌ها
- `messages`: سیستم پیام‌های Django
- `authenticate, login, logout`: توابع احراز هویت
- `render, redirect`: برای نمایش template و redirect
- `login_required`: دکوراتور برای نیاز به لاگین

---

### خط 14-17: تابع بارگذاری محتوا
```python
def _load_home_content():
    content_path = Path(settings.BASE_DIR) / 'home' / 'content.json'
    with content_path.open(encoding='utf-8') as source:
        return json.load(source)
```

**توضیح:**
- `_load_home_content()`: تابع private (با _ شروع می‌شود)
- `Path(settings.BASE_DIR)`: مسیر root پروژه
- `/ 'home' / 'content.json'`: مسیر فایل JSON
- `encoding='utf-8'`: برای پشتیبانی از فارسی
- `json.load(source)`: خواندن و parse کردن JSON

---

### خط 20: بارگذاری یکباره محتوا
```python
HOME_CONTENT = _load_home_content()
```

**توضیح:**
- محتوا یکبار در شروع برنامه بارگذاری می‌شود
- در حافظه نگه داشته می‌شود (performance بهتر)

---

### خط 23-28: View صفحه اصلی
```python
def home_page(request:HttpRequest):
    # دریافت پروژه‌ها از دیتابیس - ابتدا پروژه‌های ویژه، سپس بقیه
    projects = Projects.objects.all().order_by('-featured', '-created_date')[:3]  # نمایش حداکثر 3 پروژه
    form = ContactForm()
    
    return render(request, 'home.html', {'content': HOME_CONTENT,'projects':projects, 'contact_form': form})
```

**توضیح خط به خط:**

**خط 23:** `def home_page(request:HttpRequest):`
- تعریف view function
- `request`: درخواست HTTP از کاربر
- `HttpRequest`: type hint برای IDE

**خط 25:** `projects = Projects.objects.all().order_by('-featured', '-created_date')[:3]`
- `Projects.objects.all()`: دریافت همه پروژه‌ها
- `.order_by('-featured', '-created_date')`: مرتب‌سازی
  - `-featured`: پروژه‌های ویژه اول (True قبل از False)
  - `-created_date`: جدیدترین اول
- `[:3]`: فقط 3 پروژه اول (slicing)

**خط 26:** `form = ContactForm()`
- ایجاد instance خالی از فرم تماس

**خط 28:** `return render(request, 'home.html', {...})`
- `render`: ترکیب template با داده‌ها
- `'home.html'`: نام template
- `{'content': ...}`: context (داده‌های ارسالی به template)

---

### خط 30-41: View ذخیره فرم تماس
```python
def save_contact(request:HttpRequest):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # ذخیره Contact در دیتابیس (فیلد captcha به طور خودکار نادیده گرفته می‌شود چون در مدل نیست)
            contact = form.save()  # این یک instance از Contact را ذخیره می‌کند
            messages.success(request, "فرم با موفقیت ارسال شد!")
            return redirect('home:home')
        else:
            messages.error(request, "لطفاً تمام فیلدها را به درستی پر کنید و کد امنیتی را وارد نمایید.")
            return redirect('home:home')
    return redirect('home:home')
```

**توضیح خط به خط:**

**خط 31:** `if request.method == "POST":`
- بررسی اینکه درخواست POST است (ارسال فرم)

**خط 32:** `form = ContactForm(request.POST)`
- ایجاد فرم با داده‌های POST

**خط 33:** `if form.is_valid():`
- بررسی اعتبار فرم (validation)

**خط 35:** `contact = form.save()`
- ذخیره داده‌ها در دیتابیس
- یک object Contact ایجاد می‌شود

**خط 36:** `messages.success(request, "...")`
- نمایش پیام موفقیت به کاربر

**خط 37:** `return redirect('home:home')`
- هدایت به صفحه اصلی
- `'home:home'`: نام URL با namespace

**خط 38-40:** در صورت خطا
- نمایش پیام خطا
- redirect به صفحه اصلی

**خط 41:** اگر method POST نبود، redirect

---

### خط 43-62: View ورود به سیستم
```python
def login_view(request:HttpRequest):
    if request.user.is_authenticated:
        return redirect('home:home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'خوش آمدید {user.username}!')
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('home:home')
        else:
            messages.error(request, 'نام کاربری یا رمز عبور اشتباه است.')
    
    return render(request, 'login.html')
```

**توضیح خط به خط:**

**خط 44-45:** بررسی لاگین بودن
- اگر کاربر لاگین است، به صفحه اصلی redirect

**خط 47-49:** دریافت داده‌های فرم
- `request.POST.get('username')`: دریافت username از فرم
- `request.POST.get('password')`: دریافت password

**خط 51:** `user = authenticate(request, username=username, password=password)`
- بررسی صحت username و password
- اگر صحیح باشد، object User برمی‌گرداند
- در غیر این صورت None

**خط 52-58:** اگر کاربر معتبر بود
- `login(request, user)`: ایجاد session برای کاربر
- `messages.success`: پیام خوش‌آمدگویی
- `next_url`: اگر کاربر از صفحه محافظت‌شده آمده، بعد از لاگین به همان صفحه برود
- `redirect(next_url or 'home:home')`: redirect

**خط 59-60:** اگر کاربر معتبر نبود
- نمایش پیام خطا

**خط 62:** نمایش فرم لاگین (GET request)

---

### خط 65-112: View ثبت‌نام
```python
def signup_view(request:HttpRequest):
    if request.user.is_authenticated:
        return redirect('home:home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        # Validation
        if not username or not email or not password1 or not password2:
            messages.error(request, 'لطفاً تمام فیلدها را پر کنید.')
            return render(request, 'signup.html')
        
        if password1 != password2:
            messages.error(request, 'رمز عبور و تأیید رمز عبور یکسان نیستند.')
            return render(request, 'signup.html')
        
        if len(password1) < 8:
            messages.error(request, 'رمز عبور باید حداقل 8 کاراکتر باشد.')
            return render(request, 'signup.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'این نام کاربری قبلاً استفاده شده است.')
            return render(request, 'signup.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'این ایمیل قبلاً استفاده شده است.')
            return render(request, 'signup.html')
        
        # Create user
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1
            )
            messages.success(request, f'حساب کاربری {username} با موفقیت ایجاد شد! اکنون می‌توانید وارد شوید.')
            return redirect('home:login')
        except Exception as e:
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"Error creating user: {e}")
            messages.error(request, 'خطا در ایجاد حساب کاربری. لطفاً دوباره تلاش کنید.')
            return render(request, 'signup.html')
    
    return render(request, 'signup.html')
```

**توضیح خط به خط:**

**خط 66-67:** بررسی لاگین بودن (مشابه login_view)

**خط 69-72:** دریافت داده‌های فرم

**خط 75-78:** Validation: بررسی پر بودن همه فیلدها

**خط 80-82:** Validation: بررسی یکسان بودن رمزها

**خط 84-86:** Validation: بررسی حداقل 8 کاراکتر

**خط 88-90:** Validation: بررسی تکراری نبودن username

**خط 92-94:** Validation: بررسی تکراری نبودن email

**خط 97-102:** ایجاد کاربر
- `User.objects.create_user()`: ایجاد کاربر با hash کردن password
- `messages.success`: پیام موفقیت
- `redirect('home:login')`: هدایت به صفحه لاگین

**خط 103-108:** مدیریت خطا
- `try-except`: در صورت خطا
- `logging`: ثبت خطا در log
- نمایش پیام خطا به کاربر

---

### خط 114-135: View پروفایل
```python
@login_required
def profile_view(request:HttpRequest):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'پروفایل شما با موفقیت به‌روزرسانی شد!')
            return redirect('home:profile')
    else:
        form = ProfileForm(instance=profile)
    
    context = {
        'profile': profile,
        'form': form,
        'user': request.user,
    }
    return render(request, 'profile.html', context)
```

**توضیح خط به خط:**

**خط 114:** `@login_required`
- دکوراتور: فقط کاربران لاگین‌شده می‌توانند دسترسی داشته باشند
- اگر لاگین نباشد، به صفحه لاگین redirect می‌شود

**خط 116-119:** دریافت یا ایجاد Profile
- `try-except`: اگر Profile وجود نداشت، ایجاد می‌شود

**خط 121-126:** اگر POST request
- `ProfileForm(request.POST, request.FILES, ...)`: فرم با داده‌های POST و فایل‌ها
- `instance=profile`: فرم با داده‌های موجود پر می‌شود
- `form.save()`: ذخیره تغییرات

**خط 127-128:** اگر GET request
- فرم خالی با داده‌های Profile

**خط 130-134:** ایجاد context و render

---

### خط 137-141: View خروج از سیستم
```python
@login_required
def logout_view(request:HttpRequest):
    logout(request)
    messages.success(request, 'شما با موفقیت از حساب کاربری خود خارج شدید.')
    return redirect('home:home')
```

**توضیح:**
- `logout(request)`: پاک کردن session کاربر
- نمایش پیام و redirect به صفحه اصلی

---

## 📄 فایل: urls.py

```python
from django.urls import path
from home.views import home_page,save_contact,login_view,signup_view,profile_view,logout_view

app_name='home'

urlpatterns = [
    path('', home_page, name="home"),
    path('contact/',save_contact,name="save_contact"),
    path('login/',login_view,name="login"),
    path('signup/',signup_view,name="signup"),
    path('profile/',profile_view,name="profile"),
    path('logout/',logout_view,name="logout")
]
```

**توضیح خط به خط:**

**خط 1-2:** Import ها
- `path`: برای تعریف URL pattern
- Import کردن view functions

**خط 4:** `app_name='home'`
- تعریف namespace برای این app
- در template: `{% url 'home:home' %}`

**خط 6-13:** `urlpatterns`
- لیست URL patterns

**خط 7:** `path('', home_page, name="home")`
- URL: `/` (صفحه اصلی)
- View: `home_page`
- Name: `'home'` (برای استفاده در template)

**خط 8:** `path('contact/',save_contact,name="save_contact")`
- URL: `/contact/`
- View: `save_contact`

**خط 9-12:** سایر URL ها به همین ترتیب

---

## 📄 فایل: forms.py

```python
from django.forms import ModelForm
from captcha.fields import CaptchaField
from home.models import Contact, Profile

class ContactForm(ModelForm):
    captcha = CaptchaField(label='کد امنیتی')
    
    class Meta:
        model = Contact
        fields = "__all__"

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'phone', 'location', 'website', 'github', 'linkedin', 'twitter']
        labels = {
            'avatar': 'آواتار',
            'bio': 'بیوگرافی',
            'phone': 'شماره تماس',
            'location': 'موقعیت',
            'website': 'وب‌سایت',
            'github': 'GitHub',
            'linkedin': 'LinkedIn',
            'twitter': 'Twitter',
        }
```

**توضیح:**

**خط 1-3:** Import ها
- `ModelForm`: فرم بر اساس Model
- `CaptchaField`: فیلد کپچا
- Import مدل‌ها

**خط 5-10:** ContactForm
- `captcha = CaptchaField(...)`: اضافه کردن فیلد کپچا
- `fields = "__all__"`: همه فیلدهای مدل Contact

**خط 12-25:** ProfileForm
- `fields = [...]`: فقط فیلدهای مشخص شده
- `labels`: نام فارسی برای فیلدها

---

## 📄 فایل: admin.py

```python
from django.contrib import admin
from home.models import Contact, Profile

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('name','email','created_date')
    list_filter = ('email',)
    search_fields = ('name','message')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'location', 'created_date')
    search_fields = ('user__username', 'phone', 'location')
    list_filter = ('created_date',)
    readonly_fields = ('created_date', 'updated_date')
```

**توضیح:**

**خط 4:** `@admin.register(Contact)`
- ثبت مدل Contact در Django Admin

**خط 5-9:** تنظیمات ContactAdmin
- `date_hierarchy`: فیلتر بر اساس تاریخ در بالای صفحه
- `list_display`: ستون‌های نمایش در لیست
- `list_filter`: فیلتر در سایدبار
- `search_fields`: فیلدهای قابل جستجو

**خط 11-16:** تنظیمات ProfileAdmin (مشابه)

---

## 📄 فایل: content.json

این فایل شامل محتوای استاتیک صفحه اصلی است (hero section, about, skills, etc.)

**ساختار کلی:**
```json
{
  "hero": { ... },
  "about": { ... },
  "education": { ... },
  "languages": { ... },
  "skills": { ... },
  "contact": { ... }
}
```

این محتوا در `views.py` با تابع `_load_home_content()` بارگذاری می‌شود.

---

## 🔄 جریان کار (Flow)

### 1. صفحه اصلی (Home)
```
User → / → home_page() → home.html
```

### 2. ارسال فرم تماس
```
User → POST /contact/ → save_contact() → Validation → Save DB → Redirect
```

### 3. ورود به سیستم
```
User → /login/ → login_view() → authenticate() → login() → Redirect
```

### 4. ثبت‌نام
```
User → /signup/ → signup_view() → Validation → create_user() → Redirect
```

### 5. پروفایل
```
User → /profile/ → profile_view() → GET: نمایش فرم | POST: ذخیره
```

---

## 📝 نکات مهم

1. **Signals**: Profile به صورت خودکار برای هر User جدید ایجاد می‌شود
2. **Messages**: برای نمایش پیام‌ها به کاربر استفاده می‌شود
3. **Authentication**: از سیستم احراز هویت Django استفاده می‌شود
4. **File Upload**: برای آواتار در Profile استفاده می‌شود
5. **Captcha**: برای جلوگیری از spam در فرم تماس

---

## 🎯 خلاصه

این app شامل:
- ✅ صفحه اصلی با محتوای داینامیک
- ✅ فرم تماس با کپچا
- ✅ سیستم احراز هویت (لاگین/ثبت‌نام)
- ✅ مدیریت پروفایل کاربر
- ✅ نمایش پروژه‌ها در صفحه اصلی

