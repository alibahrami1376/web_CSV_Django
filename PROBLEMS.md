# مشکلات Deployment برای هاست

## 🔴 مشکلات امنیتی (Critical)

### 1. SECRET_KEY
- **مشکل**: SECRET_KEY با یک مقدار default در کد قرار دارد که امن نیست
- **راه حل**: باید یک SECRET_KEY جدید و قوی تولید کنید و در فایل `.env` قرار دهید
- **دستور**: `python manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`

### 2. ALLOWED_HOSTS
- **مشکل**: ALLOWED_HOSTS خالی است و باید دامنه هاست شما را شامل شود
- **راه حل**: در فایل `.env` اضافه کنید: `ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com`

### 3. DEBUG Mode
- **مشکل**: باید در production حتماً `DEBUG=False` باشد
- **راه حل**: در فایل `.env` اضافه کنید: `DEBUG=False`

### 4. Security Headers
- **مشکل**: تنظیمات امنیتی SSL و HSTS تنظیم نشده
- **راه حل**: در `settings.py` اضافه کنید:
```python
# فقط در production (وقتی DEBUG=False)
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
```

## 🟡 مشکلات Database

### 5. SQLite برای Production
- **مشکل**: SQLite برای production مناسب نیست (مشکلات همزمانی، backup، performance)
- **راه حل**: استفاده از PostgreSQL یا MySQL
- **مثال برای PostgreSQL**:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}
```

## 🟡 مشکلات Static و Media Files

### 6. Static Files Configuration
- **مشکل**: در production باید static files توسط web server (Nginx/Apache) serve شود نه Django
- **راه حل**: 
  - اجرای `python manage.py collectstatic` برای جمع‌آوری فایل‌های static
  - تنظیم Nginx/Apache برای serve کردن از `STATIC_ROOT`
  - حذف کد serve کردن static از `urls.py` (قبلاً انجام شده)

### 7. Media Files
- **مشکل**: Media files باید توسط web server serve شود
- **راه حل**: تنظیم Nginx/Apache برای serve کردن از `MEDIA_ROOT`

## 🟡 مشکلات تنظیمات

### 8. TIME_ZONE
- **مشکل**: TIME_ZONE روی UTC است
- **راه حل**: تغییر به `TIME_ZONE = 'Asia/Tehran'`

### 9. LANGUAGE_CODE
- **مشکل**: LANGUAGE_CODE روی `en-us` است
- **راه حل**: تغییر به `LANGUAGE_CODE = 'fa-ir'`

## 🟡 فایل‌های مفقود

### 10. requirements.txt
- **مشکل**: فایل `requirements.txt` وجود ندارد
- **راه حل**: ایجاد کنید با دستور: `pip freeze > requirements.txt`
- **محتوای پیشنهادی**:
```
Django==5.2.8
django-simple-captcha==0.6.2
django-multi-captcha-admin==2.0.0
python-decouple==3.8
Pillow==12.0.0
```

### 11. فایل .env
- **مشکل**: فایل `.env` وجود ندارد
- **راه حل**: ایجاد فایل `.env` در root پروژه با محتوای:
```
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
```

### 12. .env.example
- **مشکل**: فایل `.env.example` برای راهنمایی وجود ندارد
- **راه حل**: ایجاد فایل `.env.example` با ساختار فایل `.env` (بدون مقادیر حساس)

### 13. .gitignore
- **مشکل**: باید `.env` و `db.sqlite3` در `.gitignore` باشند
- **راه حل**: بررسی کنید که این فایل‌ها ignore شده‌اند

## 🟡 مشکلات Performance

### 14. Static Files Caching
- **مشکل**: باید cache headers برای static files تنظیم شود
- **راه حل**: در تنظیمات Nginx/Apache اضافه کنید

### 15. Database Connection Pooling
- **مشکل**: برای performance بهتر باید connection pooling استفاده شود
- **راه حل**: استفاده از `django-db-connection-pool` یا تنظیمات database server

## 🟡 مشکلات Logging

### 16. Logging Configuration
- **مشکل**: تنظیمات logging برای production وجود ندارد
- **راه حل**: در `settings.py` اضافه کنید:
```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs' / 'django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}
```

## 🟡 مشکلات دیگر

### 17. Admin URL
- **مشکل**: URL admin باید تغییر کند (امنیت بهتر)
- **راه حل**: در `urls.py` تغییر دهید: `path('your-secret-admin-url/', admin.site.urls)`

### 18. Email Configuration
- **مشکل**: اگر از email استفاده می‌کنید، باید تنظیمات email برای production اضافه شود
- **راه حل**: در `settings.py` اضافه کنید:
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
```

### 19. Backup Strategy
- **مشکل**: استراتژی backup برای database و media files وجود ندارد
- **راه حل**: تنظیم backup خودکار (cron job)

### 20. Monitoring
- **مشکل**: سیستم monitoring برای خطاها وجود ندارد
- **راه حل**: استفاده از Sentry یا ابزارهای مشابه

## ✅ چک‌لیست قبل از Deployment

- [ ] SECRET_KEY جدید تولید و در `.env` قرار گرفته
- [ ] DEBUG=False تنظیم شده
- [ ] ALLOWED_HOSTS شامل دامنه هاست شده
- [ ] Security headers اضافه شده
- [ ] Database به PostgreSQL/MySQL تغییر کرده
- [ ] requirements.txt ایجاد شده
- [ ] فایل `.env` ایجاد و تنظیم شده
- [ ] `python manage.py collectstatic` اجرا شده
- [ ] TIME_ZONE و LANGUAGE_CODE تنظیم شده
- [ ] Logging configuration اضافه شده
- [ ] Web server (Nginx/Apache) برای static/media تنظیم شده
- [ ] Backup strategy تنظیم شده
- [ ] تست کامل در محیط staging انجام شده

## 📝 نکات مهم

1. **هرگز** فایل `.env` را در Git commit نکنید
2. **هرگز** `db.sqlite3` را در Git commit نکنید
3. قبل از deployment حتماً تست کنید
4. از HTTPS استفاده کنید
5. فایل‌های حساس را در `.gitignore` قرار دهید

