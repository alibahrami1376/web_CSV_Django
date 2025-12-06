from django.contrib import admin
from blog.models import Post, Category, Newsletter
from django_quill.forms import QuillFormField
from django.db import models


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {"form_class": QuillFormField},
    }

    date_hierarchy = "creat_date"
    empty_value_display = "-empty"
    list_display = ("title", "counted_view", "status", "published_date", "creat_date")
    list_filter = ("status",)
    search_fields = ["title", "content"]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ("email", "created_date")
    search_fields = ("email",)
    list_filter = ("created_date",)
