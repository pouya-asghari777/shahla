from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import GroupAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import Group
from django.contrib.auth import admin as auth_admin

User = get_user_model()


class UserAdmin(auth_admin.UserAdmin):
    list_display = ['email']
    form = UserChangeForm
    add_form = UserCreationForm


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
