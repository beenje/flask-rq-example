# -*- coding: utf-8 -*-
"""
app.settings
~~~~~~~~~~~~

This module implements the app default settings.

:copyright: (c) 2016 by Benjamin Bertrand.
:license: BSD 2-Clause, see LICENSE for more details.

"""
import os

BOOTSTRAP_SERVE_LOCAL = True
SECRET_KEY = (os.environ.get('SECRET_KEY') or
              b'\x0c\x11{\xd3\x11$\xeeel\xa6\xfb\x1d~\xfd\xb3\x9d\x11\x00\xfb4\xd64\xd4\xe0')
TASKS = ['Short task', 'Long task', 'Task raises error']
MAX_TIME_TO_WAIT = 10
REDIS_URL = 'redis://redis:6379/0'
QUEUES = ['default']
