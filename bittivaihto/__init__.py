# -*- coding: utf-8 -*-
"""
    bittivaihto
    ~~~~~~~~~~~~~~

    This module contains the Flask application core.
"""

import os

from flask import Flask, jsonify, render_template, request
from flask.ext.debugtoolbar import DebugToolbarExtension

from .assets import assets
from .extensions import db, sentry

# Imported here for migrations and testing
# Todo: remove import when imported elsewhere
from bittivaihto.models import SellOrder


class Application(Flask):
    def __init__(self, environment=None):
        super(Application, self).__init__(__name__)
        self._init_settings(environment)
        self._init_extensions()
        self._init_blueprints()
        self._init_errorhandlers()
        self.route('/google78fada8781858043.html')(self._google_verification)


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
        settings_module = 'bittivaihto.settings.' + environment
        self.config.from_object(settings_module)

    def _init_blueprints(self):
        from views import api
        self.register_blueprint(api, url_prefix='/api/v1')

    def _google_verification(self):
        return 'google-site-verification: google78fada8781858043.html'

    def _init_extensions(self):
        """Initialize and configure Flask extensions with this application."""
        assets.init_app(self)
        db.init_app(self)
        DebugToolbarExtension(self)

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
