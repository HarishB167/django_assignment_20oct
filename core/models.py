from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.contrib import admin

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)


class Address(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="address")
    line1 = models.TextField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    pincode = models.CharField(max_length=255)


class ProfilePicture(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile_picture')
    image = models.ImageField(upload_to='user/profile_pictures')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name

class Profile(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_profile')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='user_profile_item')

    class Meta:
        ordering = ['user__first_name', 'user__last_name']

    def __str__(self):
        return f"{self.profile.name} {self.user.first_name} {self.user.last_name}"

    @admin.display(ordering="profile__name")
    def profile_name(self):
        return self.profile.name
    
    @admin.display(ordering='user__first_name')
    def first_name(self):
        return self.user.first_name

    @admin.display(ordering='user__last_name')
    def last_name(self):
        return self.user.last_name

