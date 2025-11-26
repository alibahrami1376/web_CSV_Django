"""
WSGI config for website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import logging

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'website.settings')

logger = logging.getLogger(__name__)
logger.info('WSGI application is starting...')
logger.info('Everything is OK!')

try:
    application = get_wsgi_application()
    logger.info('WSGI application loaded successfully!')
    logger.info('Everything is OK!')
except Exception as e:
    logger.error(f'Error loading WSGI application: {e}')
    raise
