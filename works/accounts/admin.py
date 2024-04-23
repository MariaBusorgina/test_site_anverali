from django.contrib import admin

from .models import CustomerProfile, CustomUser, PerformerProfile


@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user',]
    list_display_links = ['user',]


@admin.register(PerformerProfile)
class PerformerProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user']
    list_display_links = ['user',]


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'role', 'contact', 'experience']
    list_filter = ['role', 'experience']
    search_fields = ['email', 'first_name', 'last_name']