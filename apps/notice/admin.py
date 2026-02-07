from django.contrib import admin
from .models import Notice

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_by', 'publish_date', 'priority', 'is_active', 'category')
    list_filter = ('is_active', 'priority', 'category')
    search_fields = ('title', 'description', 'posted_by__username')
    readonly_fields = ('created_at',)
