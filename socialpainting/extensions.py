from flask.ext.sqlalchemy import SQLAlchemy
from raven.contrib.flask import Sentry


db = SQLAlchemy()
sentry = Sentry(logging=True)
