# -*- coding: utf-8 -*-
"""
app.main.forms
~~~~~~~~~~~~~~

This module implements the main forms.

:copyright: (c) 2016 by Benjamin Bertrand.
:license: BSD 2-Clause, see LICENSE for more details.

"""
from flask import current_app
from flask_wtf import Form
from wtforms import SelectField


class TaskForm(Form):
    task = SelectField('Task')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.task.choices = [(task, task) for task in current_app.config['TASKS']]
