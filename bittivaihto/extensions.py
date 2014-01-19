from __future__ import absolute_import

from flask.ext.seasurf import SeaSurf
from flask.ext.sqlalchemy import SQLAlchemy
from raven.contrib.flask import Sentry


csrf = SeaSurf()
db = SQLAlchemy()
sentry = Sentry(logging=True)
