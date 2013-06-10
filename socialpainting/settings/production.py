# -*- coding: utf-8 -*-
"""
    socialpainting.settings.production
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains application settings specific to a production
    environment running on Heroku.
"""

import os

from .base import *

#
# Generic
# -------

# If a secret key is set, cryptographic components can use this to sign cookies
# and other things. Set this to a complex random value when you want to use the
# secure cookie for instance.
try:
    SECRET_KEY = os.environ['SECRET_KEY']
except KeyError:
    raise Exception(
        'Application\'s secret key is not set. Secret key is needed to sign '
        "cookies and other things. You can set the secret key by running "
        '"heroku config:add SECRET_KEY=`python manage.py '
        'generate_secret_key`".'
    )

# The debug flag. Set this to True to enable debugging of the application. In
# debug mode the debugger will kick in when an unhandled exception ocurrs and
# the integrated server will automatically reload the application if changes in
# the code are detected.
DEBUG = False


#
# SQLAlchemy
# ----------

SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


#
# Sentry
# ------

SENTRY_DSN = os.environ.get('SENTRY_DSN')


#
# Webassets
# ---------

# Enable/disable webassets debug mode. Possible values are:
#
# False
#     Production mode. Bundles will be merged and filters applied.
# True
#     Enable debug mode. Bundles will output their individual source
#     files.
# 'merge'
#     Merge the source files, but do not apply filters.
ASSETS_DEBUG = False

# Controls whether bundles should be automatically built, and rebuilt, when
# required (if set to True), or whether they must be built manually be the
# user, for example via a management command.
#
# This is a good setting to have enabled during debugging, and can be very
# convenient for low-traffic sites in production as well. However, there is a
# cost in checking whether the source files have changed, so if you care about
# performance, or if your build process takes very long, then you may want to
# disable this.
#
# By default automatic building is enabled, when debugging is enabled.
ASSETS_AUTO_BUILD = False
