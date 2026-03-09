from django.contrib import admin
from .models import ContactModel, BannerModel, SliderModel


@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'is_read', 'created_at')
    list_filter = ('is_read',)
    search_fields = ('full_name', 'email')


@admin.register(BannerModel)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_filter = ('is_active',)


@admin.register(SliderModel)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'is_active', 'order')
    list_filter = ('is_active',)