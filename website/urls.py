"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import logging
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

logger = logging.getLogger(__name__)
logger.info('URL configuration loaded')
logger.info('Everything is OK!')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("home.urls", namespace="home")),
    path('blog/',include('blog.urls', namespace='blog')),
    path('projects/',include('projects.urls', namespace='projects')),
    path('captcha/', include('captcha.urls')) 
]

# فقط در حالت development static files را serve کن
if settings.DEBUG:
    logger.info('DEBUG mode: Adding static and media file serving')
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    logger.info('Static files configuration completed!')
    logger.info('Everything is OK!')
