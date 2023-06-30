from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.users.managers import CustomUserManager


class User(AbstractUser):
    username = models.EmailField('Username', blank=True, null=True)

    email = models.EmailField('Email', unique=True)
    name = models.CharField('Name', blank=True, max_length=255)

    picture = models.ImageField('Profile Picture', upload_to='profile_pictures', null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
