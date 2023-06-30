from django.core import serializers
from django.shortcuts import render
from django.utils import timezone
from django.views.generic import TemplateView

from apps.foods.models import Food
from apps.menus.models import Menu


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BaseMenuView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        menu = Menu.objects.filter(date=timezone.now()).last()
        items = self.get_items(menu)
        main = items.filter(type=Food.TYPE_MAIN)
        sides = items.filter(type=Food.TYPE_SIDE)
        drinks = items.filter(type=Food.TYPE_DRINK)
        context.update(main=main, sides=sides, drinks=drinks)
        return context

    def get_items(self, menu):
        raise NotImplementedError


class BreakfastView(BaseMenuView):
    template_name = 'breakfast.html'

    def get_items(self, menu):
        items = menu.breakfast.all()
        return items


class LunchView(BaseMenuView):
    template_name = 'lunch.html'

    def get_items(self, menu):
        items = menu.lunch.all()
        return items


class EveningView(BaseMenuView):
    template_name = 'evening.html'

    def get_items(self, menu):
        items = menu.evening.all()
        return items


class DinnerView(BaseMenuView):
    template_name = 'dinner.html'

    def get_items(self, menu):
        items = menu.dinner.all()
        return items


class AboutView(TemplateView):
    template_name = 'about.html'


class ContactView(TemplateView):
    template_name = 'contact.html'
