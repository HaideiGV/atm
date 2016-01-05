from django.contrib import admin
from cash.models import *


class CardAdmin(admin.ModelAdmin):
    fieldsets = ['number', 'status', 'pin']

admin.site.register(Card)
admin.site.register(Transactions)

