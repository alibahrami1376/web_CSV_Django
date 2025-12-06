import json
import logging
from pathlib import Path
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from home.forms import ContactForm, ProfileForm
from home.models import Contact, Profile
from django.http import HttpRequest
from projects.models import Projects
from home.massege import HomeMassege

logger = logging.getLogger(__name__)


def _load_home_content():
    logger.info("Loading home content from JSON file...")
    try:
        content_path = Path(settings.BASE_DIR) / "home" / "content.json"
        with content_path.open(encoding="utf-8") as source:
            content = json.load(source)
            logger.info("Home content loaded successfully!")
            logger.info("Everything is OK!")
            return content
    except Exception as e:
        logger.error(f"Error loading home content: {e}")
        raise


HOME_CONTENT = _load_home_content()
logger.info("HOME_CONTENT initialized")


def home_page(request: HttpRequest):
    logger.info(
        f'Home page accessed by user: {request.user.username if request.user.is_authenticated else "Anonymous"}'
    )
    try:
        projects = Projects.objects.all().order_by("-featured", "-created_date")[:3]
        # logger.info(f'Loaded {projects.count()} projects for home page')
        form = ContactForm()
        logger.info("Home page rendered successfully!")
        return render(
            request,
            "home.html",
            {"content": HOME_CONTENT, "projects": projects, "contact_form": form},
        )
    except Exception as e:
        logger.error(f"Error in home_page view: {e}")
        raise


def save_contact(request: HttpRequest):
    logger.info("save_contact view called")
    if request.method == "POST":
        logger.info("Processing contact form POST request")
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                contact = form.save()
                logger.info(
                    f"Contact form saved successfully: {contact.name} - {contact.email}"
                )
                messages.success(request, HomeMassege.messages_success)
                return redirect("home:home")
            except Exception as e:
                logger.error(f"Error saving contact form: {e}")
                messages.error(request, HomeMassege.messages_error_save)
                return redirect("home:home")
        else:
            logger.warning(f"Contact form validation failed: {form.errors}")
            messages.error(request, HomeMassege.messages_error_filed)
            return redirect("home:home")

    logger.info("save_contact called with non-POST method")
    return redirect("home:home")


def login_view(request: HttpRequest):
    logger.info("login_view accessed")
    if request.user.is_authenticated:
        logger.info(
            f"User {request.user.username} is already authenticated, redirecting to home"
        )
        return redirect("home:home")

    if request.method == "POST":
        username = request.POST.get("username")
        logger.info(f"Login attempt for username: {username}")
        password = request.POST.get("password")

        try:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                logger.info(f"User {username} logged in successfully!")
                logger.info("Everything is OK!")
                messages.success(request, f"خوش آمدید {user.username}!")
                next_url = request.GET.get("next")
                if next_url:
                    logger.info(f"Redirecting to next URL: {next_url}")
                    return redirect(next_url)
                return redirect("home:home")
            else:
                logger.warning(f"Failed login attempt for username: {username}")
                messages.error(request, HomeMassege.message_error_fail_login)
        except Exception as e:
            logger.error(f"Error during login: {e}")
            messages.error(request, HomeMassege.message_error_system_login)

    return render(request, "login.html")


def signup_view(request: HttpRequest):
    logger.info("signup_view accessed")
    if request.user.is_authenticated:
        logger.info(
            f"User {request.user.username} is already authenticated, redirecting to home"
        )
        return redirect("home:home")

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        logger.info(f"Signup attempt for username: {username}, email: {email}")

        # Validation
        if not username or not email or not password1 or not password2:
            logger.warning("Signup failed: Missing required fields")
            messages.error(request, "لطفاً تمام فیلدها را پر کنید.")
            return render(request, "signup.html")

        if password1 != password2:
            logger.warning("Signup failed: Passwords do not match")
            messages.error(request, "رمز عبور و تأیید رمز عبور یکسان نیستند.")
            return render(request, "signup.html")

        if len(password1) < 8:
            logger.warning("Signup failed: Password too short")
            messages.error(request, "رمز عبور باید حداقل 8 کاراکتر باشد.")
            return render(request, "signup.html")

        if User.objects.filter(username=username).exists():
            logger.warning(f"Signup failed: Username {username} already exists")
            messages.error(request, "این نام کاربری قبلاً استفاده شده است.")
            return render(request, "signup.html")

        if User.objects.filter(email=email).exists():
            logger.warning(f"Signup failed: Email {email} already exists")
            messages.error(request, "این ایمیل قبلاً استفاده شده است.")
            return render(request, "signup.html")

        # Create user
        try:
            user = User.objects.create_user(
                username=username, email=email, password=password1
            )
            logger.info(f"User {username} created successfully!")
            messages.success(
                request,
                f"حساب کاربری {username} با موفقیت ایجاد شد! اکنون می‌توانید وارد شوید.",
            )
            return redirect("home:login")
        except Exception as e:
            logger.error(f"Error creating user: {e}")
            messages.error(request, "خطا در ایجاد حساب کاربری. لطفاً دوباره تلاش کنید.")
            return render(request, "signup.html")

    return render(request, "signup.html")


@login_required
def profile_view(request: HttpRequest):
    logger.info(f"Profile view accessed by user: {request.user.username}")
    try:
        profile = request.user.profile
        logger.info(f"Profile found for user: {request.user.username}")
    except Profile.DoesNotExist:
        logger.info(
            f"Profile does not exist for user {request.user.username}, creating new profile"
        )
        profile = Profile.objects.create(user=request.user)
        logger.info("Profile created successfully!")
        logger.info("Everything is OK!")

    if request.method == "POST":
        logger.info(f"Profile update POST request from user: {request.user.username}")
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            try:
                form.save()
                logger.info(
                    f"Profile updated successfully for user: {request.user.username}"
                )
                logger.info("Everything is OK!")
                messages.success(request, "پروفایل شما با موفقیت به‌روزرسانی شد!")
                return redirect("home:profile")
            except Exception as e:
                logger.error(f"Error updating profile: {e}")
                messages.error(
                    request, "خطا در به‌روزرسانی پروفایل. لطفاً دوباره تلاش کنید."
                )
        else:
            logger.warning(f"Profile form validation failed: {form.errors}")
    else:
        form = ProfileForm(instance=profile)

    context = {
        "profile": profile,
        "form": form,
        "user": request.user,
    }
    return render(request, "profile.html", context)


@login_required
def logout_view(request: HttpRequest):
    username = request.user.username
    logger.info(f"User {username} logging out")
    logout(request)
    logger.info(f"User {username} logged out successfully!")
    messages.success(request, "شما با موفقیت از حساب کاربری خود خارج شدید.")
    return redirect("home:home")
