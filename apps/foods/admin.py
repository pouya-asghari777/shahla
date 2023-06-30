from django.contrib import admin
from django.utils.html import format_html

from apps.foods.models import Food


class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'description', 'price']
    list_editable = ['price']
    fields = ['name', 'type', 'description', 'price']
    list_filter = ['type']

    # def thumbnail(self, obj):
    #     if obj.picture:
    #         return format_html('<img src="{}" width="80" height="80"/>'.format(obj.picture.url))
    #
    # thumbnail.short_description = ' '


admin.site.register(Food, FoodAdmin)
