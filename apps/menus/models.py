from django.db import models

from apps.foods.models import Food


class Menu(models.Model):
    date = models.DateField(verbose_name='Date', help_text="")

    breakfast = models.ManyToManyField(to=Food, related_name='breakfast_menus', blank=True)
    lunch = models.ManyToManyField(to=Food, related_name='lunch_menus', blank=True)
    evening = models.ManyToManyField(to=Food, related_name='evening_menus', blank=True)
    dinner = models.ManyToManyField(to=Food, related_name='dinner_menus', blank=True)

    created = models.DateTimeField('Created', auto_now_add=True)
    updated = models.DateTimeField('Updated', auto_now=True)

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menus'

    def __str__(self):
        return str(self.date)

    def breakfast_items(self):
        return ', '.join(str(food) for food in self.breakfast.all())

    def lunch_items(self):
        return ', '.join(str(food) for food in self.lunch.all())

    def evening_items(self):
        return ', '.join(str(food) for food in self.evening.all())

    def dinner_items(self):
        return ', '.join(str(food) for food in self.dinner.all())
