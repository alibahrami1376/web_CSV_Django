# 📚 مستندات کامل پروژه Django Portfolio

## 📖 فهرست مطالب

این پوشه شامل مستندات کامل و خط به خط تمام بخش‌های پروژه است.

### 📄 فایل‌های مستندات

1. **[01_HOME_APP.md](./01_HOME_APP.md)**
   - مستندات کامل App: HOME
   - شامل: Models, Views, URLs, Forms, Admin
   - توضیح خط به خط تمام کدها
   - جریان کار (Flow)
   - نکات مهم

2. **[02_BLOG_APP.md](./02_BLOG_APP.md)**
   - مستندات کامل App: BLOG
   - شامل: Models (Post, Category, Newsletter)
   - Views (blog_home, blog_detail, blog_search)
   - Pagination
   - Custom Template Tags
   - جستجو و فیلتر

3. **[03_PROJECTS_APP.md](./03_PROJECTS_APP.md)**
   - مستندات کامل App: PROJECTS
   - شامل: Models (Projects, Category)
   - Views (projects_list, project_detail)
   - فیلتر پیشرفته
   - مرتب‌سازی
   - Session-based View Counter

4. **[04_WEBSITE_CONFIG.md](./04_WEBSITE_CONFIG.md)**
   - مستندات کامل: WEBSITE CONFIGURATION
   - شامل: settings.py (خط به خط)
   - urls.py (URL routing)
   - wsgi.py / asgi.py
   - Static & Media Files
   - Security Settings

5. **[05_TEMPLATES.md](./05_TEMPLATES.md)**
   - مستندات کامل: TEMPLATES
   - شامل: base.html
   - home.html
   - Template Tags & Filters
   - Dynamic Content
   - Form Handling

---

## 🎯 نحوه استفاده

### برای یادگیری
1. از فایل **01_HOME_APP.md** شروع کنید
2. سپس **04_WEBSITE_CONFIG.md** را بخوانید (برای درک کلی)
3. بعد **02_BLOG_APP.md** و **03_PROJECTS_APP.md**
4. در نهایت **05_TEMPLATES.md** برای درک frontend

### برای مرجع
- هر فایل به صورت مستقل قابل استفاده است
- می‌توانید مستقیماً به بخش مورد نظر بروید
- تمام کدها خط به خط توضیح داده شده‌اند

---

## 📋 ساختار پروژه

```
web_CSV_Django/
├── home/              # App صفحه اصلی
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── admin.py
├── blog/              # App وبلاگ
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templatetags/
├── projects/          # App پروژه‌ها
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── website/           # تنظیمات اصلی
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── templates/         # Template ها
│   ├── base.html
│   ├── home.html
│   └── ...
└── DOC/               # مستندات (این پوشه)
    ├── README.md
    ├── 01_HOME_APP.md
    ├── 02_BLOG_APP.md
    ├── 03_PROJECTS_APP.md
    ├── 04_WEBSITE_CONFIG.md
    └── 05_TEMPLATES.md
```

---

## 🔍 جستجوی سریع

### Models
- **Contact**: [01_HOME_APP.md#مدل-contact](./01_HOME_APP.md#خط-6-16-مدل-contact)
- **Profile**: [01_HOME_APP.md#مدل-profile](./01_HOME_APP.md#خط-18-36-مدل-profile)
- **Post**: [02_BLOG_APP.md#مدل-post](./02_BLOG_APP.md#خط-10-27-مدل-post)
- **Projects**: [03_PROJECTS_APP.md#مدل-projects](./03_PROJECTS_APP.md#خط-18-66-مدل-projects)

### Views
- **home_page**: [01_HOME_APP.md#view-صفحه-اصلی](./01_HOME_APP.md#خط-23-28-view-صفحه-اصلی)
- **blog_home**: [02_BLOG_APP.md#view-صفحه-اصلی-وبلاگ](./02_BLOG_APP.md#خط-11-29-view-صفحه-اصلی-وبلاگ)
- **projects_list**: [03_PROJECTS_APP.md#view-لیست-پروژه‌ها](./03_PROJECTS_APP.md#خط-7-82-view-لیست-پروژه‌ها)

### Settings
- **SECRET_KEY**: [04_WEBSITE_CONFIG.md#secret_key](./04_WEBSITE_CONFIG.md#خط-23-24-secret_key)
- **DATABASES**: [04_WEBSITE_CONFIG.md#databases](./04_WEBSITE_CONFIG.md#خط-85-93-databases)
- **STATIC_FILES**: [04_WEBSITE_CONFIG.md#static--media-files](./04_WEBSITE_CONFIG.md#خط-127-137-static--media-files)

### Templates
- **base.html**: [05_TEMPLATES.md#فایل-basehtml](./05_TEMPLATES.md#-فایل-basehtml)
- **home.html**: [05_TEMPLATES.md#فایل-homehtml](./05_TEMPLATES.md#-فایل-homehtml)

---

## 💡 نکات مهم

### برای مبتدیان
1. ابتدا Django basics را یاد بگیرید
2. سپس Models را مطالعه کنید
3. بعد Views و URLs
4. در نهایت Templates

### برای حرفه‌ای‌ها
- مستندات به عنوان مرجع استفاده کنید
- کدها به صورت کامل توضیح داده شده‌اند
- می‌توانید مستقیماً به بخش مورد نظر بروید

---

## 🛠️ تکنولوژی‌های استفاده شده

- **Django 5.2.8**: Framework اصلی
- **SQLite**: دیتابیس (development)
- **Django Simple Captcha**: کپچا
- **Feather Icons**: آیکون‌ها
- **Custom Web Components**: Header & Footer

---

## 📝 توضیحات

### چرا این مستندات؟
- **یادگیری**: برای درک کامل پروژه
- **مرجع**: برای استفاده سریع
- **نگهداری**: برای به‌روزرسانی و توسعه

### چه چیزی در مستندات است؟
- ✅ توضیح خط به خط تمام کدها
- ✅ توضیح پارامترها و متغیرها
- ✅ جریان کار (Flow)
- ✅ نکات مهم و best practices
- ✅ مثال‌های عملی

---

## 🔗 لینک‌های مفید

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Models](https://docs.djangoproject.com/en/5.2/topics/db/models/)
- [Django Views](https://docs.djangoproject.com/en/5.2/topics/http/views/)
- [Django Templates](https://docs.djangoproject.com/en/5.2/topics/templates/)

---

## 📞 پشتیبانی

اگر سوالی دارید یا مشکلی پیش آمد:
1. مستندات را دوباره بررسی کنید
2. کدهای مربوطه را در فایل‌های اصلی چک کنید
3. از Django documentation استفاده کنید

---

**آخرین به‌روزرسانی**: 2025-11-24

**نسخه**: 1.0

