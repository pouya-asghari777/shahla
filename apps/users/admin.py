from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.models import Group

User = get_user_model()


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
