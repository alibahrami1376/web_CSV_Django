import json
from pathlib import Path
from django.contrib import messages
from django.contrib.auth import authenticate, login
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
        
        form = ContactForm(request.POST)
        if form.is_valid():
            
            form.save()
            messages.success(request, "فرم با موفقیت ارسال شد!")
            return redirect('home:home')
            
            
            
    return redirect('home:home')

def login_view(request):
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
    