# -*- coding: utf-8 -*-
"""
    socialpainting
    ~~~~~~~~~~~~~~

    This module contains the Flask application core.
"""

import os

from flask import Flask, jsonify, render_template, request
from flask.ext.debugtoolbar import DebugToolbarExtension
from flask.ext.xuacompatible import XUACompatible
from flask.ext.security import Security

from .assets import assets
from .extensions import db, sentry, user_datastore

# Todo: remove this import after models are imported elsewhere
from .models import Round, Layer


class Application(Flask):
    def __init__(self, environment=None):
        super(Application, self).__init__(__name__)
        self._init_settings(environment)
        self._init_extensions()
        self._init_blueprints()
        self._init_errorhandlers()

    def _init_settings(self, environment=None):
        """
        Initialize application configuration.

        This method loads the configuration from the given environment
        (production, development, test).  If no environment is given as an
        argument, the environment is read from ``FLASK_ENV`` environmental
        variable.  If ``FLASK_ENV`` is not defined, the environment defaults to
        development.

        The environment specific configuration is loaded from the module
        corresponding to the environment in :module:`.settings`.

        :param environment: the application environment
        """
        if environment is None:
            environment = os.environ.get('FLASK_ENV', 'development')
        settings_module = 'socialpainting.settings.' + environment
        self.config.from_object(settings_module)

    def _init_blueprints(self):
        from .views import pages

        self.register_blueprint(pages)

    def _init_extensions(self):
        """Initialize and configure Flask extensions with this application."""
        assets.init_app(self)
        db.init_app(self)
        DebugToolbarExtension(self)
        XUACompatible(self)
        Security(self, user_datastore)

        # Initialize Raven only if SENTRY_DSN setting is defined.
        if self.config.get('SENTRY_DSN'):
            sentry.init_app(self)

    def _init_errorhandlers(self):
        """Initialize the HTTP error handlers."""
        @self.errorhandler(403)
        def forbidden(error):
            if request.is_xhr:
                response = jsonify(error='Sorry, not allowed')
                response.status_code = 403
                return response
            return render_template('403.html', error=error), 403

        @self.errorhandler(404)
        def page_not_found(error):
            if request.is_xhr:
                response = jsonify(error='Sorry, page not found')
                response.status_code = 404
                return response
            return render_template('404.html', error=error), 404

        @self.errorhandler(500)
        def server_error(error):
            if request.is_xhr:
                response = jsonify(error='Sorry, an error has occurred')
                response.status_code = 500
                return response
            return render_template('500.html', error=error), 500
