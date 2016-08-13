# -*- coding: utf-8 -*-
"""
app.main.views
~~~~~~~~~~~~~~

This module implements the main blueprint.

:copyright: (c) 2016 by Benjamin Bertrand.
:license: BSD 2-Clause, see LICENSE for more details.

"""
import redis
from flask import Blueprint, render_template, request, jsonify, current_app, g
from rq import push_connection, pop_connection, Queue
from .. import tasks
from .forms import TaskForm

bp = Blueprint('main', __name__)


def get_redis_connection():
    redis_connection = getattr(g, '_redis_connection', None)
    if redis_connection is None:
        redis_url = current_app.config['REDIS_URL']
        redis_connection = g._redis_connection = redis.from_url(redis_url)
    return redis_connection


@bp.before_request
def push_rq_connection():
    push_connection(get_redis_connection())


@bp.teardown_request
def pop_rq_connection(exception=None):
    pop_connection()


@bp.route('/_run_task', methods=['POST'])
def run_task():
    task = request.form.get('task')
    q = Queue()
    job = q.enqueue(tasks.run, task)
    return jsonify({'job_id': job.get_id()})


@bp.route('/')
def index():
    form = TaskForm()
    return render_template('index.html', form=form)
