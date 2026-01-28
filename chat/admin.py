from django.contrib import admin
from .models import Room, Message 

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("uid", "name")
    filter_horizontal = ("participants",)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("uid", "room", "sender", "created_at", "is_read")
    list_filter = ("is_read",)
    search_fields = ("content",)