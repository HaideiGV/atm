from django.conf.urls import patterns, include, url
from . import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', views.card_number_page),
    url(r'^pin/$', views.pin_code_page),
    url(r'^operations/$', views.operations_page),
    url(r'^balance/$', views.balance_page),
    url(r'^take_cash/$', views.withdraw_cash_page),
    url(r'^report/$', views.report_page),
    url(r'^error/$', views.error_page),

]