# -*- coding: UTF-8 -*-

import sys
from django.conf import settings

if not settings.configured:
    settings.configure(
        DATABASE_ENGINE='sqlite3',
        INSTALLED_APPS=[
            'analytics',
        ],
    )

from django.test.simple import run_tests

def runtests(*test_args):
    failures = run_tests(test_args, verbosity=1, interactive=True)
    sys.exit(failures)

if __name__ == '__main__':
    runtests(*sys.argv[1:])
