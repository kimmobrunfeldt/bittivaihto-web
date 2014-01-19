# -*- coding: utf-8 -*-
"""
    bittivaihto.settings.test
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    This module contains application settings specific to a automated tests.
"""

from .base import *

#
# Generic
# -------

CSRF_ENABLED = False

# If a secret key is set, cryptographic components can use this to sign cookies
# and other things. Set this to a complex random value when you want to use the
# secure cookie for instance.
SECRET_KEY = 'development key'

# The debug flag. Set this to True to enable debugging of the application. In
# debug mode the debugger will kick in when an unhandled exception ocurrs and
# the integrated server will automatically reload the application if changes in
# the code are detected.
DEBUG = True

TESTING = True


#
# Flask-DebugToolbar
# ------------------

DEBUG_TB_ENABLED = False


#
# SQLAlchemy
# ----------

SQLALCHEMY_DATABASE_URI = 'postgres://postgres@localhost/bittivaihto_web_test'

SERVER_NAME = 'localhost'
