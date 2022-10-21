from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . import models

@admin.register(models.Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['line1', 'city', 'state', 'pincode']


@admin.register(models.ProfilePicture)
class ProfilePictureAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'image']
    list_select_related = ['user']
    ordering = ['user__first_name', 'user__last_name']


@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2',
        'email', 'first_name', 'last_name'),
        }),
    )

@admin.register(models.Profile)
class Profile(admin.ModelAdmin):
    list_display = ['name']

@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['profile_name', 'first_name', 'last_name']
    list_select_related = ['user', 'profile']
    ordering = ['profile__name', 'user__first_name', 'user__last_name']

