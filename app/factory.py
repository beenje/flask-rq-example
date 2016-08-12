# -*- coding: utf-8 -*-
"""
app.factory
~~~~~~~~~~~

Create the WSGI application.

:copyright: (c) 2016 by Benjamin Bertrand.
:license: BSD 2-Clause, see LICENSE for more details.

"""
from flask import Flask
from . import settings
from .extensions import bootstrap
from .main.views import bp as main


def create_app():
    app = Flask(__name__)
    app.config.from_object(settings)
    app.config.from_envvar('LOCAL_SETTINGS', silent=True)
    bootstrap.init_app(app)
    app.register_blueprint(main)
    return app
