# -*- coding: UTF-8 -*-

from django.contrib import admin

from analytics.models import Log, Event

class LogAdmin(admin.ModelAdmin):
    list_display = ('level', 'short_message', 'source', 'host', 'created_at')
    list_display_links = ('short_message',)
    list_filter = ('level', 'created_at')
    search_fields = ('message', 'source', 'host')
    readonly_fields = ('created_at', 'updated_at')

class EventAdmin(admin.ModelAdmin):
    list_display = ('category', 'action', 'label', 'created_at')
    list_display_links = ('label',)
    list_filter = ('created_at',)
    search_fields = ('category', 'action', 'label')
    readonly_fields = ('parameters', 'created_at', 'updated_at')

admin.site.register(Log, LogAdmin)
admin.site.register(Event, EventAdmin)
