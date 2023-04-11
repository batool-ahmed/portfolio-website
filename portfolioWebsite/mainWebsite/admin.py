from django.contrib import admin
from django.contrib.admin import ModelAdmin
from mainWebsite.models import Portfolio

@admin.register(Portfolio)
class PortfolioAdmin(ModelAdmin):
    list_display = ('title', 'author')
