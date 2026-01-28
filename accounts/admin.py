from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("mobile", "email", "is_staff", "is_active")
    search_fields = ("mobile", "email")
    ordering = ("-created_at",)
