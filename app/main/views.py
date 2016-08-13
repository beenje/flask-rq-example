# -*- coding: utf-8 -*-
"""
app.main.views
~~~~~~~~~~~~~~

This module implements the main blueprint.

:copyright: (c) 2016 by Benjamin Bertrand.
:license: BSD 2-Clause, see LICENSE for more details.

"""
from flask import Blueprint, render_template, request, jsonify
from .. import tasks
from .forms import TaskForm

bp = Blueprint('main', __name__)


@bp.route('/_run_task', methods=['POST'])
def run_task():
    task = request.form.get('task')
    try:
        result = tasks.run(task)
    except Exception as e:
        return jsonify({'message': 'Task failed: {}'.format(e)}), 500
    return jsonify({'result': result})


@bp.route('/')
def index():
    form = TaskForm()
    return render_template('index.html', form=form)
