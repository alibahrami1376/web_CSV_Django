# 🌐 Portfolio Website - Django

A professional portfolio and resume website built with Django that includes various sections such as biography, projects, blog, and contact.
[website-address](https://thealibahrami.ir/)

## 📋 Table of Contents
- [Features](#-Features)
- [Technologies](#-Technologies)
- [Installation](#Installation)
- [settings](#-settings)



## ✨ Features

### 🏠 Home page (Home)
- Show biography and personal information
- Education section
- Programming languages
- Skills and abilities
- Contact form with CAPTCHA
- Dynamic header with different menu for different pages

### 📝 Weblog (Blog)
- Content Management System with Rich Text Editor (Quill)
- Post Categorisation
- Post Search
- Pagination
- Show Related Posts
- View Count
- Filter by Category

### 💼 (Projects)
- Show list of projects with full details
- Project categories
- Project status (completed, in development, stopped)
- GitHub, demo and website links
- Featured projects
- Advanced search and filtering
- View count

### 🔐 Identity verification
- Registration and login system
- User profile with avatar
- Profile management

### 🎨 User interface 
- Responsive and Mobile-First Design
- Light/Dark Theme Support
- Web Components for Header and Footer
- Use of Feather Icons
- Custom Error Pages (400, 403, 404, 500)

### 🔍 SEO ​​and optimization
- Sitemap.xml
- Robots.txt
- Meta Tags
- Optimized URL Structure

## 🛠 Technologies

### Backend
- **Django 5.2.8** - Core Framework
- **Python 3.12+** - Programming Language
- **PostgreSQL** - Database (can be used with SQLite in development)

### Frontend
- **HTML5/CSS3** - Structure and Styling
- **JavaScript (ES6+)** - Interactions
- **Web Components** - Reusable Components
- **Feather Icons** - Icons


### Libraries and Packages
- `django-quill` - Rich Text Editor
- `django-robots` - Robots.txt Manager
- `django-simple-captcha` - CAPTCHA for Forms
- `django-debug-toolbar` - Debug Tool
- `python-decouple` - Configuration Manager
- `Pillow` - Image Processing
- `gunicorn` - WSGI Server for Production


## 🚀 Installation

### 1. Clone the project

```bash
git clone <repository-url>
cd Web_Csv/web_CSV_Django
```

### 2. Creating a Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```
### 3. Installing dependencies
```bash
pip install -r requirements.txt
```
### 4. Environment Settings

Create a `.env` file in the project root:

In the env.example file, copy the values ​​into env.

Copy the variables from env.example into .env and adjust them based on your environment (development or production).

Uses SQLite as the default database
No additional configuration required

Production Mode (DEBUG=False)

Uses PostgreSQL

Make sure to set correct credentials

DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

### 5. Running Migrations

```bash
python manage.py migrate
```

### 6. Create a Superuser

```bash
python manage.py createsuperuser
```

### 7. Running the Development Server

```bash
python manage.py runserver
```
Then go to the address `http://127.0.0.1:8000`.


## 💻 Use

### Access to the admin panel
1. Go to `http://127.0.0.1:8000/admin`
2. Log in with the superuser you created
3. You can manage blog posts, projects, and contact messages

### Static and Media Files Settings

```python
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

## 👤 Author

**Ali Bahrami**

- GitHub: [@alibahrami1376](https://github.com/alibahrami1376)

## 🙏 Thanks

This course was conducted after watching Mr. Ali Bigdali's course at [MaktabKhooneh](https://maktabkhooneh.org/course/%D8%A2%D9%85%D9%88%D8%B2%D8%B4-%D8%AC%D9%86%DA%AF%D9%88-mk1287/).
 Thank you to  [Mr.Bigdali](https://github.com/AliBigdeli) for the excellent trainin

