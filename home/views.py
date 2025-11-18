import json
from pathlib import Path
from django.contrib import messages
from django.conf import settings
from django.http import request
from django.shortcuts import render,redirect
from home.forms import ContactForm

def _load_home_content():
    content_path = Path(settings.BASE_DIR) / 'home' / 'content.json'
    with content_path.open(encoding='utf-8') as source:
        return json.load(source)


HOME_CONTENT = _load_home_content()


def home_page(request):
    return render(request, 'home.html', {'content': HOME_CONTENT})

def save_contact(request:request):
    if request.method == "POST":
        print("input yessssssssss")
        form = ContactForm(request.POST)
        if form.is_valid():
            
            form.save()
            messages.success(request, "فرم با موفقیت ارسال شد!")
            return redirect('home:home')
            
            
            
    return redirect('home:home')
    