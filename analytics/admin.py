# -*- coding: UTF-8 -*-

from django.contrib import admin

from analytics.models import Log

class LogAdmin(admin.ModelAdmin):
    list_display = ('level', 'short_message', 'source', 'host', 'created_at')
    list_display_links = ('short_message',)
    list_filter = ('level', 'created_at')
    search_fields = ('message', 'source', 'host')
    readonly_fields = ('created_at', 'updated_at')
admin.site.register(Log, LogAdmin)
