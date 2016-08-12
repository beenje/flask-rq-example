# -*- coding: utf-8 -*-
"""
app.tasks
~~~~~~~~~

This module implements the tasks to run.

:copyright: (c) 2016 by Benjamin Bertrand.
:license: BSD 2-Clause, see LICENSE for more details.

"""
import random
import time
from flask import current_app


def run(task):
    if 'error' in task:
        time.sleep(0.5)
        1 / 0
    if task.startswith('Short'):
        seconds = 1
    else:
        seconds = random.randint(1, current_app.config['MAX_TIME_TO_WAIT'])
    time.sleep(seconds)
    return '{} performed in {} second(s)'.format(task, seconds)
