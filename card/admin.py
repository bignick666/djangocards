from django.contrib import admin
from .models import Card, Profile


class CardInline(admin.TabularInline):
    model = Card
    extra = 1


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']
    list_filter = ['username', 'email']
    exclude = ['last_login', 'is_superuser', 'is_active', 'is_staff', 'groups', 'user_permissions']
    inlines = [CardInline]


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['profile', 'series', 'number', 'created_at', 'ended_at', 'status']
    list_filter = ['series', 'number', 'created_at', 'ended_at', 'status']
