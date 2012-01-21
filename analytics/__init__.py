# -*- coding: UTF-8 -*-

import logging
import platform

class DatabaseHandler(logging.Handler):

    HOST = platform.uname()[1]

    def emit(self, record):
        from analytics.models import Log

        source = getattr(record, 'source', record.name)
        Log.objects.create(source=source, level=record.levelname, message=record.msg, host=self.HOST)
