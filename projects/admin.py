from django.contrib import admin
from projects.models import Projects, Category
from django_quill.forms import QuillFormField
from django.db import models


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "created_date")
    list_filter = ("created_date",)
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}
    ordering = ("name",)


@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.TextField: {"form_class": QuillFormField},
    }
    list_display = (
        "title",
        "status",
        "featured",
        "view_count",
        "author",
        "created_date",
    )
    list_filter = ("status", "featured", "category", "created_date")
    search_fields = ("title", "description", "content")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("category",)
    readonly_fields = ("view_count", "created_date", "updated_date")
    date_hierarchy = "created_date"
    ordering = ("-created_date",)

    fieldsets = (
        (
            "اطلاعات اصلی",
            {"fields": ("title", "slug", "description", "content", "image")},
        ),
        ("دسته‌بندی و وضعیت", {"fields": ("category", "status", "featured")}),
        ("لینک‌ها", {"fields": ("github_url", "demo_url", "website_url")}),
        ("اطلاعات تکمیلی", {"fields": ("author", "published_date")}),
        (
            "آمار",
            {
                "fields": ("view_count", "created_date", "updated_date"),
                "classes": ("collapse",),
            },
        ),
    )
