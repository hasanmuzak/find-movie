from django.contrib import admin
from .models import CustomUser


# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'first_name', 'last_name', 'is_admin', 'is_active']
    list_display_links = ['id', 'username', 'email']


admin.site.register(CustomUser, CustomUserAdmin)
