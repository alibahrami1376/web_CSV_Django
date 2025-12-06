from django.contrib import admin
from home.models import Contact, Profile


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    list_display = ("name", "email", "created_date")
    list_filter = ("email",)
    search_fields = ("name", "message")


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone", "location", "created_date")
    search_fields = ("user__username", "phone", "location")
    list_filter = ("created_date",)
    readonly_fields = ("created_date", "updated_date")
