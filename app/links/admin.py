from django.contrib import admin

from .models import Link

# Register your models here.

@admin.register(Link)
class AdminLink(admin.ModelAdmin):
    readonly_fields = ('id', 'created_at', 'updated_at')
    list_display = ('id', 'original_url', 'owner', 'created_at')
    fields = ('id', 'original_url', 'owner', 'updated_at', 'created_at')