# مستندات کامل: TEMPLATES

## 📁 ساختار Templates
```
templates/
├── base.html              # Template اصلی (base)
├── home.html              # صفحه اصلی
├── login.html             # صفحه ورود
├── signup.html            # صفحه ثبت‌نام
├── profile.html           # صفحه پروفایل
├── blog/
│   ├── blog_home.html
│   ├── blog_detail.html
│   ├── blog_category_sidebar.html
│   └── latest_posts.html
└── projects/
    ├── projects_list.html
    └── project_detail.html
```

---

## 📄 فایل: base.html

### خط 1: Load Static
```django
{% load static %}
```

**توضیح:**
- بارگذاری template tag `static`
- برای دسترسی به فایل‌های static
- استفاده: `{% static 'css/style.css' %}`

---

### خط 2-3: HTML Declaration
```html
<!DOCTYPE html>
<html lang="fa" dir="rtl">
```

**توضیح:**
- `lang="fa"`: زبان فارسی
- `dir="rtl"`: راست به چپ (Right-to-Left)

---

### خط 4-7: Head Section
```html
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Ali Bahrami</title>
```

**توضیح:**
- `charset="UTF-8"`: پشتیبانی از کاراکترهای فارسی
- `viewport`: responsive design
- `title`: عنوان صفحه

---

### خط 8: CSS
```html
<link rel="stylesheet" href="{% static 'css/portfolio-style.css' %}" />
```

**توضیح:**
- `{% static 'css/portfolio-style.css' %}`: مسیر فایل CSS
- Django مسیر را به `/static/css/portfolio-style.css` تبدیل می‌کند

---

### خط 10-40: Feather Icons Script
```html
<script src="https://cdn.jsdelivr.net/npm/feather-icons/dist/feather.min.js"></script>
<script>
  // Fallback در صورت عدم لود شدن feather از CDN اصلی
  (function() {
    function loadFeatherFallback() {
      if (typeof feather === 'undefined') {
        console.warn('Feather icons از CDN لود نشد. تلاش برای استفاده از CDN جایگزین...');
        var script = document.createElement('script');
        script.src = 'https://unpkg.com/feather-icons';
        script.onerror = function() {
          console.warn('Feather icons از هیچ CDN لود نشد. آیکون‌ها ممکن است نمایش داده نشوند.');
        };
        script.onload = function() {
          if (typeof feather !== 'undefined') {
            feather.replace();
          }
        };
        document.head.appendChild(script);
      }
    }
    
    // بررسی بعد از لود شدن صفحه
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', function() {
        setTimeout(loadFeatherFallback, 500);
      });
    } else {
      setTimeout(loadFeatherFallback, 500);
    }
  })();
</script>
```

**توضیح خط به خط:**

**خط 10:** بارگذاری Feather Icons از CDN

**خط 14:** `loadFeatherFallback()`: تابع fallback
- اگر feather لود نشد، از CDN جایگزین استفاده می‌کند

**خط 15:** `if (typeof feather === 'undefined')`
- بررسی وجود feather

**خط 17-18:** ایجاد script tag جدید
- `document.createElement('script')`: ایجاد element
- `script.src = '...'`: تنظیم URL

**خط 19-21:** `script.onerror`
- اگر CDN جایگزین هم لود نشد، warning

**خط 22-25:** `script.onload`
- اگر لود شد، `feather.replace()` را اجرا می‌کند

**خط 27:** `document.head.appendChild(script)`
- اضافه کردن script به head

**خط 32-38:** بررسی readyState
- اگر صفحه در حال لود است، منتظر می‌ماند
- سپس fallback را اجرا می‌کند

---

### خط 43-56: Body Section
```html
<body class="dark-theme">
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
  {% endif %} {%block content %} {% endblock %}
```

**توضیح خط به خط:**

**خط 43:** `class="dark-theme"`
- کلاس برای تم تاریک

**خط 44:** `{% if user.is_authenticated %}`
- بررسی لاگین بودن کاربر
- `user`: از context processor

**خط 45:** `{% if user.profile %}`
- بررسی وجود profile

**خط 46-50:** Header با avatar
- `data-is-auth="true"`: کاربر لاگین است
- `data-avatar="..."`: مسیر avatar
- `{% if user.profile.avatar %}`: بررسی وجود avatar
- `{{ user.profile.avatar.url }}`: URL تصویر
- `data-profile-url="{% url 'home:profile' %}"`: لینک پروفایل
- `{% url 'home:profile' %}`: ساخت URL از name

**خط 52:** Header بدون avatar
- اگر profile وجود نداشت

**خط 54:** Header برای کاربر غیر لاگین
- `data-is-auth="false"`

**خط 56:** `{%block content %} {% endblock %}`
- Block برای محتوای صفحات دیگر
- صفحات دیگر با `{% extends 'base.html' %}` این block را پر می‌کنند

---

### خط 57-72: Footer & Scripts
```html
<portfolio-footer></portfolio-footer>
<script src="{% static 'js/header.js'%}"></script>
<script src="{% static 'js/footer.js'%}"></script>
<script src="{% static 'js/portfolio-script.js'%}"></script>
<script>
  // صبر کردن تا feather لود شود
  function initFeather() {
    if (typeof feather !== 'undefined') {
      feather.replace();
    } else {
      // اگر feather هنوز لود نشده، دوباره تلاش کن
      setTimeout(initFeather, 100);
    }
  }
  initFeather();
</script>
```

**توضیح:**
- `portfolio-footer`: Custom element برای footer
- Script های JavaScript
- `initFeather()`: تابع برای initialize کردن feather icons
- `feather.replace()`: جایگزینی `data-feather` با SVG

---

## 📄 فایل: home.html

### خط 1: Extend Base
```django
{% extends 'base.html' %} {% block content %}
```

**توضیح:**
- `{% extends 'base.html' %}`: ارث‌بری از base.html
- `{% block content %}`: شروع block content

---

### خط 3-30: Hero Section
```django
<main>
  <!-- Home Section -->
  <section id="home" class="hero-section">
    <div class="hero-content">
      <div class="profile-image-container">
        <img
          src="{{ content.hero.profile_image }}"
          alt="Profile Picture"
          class="profile-image"
        />
      </div>
      <h1 class="hero-title">{{ content.hero.title }}</h1>
      <div class="hero-subtitle">
        {% for role in content.hero.roles %}
        <span>{{ role }}</span>
        {% if not forloop.last %}
        <span class="separator">|</span>
        {% endif %} {% endfor %}
      </div>
      <div class="hero-buttons">
        {% for button in content.hero.buttons %}
        <a href="{{ button.href }}" class="btn btn-{{ button.variant }}"
          >{{ button.label }}</a
        >
        {% endfor %}
      </div>
    </div>
  </section>
```

**توضیح خط به خط:**

**خط 8-9:** `src="{{ content.hero.profile_image }}"`
- نمایش تصویر از content.json
- `{{ }}`: نمایش متغیر

**خط 14:** `{{ content.hero.title }}`
- نمایش عنوان

**خط 16-20:** Loop برای roles
- `{% for role in content.hero.roles %}`: loop
- `{{ role }}`: نمایش هر role
- `{% if not forloop.last %}`: اگر آخرین نیست
- `forloop.last`: متغیر Django برای آخرین iteration
- نمایش separator بین roles

**خط 23-27:** Loop برای buttons
- `{% for button in content.hero.buttons %}`
- `href="{{ button.href }}"`: لینک دکمه
- `class="btn btn-{{ button.variant }}"`: کلاس دینامیک
- `{{ button.label }}`: متن دکمه

---

### خط 32-44: About Section
```django
<!-- About / Biography Section -->
<section id="about" class="section">
  <div class="container">
    <h2 class="section-title">{{ content.about.title }}</h2>
    <div class="about-content">
      <div class="about-text">
        {% for paragraph in content.about.paragraphs %}
        <p>{{ paragraph }}</p>
        {% endfor %}
      </div>
    </div>
  </div>
</section>
```

**توضیح:**
- نمایش عنوان
- Loop برای paragraphs
- هر paragraph در یک `<p>` tag

---

### خط 46-66: Education Section
```django
<!-- Education Section -->
<section id="education" class="section">
  <div class="container">
    <h2 class="section-title">{{ content.education.title }}</h2>
    <div class="education-timeline">
      {% for item in content.education.items %}
      <div class="education-item">
        <div class="education-icon">
          <i data-feather="{{ item.icon }}"></i>
        </div>
        <div class="education-content">
          <h3>{{ item.title }}</h3>
          <p class="education-institution">{{ item.institution }}</p>
          <p class="education-period">{{ item.period }}</p>
          <p class="education-description">{{ item.description }}</p>
        </div>
      </div>
      {% endfor %}
    </div>
  </div>
</section>
```

**توضیح:**
- Loop برای education items
- `data-feather="{{ item.icon }}"`: آیکون feather
- نمایش title, institution, period, description

---

### خط 68-135: Languages Section
```django
<!-- Languages Section -->
<section id="languages" class="section">
  <div class="container">
    <h2 class="section-title">{{ content.languages.title }}</h2>
    <div class="languages-grid">
      {% for language in content.languages.items %}
      <div class="language-item" data-language-index="{{ forloop.counter0 }}" data-writing="{{ language.writing }}" data-speaking="{{ language.speaking }}" data-listening="{{ language.listening }}">
        <div class="language-header">
          <div class="language-name">
            <i data-feather="globe"></i>
            <span>{{ language.name }}</span>
          </div>
          <div class="language-level">
            <span class="level-text">{{ language.level_text }}</span>
            <div class="level-bar">
              <div
                class="level-fill"
                style="width: {{ language.proficiency }}%"
              ></div>
            </div>
          </div>
          <div class="language-toggle">
            <i data-feather="chevron-down" class="toggle-icon"></i>
          </div>
        </div>
        <div class="language-details">
          <div class="language-skill">
            <div class="skill-header">
              <span class="skill-label">
                <i data-feather="edit-3"></i>
                نوشتن (Writing)
              </span>
              <span class="skill-percentage">{{ language.writing }}%</span>
            </div>
            <div class="skill-bar">
              <div class="skill-fill" data-width="{{ language.writing }}" style="width: 0%"></div>
            </div>
          </div>
          <!-- Similar for speaking and listening -->
        </div>
      </div>
      {% endfor %}
    </div>
  </div>
</section>
```

**توضیح خط به خط:**

**خط 74:** `data-language-index="{{ forloop.counter0 }}"`
- Index زبان (0-based)
- `forloop.counter0`: شمارنده از 0

**خط 74:** `data-writing="{{ language.writing }}"`
- داده‌های مهارت برای JavaScript

**خط 85:** `style="width: {{ language.proficiency }}%"`
- عرض progress bar
- `{{ }}`: مقدار دینامیک

**خط 100:** `data-width="{{ language.writing }}"`
- داده برای JavaScript animation

---

### خط 137-156: Skills Section
```django
<!-- Skills Section -->
<section id="skills" class="section">
  <div class="container">
    <h2 class="section-title">{{ content.skills.title }}</h2>
    <div class="skills-grid">
      {% for skill in content.skills.items %}
      <div class="skill-card">
        <i data-feather="{{ skill.icon }}"></i>
        <h3>{{ skill.title }}</h3>
        <p>{{ skill.description }}</p>
        <div class="skill-tags">
          {% for tag in skill.tags %}
          <span>{{ tag }}</span>
          {% endfor %}
        </div>
      </div>
      {% endfor %}
    </div>
  </div>
</section>
```

**توضیح:**
- Loop برای skills
- نمایش icon, title, description
- Loop برای tags

---

### خط 158-225: Projects Section
```django
<!-- Projects Section -->
<section id="projects" class="section">
  <div class="container">
    <h2 class="section-title">پروژه ها</h2>
    <div class="projects-grid">
      {% for project in projects %}
      <div class="project-card">
        <div class="project-image">
          {% if project.image %}
          <img src="{{ project.image.url }}" alt="{{ project.title }}" />
          {% else %}
          <div class="project-image-placeholder">
            <i data-feather="image"></i>
          </div>
          {% endif %}
          {% if project.featured %}
          <div class="project-featured">
            <i data-feather="star"></i>
            <span>ویژه</span>
          </div>
          {% endif %}
          <div class="project-status project-status-{{ project.status }}">
            <i data-feather="{% if project.status == 'completed' %}check-circle{% elif project.status == 'in_progress' %}clock{% else %}pause-circle{% endif %}"></i>
            <span>{{ project.get_status_display }}</span>
          </div>
        </div>
        <div class="project-content">
          <h3>{{ project.title }}</h3>
          <p>{{ project.description }}</p>
          <div class="project-tags">
            {% for cat in project.category.all %}
            <span>{{ cat.name }}</span>
            {% endfor %}
          </div>
          <div class="project-links">
            {% if project.website_url %}
            <a href="{{ project.website_url }}" class="project-link project-link-demo" target="_blank" rel="noopener noreferrer">
              مشاهده وب‌سایت
              <i data-feather="arrow-left"></i>
            </a>
            {% endif %}
            <!-- Similar for github_url and demo_url -->
          </div>
        </div>
      </div>
      {% empty %}
      <p style="text-align: center; grid-column: 1 / -1; padding: 2rem; color: var(--text-secondary-color);">هیچ پروژه‌ای یافت نشد.</p>
      {% endfor %}
    </div>
  </div>
</section>
```

**توضیح خط به خط:**

**خط 163:** `{% for project in projects %}`
- Loop برای پروژه‌ها از view

**خط 165-171:** تصویر پروژه
- `{% if project.image %}`: بررسی وجود تصویر
- `{{ project.image.url }}`: URL تصویر
- `{% else %}`: placeholder اگر تصویر نبود

**خط 172-176:** پروژه ویژه
- `{% if project.featured %}`: بررسی featured بودن

**خط 177-181:** وضعیت پروژه
- `project-status-{{ project.status }}`: کلاس دینامیک
- `{% if project.status == 'completed' %}...{% elif %}...{% endif %}`: شرط برای آیکون
- `{{ project.get_status_display }}`: نمایش فارسی وضعیت

**خط 188-191:** دسته‌بندی‌ها
- `{% for cat in project.category.all %}`
- `.all()`: همه دسته‌بندی‌های ManyToMany

**خط 193-204:** لینک‌ها
- `{% if project.website_url %}`: بررسی وجود لینک
- `target="_blank"`: باز کردن در تب جدید
- `rel="noopener noreferrer"`: امنیت

**خط 205-206:** `{% empty %}`
- اگر projects خالی بود، این پیام نمایش داده می‌شود

---

### خط 227-278: Contact Section
```django
<!-- Contact Section -->
<section id="contact" class="section">
  <div class="container">
    <h2 class="section-title">{{ content.contact.title }}</h2>
    
    <!-- نمایش پیام‌های Django messages -->
    {% if messages %}
      <div class="messages-container">
        {% for message in messages %}
          <div class="alert alert-{{ message.tags }}">
            {{ message }}
          </div>
        {% endfor %}
      </div>
    {% endif %}
    
    <div class="contact-content">
      <div class="contact-info">
        <h3>{{ content.contact.intro_title }}</h3>
        <p>{{ content.contact.intro_text }}</p>
        <div class="contact-details">
          {% for detail in content.contact.details %}
          <div class="contact-item">
            <i data-feather="{{ detail.icon }}"></i>
            <div>
              <strong>{{ detail.label }}</strong>
              <span>{{ detail.value }}</span>
            </div>
          </div>
          {% endfor %}
        </div>
      </div>
      <form class="contact-form" id="contactForm" method="POST" action="{% url 'home:save_contact' %}">
        {% csrf_token %}
        
        {% for field in content.contact.form.fields %}
        <div class="form-group">
          <label for="{{ field.id }}">{{ field.label }}</label>
          {% if field.type == 'textarea' %}
          <textarea
            id="{{ field.id }}"
            name="{{ field.id }}"
            required
          ></textarea>
          {% else %}
          <input
            type="{{ field.type }}"
            id="{{ field.id }}"
            name="{{ field.id }}"
            required
          />
          {% endif %}
        </div>
        {% endfor %}
        
        <button type="button" id="submitBtn" class="btn btn-primary" onclick="handleSubmitClick(event)">
          {{ content.contact.form.submit_label }}
        </button>
      </form>
    </div>
  </div>
</section>
```

**توضیح خط به خط:**

**خط 233-239:** نمایش پیام‌ها
- `{% if messages %}`: بررسی وجود پیام
- `{% for message in messages %}`: loop برای پیام‌ها
- `alert-{{ message.tags }}`: کلاس دینامیک (success, error, etc.)
- `{{ message }}`: متن پیام

**خط 247-254:** اطلاعات تماس
- Loop برای details از content.json

**خط 255:** فرم تماس
- `method="POST"`: ارسال POST
- `action="{% url 'home:save_contact' %}"`: URL action
- `{% csrf_token %}`: CSRF token (اجباری برای POST)

**خط 257-273:** فیلدهای فرم
- Loop برای fields از content.json
- `{% if field.type == 'textarea' %}`: شرط برای textarea
- `name="{{ field.id }}"`: name فیلد (باید با model field مطابقت داشته باشد)

**خط 275:** دکمه ارسال
- `type="button"`: جلوگیری از submit خودکار
- `onclick="handleSubmitClick(event)"`: JavaScript handler

---

### خط 281-306: Captcha Modal
```django
<!-- مودال کپچا -->
<div id="captchaModal" class="captcha-modal" style="display: none;">
  <div class="captcha-modal-overlay"></div>
  <div class="captcha-modal-content">
    <div class="captcha-modal-header">
      <h3>تأیید امنیتی</h3>
      <button type="button" class="captcha-modal-close" id="closeCaptchaModal">
        <i data-feather="x"></i>
      </button>
    </div>
    <div class="captcha-modal-body">
      <p>لطفاً کد امنیتی زیر را وارد کنید:</p>
      <div id="captchaFieldContainer">
        {% if contact_form %}
        {{ contact_form.captcha }}
        {% else %}
        <p style="color: red;">خطا: فرم کپچا یافت نشد. لطفاً صفحه را رفرش کنید.</p>
        {% endif %}
      </div>
      <div class="captcha-modal-actions">
        <button type="button" class="btn btn-secondary" id="cancelCaptchaBtn">انصراف</button>
        <button type="button" class="btn btn-primary" id="confirmCaptchaBtn">تأیید و ارسال</button>
      </div>
    </div>
  </div>
</div>
```

**توضیح:**
- Modal برای کپچا
- `style="display: none;"`: مخفی به صورت پیش‌فرض
- `{% if contact_form %}`: بررسی وجود فرم
- `{{ contact_form.captcha }}`: نمایش فیلد کپچا

---

## 📝 نکات مهم Template Tags

### 1. Variables
```django
{{ variable }}
```
- نمایش متغیر
- HTML escape می‌شود

### 2. Filters
```django
{{ variable|upper }}
{{ variable|date:"Y-m-d" }}
```
- تبدیل متغیر

### 3. Tags
```django
{% if condition %}
{% for item in items %}
{% url 'app:name' %}
{% static 'path' %}
```
- منطق و کنترل

### 4. Comments
```django
{# این یک کامنت است #}
```
- کامنت در template

### 5. Inheritance
```django
{% extends 'base.html' %}
{% block content %}...{% endblock %}
```
- ارث‌بری template

### 6. Includes
```django
{% include 'partial.html' %}
```
- شامل کردن template دیگر

---

## 🎯 خلاصه

Templates شامل:
- ✅ Template inheritance (base.html)
- ✅ Dynamic content از JSON و Database
- ✅ Loop و Condition
- ✅ Form handling
- ✅ Message display
- ✅ Static files
- ✅ URL generation
- ✅ CSRF protection
- ✅ Custom elements (Web Components)

