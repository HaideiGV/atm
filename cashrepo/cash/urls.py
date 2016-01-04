from django.conf.urls import patterns, include, url
from . import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', views.card_number_page),
    url(r'^pin/$', views.pin_code_page),

]