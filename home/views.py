import json
from pathlib import Path
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.conf import settings
from django.http import request
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from home.forms import ContactForm, ProfileForm
from home.models import Profile
from django.http import HttpRequest
from projects.models import Projects

def _load_home_content():
    content_path = Path(settings.BASE_DIR) / 'home' / 'content.json'
    with content_path.open(encoding='utf-8') as source:
        return json.load(source)


HOME_CONTENT = _load_home_content()


def home_page(request:HttpRequest):
    # دریافت پروژه‌ها از دیتابیس - ابتدا پروژه‌های ویژه، سپس بقیه
    projects = Projects.objects.all().order_by('-featured', '-created_date')[:3]  # نمایش حداکثر 3 پروژه
    
    return render(request, 'home.html', {'content': HOME_CONTENT,'projects':projects})

def save_contact(request:HttpRequest):
    if request.method == "POST":
        
        form = ContactForm(request.POST)
        if form.is_valid():
            
            form.save()
            messages.success(request, "فرم با موفقیت ارسال شد!")
            return redirect('home:home')
            
            
            
    return redirect('home:home')

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
            messages.error(request, f'خطا در ایجاد حساب کاربری: {str(e)}')
            return render(request, 'signup.html')
    
    return render(request, 'signup.html')

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

@login_required
def logout_view(request:HttpRequest):
    logout(request)
    messages.success(request, 'شما با موفقیت از حساب کاربری خود خارج شدید.')
    return redirect('home:home')