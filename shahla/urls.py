"""shahla URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from apps.menus.views import IndexView, BreakfastView, LunchView, EveningView, DinnerView, AboutView, ContactView

urlpatterns = [
                  path('', IndexView.as_view(), name='index'),
                  path('breakfast/', BreakfastView.as_view(), name='breakfast'),
                  path('lunch/', LunchView.as_view(), name='lunch'),
                  path('evening/', EveningView.as_view(), name='evening'),
                  path('dinner/', DinnerView.as_view(), name='dinner'),
                  path('about/', AboutView.as_view(), name='about'),
                  path('contact/', ContactView.as_view(), name='contact'),
                  path('admin/', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + staticfiles_urlpatterns()

admin.site.site_header = 'Shahla Catering'
