from django.contrib import admin
from .models import SiteUser
from django.contrib.sessions.models import Session


@admin.register(SiteUser)
class SiteUserAdmin(admin.ModelAdmin):
    list_display = ('session_key', 'image')


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('objects',)
