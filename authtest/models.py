from django.contrib.admin import forms
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import Group, AbstractUser
from django.contrib.auth.forms import UserCreationForm


# Create your models here.


class Role(models.Model):
    role = models.CharField(max_length=200)

    def __str__(self):
        return self.role


class User(AbstractUser):
    full_name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)  # can login
    staff = models.BooleanField(default=False)  # staff user non superuser
    admin = models.BooleanField(default=False)  # superuser
    timestamp = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)  # role
    USERNAME_FIELD = 'full_name'  # username

    def __str__(self):
        return self.full_name




class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['full_name', 'email', 'password1', 'password2', 'role']
