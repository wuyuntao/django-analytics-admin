# -*- coding: UTF-8 -*-

from django.db import models
from django.utils.translation import ugettext as _

class Log(models.Model):
    """ A log message, used by DatabaseHandler """

    DEBUG     = 'DEBUG'
    INFO      = 'INFO'
    WARNING   = 'WARNING'
    CRITICAL  = 'CRITICAL'
    ERROR     = 'ERROR'
    EXCEPTION = 'EXCEPTION'

    LEVEL_CHOICES = (
        (DEBUG,     'DEBUG'),
        (INFO,      'INFO'),
        (WARNING,   'WARNING'),
        (ERROR,     'ERROR'),
        (CRITICAL,  'CRITICAL'),
        (EXCEPTION, 'EXCEPTION'),
    )

    level       = models.CharField(_('level'), max_length=10, choices=LEVEL_CHOICES, default=INFO, db_index=True)
    message     = models.TextField(_('message'))
    source      = models.CharField(_('source'), max_length=128, blank=True, db_index=True)
    host        = models.CharField(_('host'), max_length=200, blank=True, null=True)

    created_at  = models.DateTimeField(_('created_at'), auto_now_add=True, db_index=True)
    updated_at  = models.DateTimeField(_('updated_at'), auto_now=True)

    class Meta:
        verbose_name = 'log'
        verbose_name_plural = 'logs'
        get_latest_by = 'created_at'

    def __unicode__(self):
        return u'[%s] %s' % (self.level, self.message)

    def short_message(self, max_length=100):
        return self.message if len(self.message) <= max_length else (u'%s...' % self.message[:max_length])
    short_message.short_description = _('short message')
