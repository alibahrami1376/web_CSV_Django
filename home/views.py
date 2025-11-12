import json
from pathlib import Path

from django.conf import settings
from django.shortcuts import render


def _load_home_content():
    content_path = Path(settings.BASE_DIR) / 'home' / 'content.json'
    with content_path.open(encoding='utf-8') as source:
        return json.load(source)


HOME_CONTENT = _load_home_content()


def home_page(request):
    return render(request, 'home.html', {'content': HOME_CONTENT})
