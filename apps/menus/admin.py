from django.contrib import admin

from apps.menus.models import Menu


class MenuAdmin(admin.ModelAdmin):
    filter_horizontal = ['breakfast', 'lunch', 'evening', 'dinner']
    list_display = ['date', 'breakfast_items', 'lunch_items', 'evening_items', 'dinner_items']
    list_filter = ['date']


admin.site.register(Menu, MenuAdmin)
